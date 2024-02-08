import numpy as np
import torch
import torch.nn as nn, torch.optim as optim
import torch.nn.functional as F
from matplotlib import pyplot as plt
from torchvision import datasets, transforms
from torch.utils.data import DataLoader
from torch.utils.tensorboard import SummaryWriter


# LeNet-5示例
class LeNet5(nn.Module):
    def __init__(self):
        super(LeNet5, self).__init__()

        # 定义第卷积层C1, 输入通道为1，输出通道为6，卷积核大小为5(6个5x5的卷积核)
        self.conv1 = nn.Conv2d(1, 6, kernel_size=5)
        # 定义池化层S2，最大池化，窗口大小为2
        self.max_pool2 = nn.MaxPool2d(kernel_size=2, stride=2)
        # 定义第卷积层C3, 输入通道为6，输出通道为16，卷积核大小为5(16个5x5的卷积核)
        self.conv3 = nn.Conv2d(6, 16, kernel_size=5)
        # 定义池化层S4，最大池化，窗口大小为2
        self.max_pool4 = nn.MaxPool2d(kernel_size=2, stride=2)
        # 定义第卷积层C5，可以视为全连接层, 输入通道为16*5*5，输出通道为120。
        self.fc5 = nn.Linear(16 * 5 * 5, 120)
        # 定义全连接层F6，输入维度为120，输出维度为84
        self.fc6 = nn.Linear(120, 84)
        # 定义输出层，输入维度为84，输出维度为10
        self.fc7 = nn.Linear(84, 10)

    def forward(self, x):
        # 通过C1后使用ReLU激活函数
        x = F.relu(self.conv1(x))
        # 通过S2
        x = self.max_pool2(x)
        # 通过C3后使用ReLU激活函数
        x = F.relu(self.conv3(x))
        # 通过S4
        x = self.max_pool4(x)
        # 展平特征图
        # x.view(-1, 16*5*5) 这行代码的作用是将前面卷积层和池化层处理后的多维特征图展平为一维向量。这一步是必要的，因为全连接层（如 self.fc5）期望其输入是一维向量形式，而不是多维特征图。
        x = x.view(-1, 16 * 5 * 5)
        # 通过C5后使用ReLU激活函数
        x = F.relu(self.fc5(x))
        # 通过F6后使用ReLU激活函数
        x = F.relu(self.fc6(x))
        # 输出层
        x = self.fc7(x)
        return x


# 加载数据集
batch_size = 64

# MNIST 数据集的转换器，首先将数据转换为张量，然后标准化
transform = transforms.Compose([
    transforms.Resize((32, 32)),  # LeNet-5 需要 32x32 的输入
    transforms.ToTensor(),
    transforms.Normalize((0.1307,), (0.3081,))
])

# 下载并加载训练集
train_dataset = datasets.MNIST(root='C:\\Users\\yhb\\MscProject\\AI_TA\\data', train=True, download=False, transform=transform)
train_loader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True)

# 下载并加载测试集
test_dataset = datasets.MNIST(root='C:\\Users\\yhb\\MscProject\\AI_TA\\data', train=False, download=False, transform=transform)
test_loader = DataLoader(test_dataset, batch_size=batch_size, shuffle=False)


# train_epoch_losses = []
# test_epoch_losses = []

# 初始化 SummaryWriter
writer = SummaryWriter('runs/LeNet5')

# 通过在循环中调用 writer.add_scalar() 方法，我们可以记录训练和测试损失。这些损失将在 TensorBoard 中显示为图表。
# writer.add_scalar('Loss/train', loss.item(), epoch * len(train_loader) + batch_idx)
# 参数为tag='Loss/train'，scalar_value=loss.item()，global_step=epoch * len(train_loader) + batch_idx
# tag 是一个字符串，用于标识记录的数据。scalar_value 是要记录的数据。global_step 是一个整数，用于标识记录的步数。

def train(model, device, train_loader, optimizer, epoch):
    model.train()
    epoch_loss = 0
    for batch_idx, (data, target) in enumerate(train_loader):
        data, target = data.to(device), target.to(device)
        optimizer.zero_grad()
        output = model(data)
        loss = F.cross_entropy(output, target)
        loss.backward()
        optimizer.step()

        epoch_loss += loss.item()

        # 记录每个批次的训练损失
        writer.add_scalar('Loss/train', scalar_value=loss.item(), global_step= epoch * len(train_loader) + batch_idx)

        if batch_idx % 100 == 0:
            print(
                f"Train Epoch: {epoch} [{batch_idx * len(data)}/{len(train_loader.dataset)} ({100. * batch_idx / len(train_loader):.0f}%)]\tLoss: {loss.item():.6f}")

    # 计算并记录这个epoch的平均损失
    # train_epoch_losses.append(epoch_loss / len(train_loader))


def test(model, device, test_loader):
    model.eval()
    test_loss = 0
    with torch.no_grad():
        for data, target in test_loader:
            data, target = data.to(device), target.to(device)
            output = model(data)
            loss = F.cross_entropy(output, target)

            test_loss += loss.item()

    # 计算并记录这个epoch的平均损失
    # test_epoch_losses.append(epoch_loss / len(test_loader))
    test_loss /= len(test_loader)
    # 记录测试损失
    writer.add_scalar('Loss/test', test_loss, epoch)

    print(f'\nTest set: Average loss: {test_loss:.4f}\n')

# 设置设备并实例化模型，定义损失函数和优化器，开始训练和测试
device = torch.device("cuda" )
# device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model = LeNet5().to(device)
optimizer = optim.Adam(model.parameters())

for epoch in range(1, 4): # 这里只训练了一个epoch
    train(model, device, train_loader, optimizer, epoch)
    test(model, device, test_loader)

# 关闭 SummaryWriter
writer.close()

# # 绘制损失曲线 每个epoch的平均损失
# plt.figure(figsize=(12, 5))
# plt.subplot(1, 2, 1)
# plt.plot(train_epoch_losses, label='Train Loss')
# plt.xlabel('Epoch')
# plt.ylabel('Average Loss')
# plt.title('Train Loss per Epoch')
# plt.legend()
#
# plt.subplot(1, 2, 2)
# plt.plot(test_epoch_losses, label='Test Loss')
# plt.xlabel('Epoch')
# plt.ylabel('Average Loss')
# plt.title('Test Loss per Epoch')
# plt.legend()
#
# plt.tight_layout()
# plt.show()




