
### 任务二：扩展 WordFreq 应用程序

#### 任务 A - 启动开发实例

1. **登录 AWS Academy 并启动 Learner Lab。**
2. **在实验室屏幕上注意剩余的学分，并在每个会话开始时检查这些学分。**
3. **注意会话时间。在需要刷新此实验室页面并重新打开任何 AWS 控制台页面之前，您有4小时的时间。**
4. **实验室启动后，点击状态为绿色的 'AWS' 按钮，打开一个新的 AWS 控制台页面。**
5. **转到 EC2 服务并启动一个实例，使用以下非默认设置：**
   - AMI：选择 Ubuntu，默认 AMI (Ubuntu Server 22.04 LTS(HVM), SSD Volume Type)。
   - 名称：wordfreq-dev。
   - 实例类型：t2.micro。
   - 密钥对：learnerlab-keypair（创建新密钥对后下载 .pem 文件并保管好！如果在 Windows 上使用 PuTTy，请下载 .ppk 文件）。
   - 安全组：wordfreq-dev-sg，规则：SSH（默认规则）。
   - 存储卷：30GB GP2。
   - IAM 实例配置文件（高级细节下）：选择 EMR_EC2_DefaultRole。

#### 任务 B - 创建 S3 存储桶

1. **使用 EC2 控制台页面左上角的服务下拉菜单选择 S3（最好在新浏览器标签页中打开）。**
2. **创建一个新的 S3 存储桶，此为上传桶，使用以下非默认设置：**
   - 存储桶名称：唯一名称，使用字母数字字符或破折号，例如使用您的首字母或日期；例如：zj-wordfreq-nov23-uploading。
3. **创建第二个 S3 存储桶，此为处理桶，使用以下非默认设置：**
   - 存储桶名称：唯一名称，例如：zj-wordfreq-nov23-processing。
4. **记录存储桶名称以备后用。**
5. **记录存储桶的 ARN（Amazon 资源名称）：在存储桶列表视图中，选择一个队列并点击 'Copy ARN'，然后记录每个存储桶的 ARN 以备后用。**

#### 任务 C - 创建 SQS 队列

1. **使用服务下拉菜单选择 SQS（最好在另一个新浏览器标签页中打开）。**
2. **创建一个新的 SQS 队列（用于文件处理作业），使用以下非默认设置：**
   - 队列类型：标准。
   - 队列名称：wordfreq-jobs。
   - 访问策略：高级。
   - 修改 JSON 策略代码部分。
3. **创建队列后，记录队列 URL（'https://sqs.us-east-1.amazonaws.com/....'）。**
4. **创建第二个 SQS 队列（用于文件处理结果），使用与作业队列相同的配置。**
5. **再次记录创建的队列 URL。**

#### 任务 D - 创建 Amazon SNS 主题

1. **使用服务下拉菜单选择简单通知服务（SNS），最好在另一个新浏览器标签页中打开。**
2. **创建主题，使用以下非默认设置：**
   - 类型：标准。
   - 名称：wordfreq-file-copied。
   - 访问策略：基本，所有人都可以发布消息，所有人都可以订阅。
   - 创建主题并记录您的 SNS ARN。
3. **在左侧导航窗格中，选择订阅。**
4. **为作业队列创建一个订阅：**
   -

 主题：wordfreq-file-copied（选择）。
   - 协议：Amazon SQS。
   - 端点：wordfreq-jobs（选择）。
   - 勾选启用原始消息传递。
5. **创建第二个订阅以发送电子邮件：**
   - 主题：wordfreq-file-copied（选择）。
   - 协议：电子邮件。
   - 端点：您的电子邮件地址（请使用个人地址，例如 Gmail 账户）。
   - 您将收到一封电子邮件以确认此订阅，点击电子邮件中的链接。如果您没有收到链接，请检查您的垃圾邮件文件夹。

#### 任务 E - 从存储桶配置文件复制通知到 SNS

1. **返回 S3 控制台页面，点击您的处理 S3 存储桶（例如 zj-wordfreq-nov23-processing）> 属性。**
2. **向下滚动到 '事件通知'，点击 '创建事件通知'。**
3. **配置以下非默认设置：**
   - 事件名称：file-copied-ev。
   - 事件类型：[选择 '所有对象创建事件']。
   - 目的地：SNS 主题。
   - SNS 主题：[选择 'wordfreq-file-copied']。
4. **如果您成功创建了事件通知，您将收到一封电子邮件。**
5. **返回 SQS 控制台页面，您应该会看到在 wordfreq-jobs 队列中有 1（测试）消息可用。选择 wordfreq-jobs 并点击操作 -> 清除。**


