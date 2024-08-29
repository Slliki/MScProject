# EXPLANATION OF CODE
## 1. FNN
### 1. 关于fnn的forward方法
为了使用posweight于损失函数，需要将最后一层结果直接输出（而不经过sigmoid），然后通过BCEwithlogitsLoss将
损失函数转换为0-1. 

### 2. 关于pos_weight
pos_weigh=num_of_neg/num_of_pos,该参数可以让正样本的损失在整体损失中会占更大的比重，从而引导模型更关注正样本。

## 2. Tabnet
### tabnet参数
```python
tabnet = TabNetClassifier(
    device_name=device.type,
    n_d=16, # Feature representation dimension for each decision step. Defaults to 8.
    n_a=16, # Attention representation dimension for each decision step. Defaults to 8.
    n_steps=4, #  Number of decision steps for each model. Defaults to 3.
    optimizer_fn=torch.optim.AdamW,
    optimizer_params=dict(lr=1e-3), # learning rate
)
```

### 1. 自定义tabnet
通过重写train_batch，来使用自定义的损失函数bcewithlogitsloss，以及pos_weight参数。
### 2. 稀疏性损失
```python
# 使用自定义的 compute_loss 函数计算损失
        loss = self.compute_loss(output, y)
        # 将稀疏性损失引入总损失中，这里通过减去稀疏性损失的权重来实现
        loss = loss - self.lambda_sparse * M_loss
```
TabNet 通过稀疏性损失来控制每一层特征选择的稀疏性。稀疏性意味着模型在每次决策中尽量使用少量的输入特征，从而避免了所有特征都参与每个决策过程。这种稀疏性有助于提升模型的解释性，因为它可以明确指出哪些特征在决策过程中起到了关键作用。

稀疏性损失（M_loss） 是通过鼓励稀疏性的惩罚项。如果这个值太大，表示模型选择了太多特征，违反了稀疏性的原则。因此，通过在总损失中减去稀疏性损失乘以权重（lambda_sparse），模型将被迫减少特征选择的数量，以最小化总损失，从而鼓励更稀疏的特征选择。

## 3. CTGAN
```python
# 创建CTGAN实例
ctgan = CTGAN(
    embedding_dim=embedding_dim,
    generator_dim=generator_dim,
    discriminator_dim=discriminator_dim,
    batch_size=batch_size,
    log_frequency=log_frequency,
    verbose=verbose,
    epochs=epochs
)
```
参数说明：
- embedding_dim: 嵌入层维度。用于将分类变量映射到连续的向量空间。
- generator_dim：生成器的维度。定义生成器每一层的神经元数
- discriminator_dim：判别器的维度。定义判别器每一层的神经元数
- batch_size：批处理大小
- The frequency of logging, usually once every certain number of batches.