### Task F - 登录开发实例并设置环境

1. **返回 EC2 控制台并选择 wordfreq-dev 实例：**
   - 选中 wordfreq-dev 实例（勾选旁边的复选框）。

2. **连接到实例：**
   - 点击上方的 “Connect” 按钮，然后选择 “SSH client” 选项卡。

3. **根据您的操作系统连接：**
   - 如果您使用的是 Linux 或 MacOS，可直接按照显示的指令在终端窗口中连接。
   - 如果您使用 Windows，则请按照以下页面的 “Prerequisites” 和 “Connecting to your Linux instance” 部分的说明操作：[AWS 官方文档链接](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/putty.html)（适用于 PuTTy - 还有其他 SSH 客户端可供选择）。
   - 还有一个有用的 4 分钟视频可供参考：[Linux Academy 视频链接](https://www.youtube.com/watch?v=bi7ow5NGC-U&lc=Ugh4DAc2SqJj3HgCoAEC)（登录时请确保使用 'ubuntu' 用户名）。

4. **首次登录确认：**
   - 首次登录时，您可能需要确认连接有效，输入 'yes'。

5. **确认成功登录：**
   - 如果您看到类似 'ubuntu@ip-172-XXX-XXX-XXX' 或 ':~ $' 的命令行提示符（可能需要 30 秒才会完全显示），这表明您已成功登录。

6. **更新系统并安装必要工具：**
   - 在 SSH CLI 窗口中运行以下命令来更新系统（可能需要一两分钟）：
     ```
     sudo apt update
     ```
   - 安装 AWS CLI 和 unzip 工具：
     ```
     sudo apt install awscli
     sudo apt install unzip
     ```

7. **安装并配置 Go 语言环境：**
   - 下载 Go 语言包：
     ```
     wget https://go.dev/dl/go1.20.1.linux-amd64.tar.gz
     ```
   - 解压文件并移动到相应目录：
     ```
     sudo tar -C /usr/local -xzf go1.20.1.linux-amd64.tar.gz
     ```
   - 在 `.bash_profile` 中添加 Go 到 `$PATH` 环境变量：
     ```
     vi ~/.bash_profile
     ```
     - 按 'i' 进入 Vi 的插入模式，然后粘贴或输入以下内容：
       ```
       export PATH=$PATH:/usr/local/go/bin
       ```
     - 按 Escape 键退出插入模式
     - 输入 ':wq' 保存并退出 Vi 编辑器
   - 重新加载 profile 并检查 Go 是否安装以及其版本：
     ```
     source ~/.bash_profile
     go version
     ```

   - 如果您看到类似 'go version go1.20.1 linux/amd64' 的输出，表示 Go 已成功安装。

注：稍后退出 SSH 会话时，请输入 `exit`。

---

### Task G - 将应用代码压缩包复制到开发实例

1. **返回 S3 控制台并点击上传 Bucket 名称：**
   - 例如，`zj-wordfreq-nov23-uploading`。

2. **上传课程作业 Zip 文件：**
   - 点击 “Objects” 标签下的 “Upload” 按钮，选择 `lsde-wordfreq-app.zip` 文件上传，或直接将该 Zip 文件拖拽到网页上并确认。

3. **复制 S3 URI：**
   - 上传后，点击文件名链接，然后在打开的文件详情页面找到 S3 URI 并复制下来（用于稍后从 CLI 访问该文件）。
   - 例如，`s3://zj-wordfreq-nov23-uploading/lsde-wordfreq-app.zip`。

4. **检查 S3 Bucket 权限：**
   - 运行以下命令以确保您可以看到您的 S

3 Bucket 名称，这表明您具有正确的权限：
     ```
     aws s3 ls
     ```

5. **从 S3 下载 Zip 文件到开发实例：**
   - 运行以下命令，将您记录下的 'S3 URI' 替换为实际的 S3_URI（不要忘记最后的点号，表示复制到当前目录）：
     ```
     aws s3 cp S3_URI .
     ```

6. **解压缩并检查目录：**
   - 检查您现在是否已在开发实例上下载了 Zip 文件，然后解压缩该包：
     ```
     ls
     unzip lsde-wordfreq-app.zip
     ```
   - 再次运行 'ls' 命令 - 现在您应该看到有一个新的 'lsde-wordfreq-app' 目录。

注：为防万一，我们会保留 Zip 文件，以防您需要完全删除目录及其所有文件并重新开始。在主目录中，您可以使用以下命令执行此操作：`rm -rf lsde-wordfreq-app; unzip lsde-wordfreq-app.zip`。

### Task H - 设置并配置 WordFreq 应用程序

1. **进入应用文件夹并设置执行权限：**
   - 切换到 `lsde-wordfreq-app` 文件夹，并确保所有 shell 脚本具有正确的执行权限：
     ```
     cd lsde-wordfreq-app
     chmod +x *.sh
     ```

2. **运行 setup.sh 脚本：**
   - 这将安装 GO 语言运行环境和任何依赖项，同时创建 DynamoDB 的 'wordfreq' 数据库表：
     ```
     ./setup.sh
     ```
   - 注意：此脚本运行可能需要几分钟，并以 'Setup complete.' 结束。如果显示错误，请再次运行。如果仍有其他错误（忽略 'table already exists' 错误）并且没有得到 'Setup complete'，请在 BB 论坛发帖或预约办公时间。

3. **可选：在 DynamoDB 控制台中查看表：**
   - 在另一个浏览器标签页中打开 DynamoDB 控制台，点击 Tables，选择 wordfreq 并点击 View Items，将显示添加到表中的项目（行）。最初，该表是空的。

4. **手动编辑脚本以引用正确的 SQS 队列 URL：**
   - 假设您将使用 'Vi' 编辑器，但您可以根据需要安装和使用其他编辑器，如 GEdit 或 EMACS。
   - 打开并编辑 `run_worker.sh` 脚本：
     ```
     vi run_worker.sh
     ```
   - 使用箭头键将光标移到以下行：
     ```
     export WORKER_QUEUE_URL="https://sqs.us-east-1.amazonaws.com/12345678/wordfreq-jobs"
     ```
   - 按 'i' 进入插入模式，然后删除 URL 并粘贴或输入您记录的 SQS jobs 队列的 URL。
   - 同样编辑以下行，更新 results 队列的 URL 值：
     ```
     export WORKER_RESULT_QUEUE_URL="https://sqs.us-east-1.amazonaws.com/12345678/wordfreq-results"
     ```
   - 按 Esc 键退出插入模式。
   - 输入 ':wq' 保存并退出 Vi 编辑器。

---
### Task I - 测试 Worker 和上传功能

1. **清空 jobs 队列中的消息：**
   - 回到 SQS 控制台窗口，选择 `wordfreq-jobs` 队列（点击左侧的单选按钮）。
   - 点击 “Purge” 按钮，并在需要时输入 'purge' 以确认您希望删除所有消息。

2. **SSH 窗口：Worker：**
   - 确保您位于正确的目录中，并启动 worker 进程。如果出现错误，请检查 `run_worker.sh` 文件中的 SQS URL。
     ```
     cd ~/lsde-wordfreq-app
     ./run_worker.sh
     ```
   - 您应该看到一些日志输出，当 worker 找到要处理的作业时，这些输出会增加。

   - 注意：WordFreq 的主要进程是这个 'worker' 应用程序，它会持续运行，检查队列上的作业并进行处理。

3. **上传文本文件：**
   - 将任何文本文件（您可以使用 BB 上的 data.zip 中的任何文本文件）上传到您的 'processing' S3 存储桶，例如 `zj-wordfreq-nov23-processing`。

   - 您应该在几分钟后看到 worker 检索作业并成功处理作业。您可以在 DynamoDB 表中检查结果。
   - 您还应该收到一个设置在 SNS 主题中的电子邮件地址发送的电子邮件，其中仅包含已处理的作业消息。注意 S3 信息，包括对象键（文件路径）。

   - 注意：worker 的性能已经被故意削弱，处理过程中增加了额外的 10-20 秒等待时间，您不得修改。这使得在不需要大量输入文件的情况下更容易确保扩展操作有效。

   - 如果您观察到上述输出，基本应用程序正在工作。我们现在只需要将其设置为 Linux 服务。

---

### Task J - 设置 Worker 服务

1. **在 SSH 窗口中：**
   - 按 CTRL+c 退出 `worker.sh` 进程。
   - 通过运行 shell 脚本设置 WordFreq Worker 服务：
     ```
     ./configure-service.sh
     ```
   - 注意 1：此命令将 `Worker.sh` 命令安装为服务，该服务在后台运行，并将在启动时自动启动。自动扩展 EC2 worker 实例需要以这种方式配置此服务。
   - 注意 2：如果没有收到 'Service started successfully' 消息，请再次运行，或重新进行设置过程。如果仍遇到问题，请在 LSDE 的 BlackBoard 论坛发帖或预约办公时间。

2. **查看运行中的 wordfreq worker 服务的输出日志：**
   - 输入以下命令（按 CTRL+c 退出）：
     ```
     sudo journalctl -f -u wordfreq
     ```
   - 注意：要停止或启动 wordfreq worker 服务，请分别运行以下命令：
     ```
     sudo systemctl stop wordfreq
     sudo systemctl start wordfreq
     ```

3. **在处理 S3 存储桶中上传测试文件：**
   - 我们需要再次上传测试文件以检查我们的新服务是否正确处理它。
   - 上传任何文本文件（您可以使用 BB 上的 data.zip 中的任何文本文件）到您的 'processing' S3 存储桶，例如 `zj-wordfreq-nov23-processing`。

4. **再次检查 SSH 窗口显示 worker 输出的日志条目：**
   - 同样，您应该收到一个作业电子邮件。
   - 完成此步骤后，如果不再需要 SSH 窗口，可以按 CTRL+c 关闭，并恭喜自己完成了任务！
   - 但是，在结束此会话之前，建议创建一个 EC2 实例的 AMI 备份。

---

### Task K - 上传文件到您的 S3 上传存储桶

1. **下载

并准备文件：**
   - 从 BB 下载 `data.zip`。
   - 解压下载的文件并查看文件夹中的文件。您应该在文件夹中有大约 120 个文本文件。确保：
     - 文件仅为文本（.txt）格式，不使用二进制文件。
     - 文件名没有空格或非字母数字字符（连字符、下划线可以）。

2. **上传到 S3：**
   - 将这些文件上传到您的 'uploading' S3 存储桶，例如 `zj-wordfreq-nov23-uploading`。

---

### Task L - 将文件复制到您的 S3 处理存储桶以开始处理它们

1. **开始处理文件：**
   - 只需将文本文件（仅限）从上传存储桶复制到处理存储桶，即可开始使用您的 worker 应用服务处理这些文件。
   - 注意：此操作可能需要大约 20 分钟，并且如果成功，将向您的电子邮件地址发送 120 封电子邮件！您只需要一个电子邮件的截图。如果您希望停止接收电子邮件，请在 AWS 中删除 SNS 主题的电子邮件订阅，或点击每封电子邮件中的退订链接。
   - 运行以下 S3 复制命令：

     ```
     aws s3 cp s3://<上传存储桶的名称> s3://<处理存储桶的名称> --exclude "*" --include "*.txt" --recursive
     ```

     例如：
     ```
     aws s3 cp s3://zj-wordfreq-nov23-uploading s3://zj-wordfreq-nov23-processing --exclude "*" --include "*.txt" --recursive
     ```

2. **观察处理日志：**
   - 当应用开始处理文件时，观察处理日志：
     ```
     sudo journalctl -f -u wordfreq
     ```

---
### Task M - 查阅课程文档中的任务

- 实施和测试自动扩展时，您将主要使用我们在这里学到的以下操作：
  - 从上传存储桶复制文件到处理存储桶以开始处理它们（Task L）。
  - 清空队列中的消息（使用 SQS 控制台中的 'purge' 按钮 - Task E(4)）。
  - 在 EC2 实例上查看 worker 日志（Task J/L）。
  - 必要时在 EC2 实例上停止或启动 wordfreq worker 服务（Task J）。
  - 在开发实例上运行 `run_upload.sh` 脚本进行初始测试（Task I）。

注意：我们执行的基础设施配置是功能性的，但不一定是最佳实践。

---

### 重要注意事项

- 完成课程作业会话后，请确保停止任何 EC2 实例以最大限度地减少成本。
  - 注意 1：运行 EC2 t2.micro 实例的大致成本约为每小时 2 美分，但如果从不停止，费用会累积。
  - 注意 2：您不需要为停止的 EC2 实例付费，但仍需要支付其 EBS 存储卷的费用，不过这只是 EC2 成本的一小部分。
- 重启 EC2 实例后，免费的公共 IP 会更改，因此如果您仅通过 IP 地址访问 SSH，则需要复制新的 IP。

---

### 强烈推荐：在结束本次会话前创建 AMI 备份！！

- 从运行中的 EC2 实例创建 AMI 镜像（Instances > 选择 wordfreq-dev > Actions > 'Image and templates' > Create image）。
- 如果您丢失了配置好的 EC2 实例，请咨询教师如何从 AMI 检索配置，或如上所述重建新的 EC2 实例。
- EBS 快照也可以用于存储由实例使用的 EBS 磁盘卷的增量备份。

---

