# 1. Metrics
## 1.1. KS
KS指标（Kolmogorov-Smirnov Statistic），通常简称为KS值，是一种常用于二分类模型性能评估的统计指标，尤其在金融领域（如信用评分模型）中被广泛使用。它反映了模型区分正类与负类样本的能力。
该值一般越大，表明区分正负样本的能力越好，但是只是将正负样本分开，如果完全区分相反（比如把0识别为1，1识别为）），ks仍然会很高。

KS曲线并不是从FPR（False Positive Rate）和TPR（True Positive Rate）直接得到的。KS曲线的本质是基于正类和负类样本的累积分布函数（CDF），它显示了模型在不同阈值下区分正负样本的能力。

### 正确理解KS曲线

KS曲线的绘制步骤如下：

1. **预测概率排序**：首先，根据模型的预测概率 `y_prob` 对样本进行排序。

2. **计算累积分布函数**：
   - **正类CDF**：计算在不同阈值下，正类样本的累积分布函数，即在每个阈值下，预测为正类的正类样本占所有正类样本的比例。
   - **负类CDF**：计算在不同阈值下，负类样本的累积分布函数，即在每个阈值下，预测为正类的负类样本占所有负类样本的比例。

3. **计算KS值**：KS值是正类CDF和负类CDF之间的最大差值。

4. **绘制KS曲线**：KS曲线通常显示的是正类CDF与负类CDF的差异，最大差值的点即为KS值。

### 与ROC曲线的关系

- **ROC曲线**：绘制的是TPR（True Positive Rate）对FPR（False Positive Rate）的曲线，反映模型的整体分类能力。它通过不同的阈值来展示模型的FPR和TPR之间的关系。

- **KS曲线**：绘制的是正类样本CDF和负类样本CDF之间的差异曲线，强调的是模型在各个阈值下区分正负样本的能力。KS值作为最大差异处的统计量，反映了模型的区分能力。



### 总结

- **KS曲线** 是基于正类和负类累积分布函数（CDF）的差异，而不是FPR和TPR的直接关系。
- **KS值** 是KS曲线中正类和负类累积分布之间的最大差值，代表了模型区分能力的一个重要指标。
- ROC曲线和KS曲线都可以用于评估模型，但它们强调的方面不同。ROC关注整体分类能力，而KS曲线更关注模型在不同阈值下的区分能力。


## 1.2 PR曲线
PR曲线（Precision-Recall Curve）是另一种评价分类模型性能的指标，它展示了在不同阈值下的精确率（Precision）和召回率（Recall）之间的权衡关系。PR曲线的横轴是召回率，纵轴是精确率，曲线下方的面积即为AP值。
曲线越靠近右上角说明模型性能越好，AP值越大。

## Feature Importance
这两部分代码中计算 `importance` 的方式是相同的，都是通过 `feature_importances_` 属性获得的。这意味着它们代表的是同一种度量，即特征对模型预测结果的贡献度。然而，出现特征重要性值范围差异的原因可能与两个模型的具体实现和特征重要性计算方式有关。

### 不同模型的 `feature_importances_` 解释

- **XGBoost 的 `feature_importances_`**:
  - XGBoost 的 `feature_importances_` 通常是归一化的，意味着它们的总和等于 1。这种归一化过程会使得所有特征的重要性值都在 0 到 1 之间。
  - 具体计算方式为：每个特征的重要性等于该特征对每棵树的预测贡献度之和（通常是基于增益），再对所有特征的重要性进行归一化。

- **LightGBM 的 `feature_importances_`**:
  - LightGBM 的 `feature_importances_` 通常是原始的累计值，没有进行归一化。它表示的是该特征被用于分裂节点的总次数或者该特征在提升过程中所带来的总增益。
  - 因此，这些数值可以非常大，特别是在树的数量较多或某个特征被频繁使用时。

### 为什么出现这种差异？

1. **归一化与非归一化**:
   - XGBoost 通常将特征重要性值归一化为 0 到 1 之间的值，因此你看到的 `feature_importances_` 都是小数。
   - LightGBM 返回的是原始的特征重要性值，因此这些值可以大到几百甚至更高。

2. **模型内部计算方式的差异**:
   - 不同的模型在计算特征重要性时使用不同的标准和计算方式。XGBoost 可能更偏向于使用增益或分裂次数来计算重要性，而 LightGBM 可能使用纯粹的累计增益或分裂次数，这使得数值尺度不同。

### 总结

- XGBoost 和 LightGBM 都有自己的 `feature_importances_` 计算方式，导致数值的尺度不同。
- XGBoost 通常会对特征重要性值进行归一化，而 LightGBM 则返回原始累计值，这会导致数值范围不同。
- 在比较两个模型的特征重要性时，建议使用标准化方法或仅比较特征排名，以避免因为数值尺度差异而产生的误导。


# 2. 为什么选择minmax而不是standardscaler?
首先minmax只会缩放特征,不会影响特征分布.
如果原始特征的分布对欺诈识别有重要意义（例如某些特征的分布形态直接关联欺诈行为），那么保留这些特征的原始分布可能有助于提高模型的识别能力。

# 3. TabNet

**TabNet** 是一种专为处理表格数据而设计的深度学习架构，结合了神经网络的强大功能和传统决策树的可解释性。它由 Google Cloud AI 的研究人员 Sercan Ö. Arik 和 Tomas Pfister 于2019年提出。

## 3.1 发展过程与动机

TabNet 的设计初衷是为了克服在处理表格数据时的常见挑战。这些挑战包括：
- 传统机器学习算法（如决策树和随机森林）在表格数据上表现良好，但缺乏神经网络的灵活性和强大的特征提取能力。
- 深度神经网络虽然在许多任务上表现出色，但在表格数据上的表现往往不如传统方法，并且通常缺乏可解释性。

TabNet 通过引入注意力机制来选择在每个决策步骤中使用的特征，从而实现了在保持神经网络灵活性的同时提供可解释性【9†source】【10†source】。

TabNet 通过稀疏性约束（如 sparsemax）来减少不必要的特征影响，这对处理大量分类变量时尤其有用。

## 3.2 算法原理

TabNet 的核心理念是通过逐步处理和决策步骤来选择和使用特征。其主要组成部分包括特征变换器（Feature Transformer）和注意力变换器（Attentive Transformer）。

1. **特征变换器（Feature Transformer）**：
   - 由多个门控线性单元（GLU）层组成，这些层能够高效地处理输入特征并进行特征选择。
   - 前两层 GLU 层的权重在整个网络中共享，确保不同决策步骤之间的一致性，而后两层的权重则是特定于决策步骤的【11†source】。

2. **注意力变换器（Attentive Transformer）**：
   - 使用稀疏选择机制来选择重要的特征。
   - 通过 Sparsemax 正则化来鼓励稀疏性，即仅选择少量重要特征参与每个决策步骤的计算【10†source】。

3. **决策步骤（Decision Step）**：
   - 每个决策步骤通过特征变换器处理输入特征，并通过注意力变换器选择重要特征，然后生成当前步骤的输出。
   - 这些步骤逐步叠加，使模型能够逐步聚焦于最相关的特征，并最终形成决策【12†source】。

## 3.3 算法优点

- **可解释性**：通过生成的特征选择掩码，可以理解模型在每个决策步骤中选择了哪些特征，以及这些特征对最终决策的贡献。
- **高效性**：利用注意力机制，仅在每个步骤中使用最相关的特征，从而提高了模型的参数效率。
- **灵活性**：通过多层特征变换和注意力变换，TabNet 能够高效处理复杂的表格数据，并在多个任务中表现优异【9†source】【10†source】。

TabNet 的引入和发展标志着在表格数据处理领域中的一大进步，结合了深度学习和传统机器学习的优势，为实际应用提供了一个强大的工具。

## 3.4 基本架构
TabNet 是一种用于表格数据的深度学习模型，结合了注意力机制来选择和处理特征。让我详细解释一下数据在进入 TabNet 模型时逐步发生了什么：

1. **输入归一化 (BN)**: 数据首先通过批量归一化层（Batch Normalization，图中标为BN），这是为了稳定模型训练，减少内部协变量偏移。

2. **特征变换 (Feature Transformer)**: 输入的特征会进入一个特征变换模块，这个模块本质上是一个前馈神经网络。特征变换模块将输入的原始特征映射到一个高维空间，并生成新的特征表示。

3. **特征分裂 (Split)**: 特征变换后的输出会被分裂为两部分，一部分会传递到后续的处理步骤，另一部分会被传递给“注意力变换器”（Attentive Transformer）。

4. **注意力变换器 (Attentive Transformer)**: 这是TabNet的核心模块。注意力变换器生成一个掩码（Mask），这个掩码会根据输入的特征来动态选择最重要的特征子集。这个掩码确保了模型在每一步只关注于最相关的特征，而忽略不重要的部分。

5. **掩码应用 (Mask)**: 掩码应用后，选中的特征会经过特征聚合（Agg.），这里的操作类似于特征加权求和。此过程帮助模型逐步聚焦于最关键的信息。

6. **步骤迭代 (Step 1, Step 2, ...)**: 图中的Step 1和Step 2表示这个过程会重复多次，每一步都会对特征进行进一步的处理和筛选。每一步之后的输出特征会被送回特征变换模块，并再次通过上述流程进行进一步处理。

7. **输出层 (FC)**: 最终，通过所有步骤处理后的特征会被传递到一个全连接层（FC），用于最终的输出，比如分类或回归任务中的预测结果。

在这个过程中，TabNet通过注意力机制实现了特征选择的自适应性，能够在训练过程中自动学习哪些特征最为重要，从而有效地提高了模型的性能和解释性。

总结来说，TabNet模型通过多次特征变换和注意力机制，逐步提炼和聚焦于输入数据中最相关的特征，从而生成预测输出。

![RF_CV-smote.png](./imgs/refer/tabnet_structure.png)

![img.png](imgs/refer/process_tabnet.png)

## 3.5 Custom TabNet
这段代码定义了一个自定义的分类器 `CustomTabNetClassifier`，它继承了 `pytorch-tabnet` 库中的 `TabNetClassifier`。这个自定义分类器的主要目的是为了在处理二分类问题时，使用带有 `pos_weight` 参数的损失函数，以应对类别不平衡问题。让我们逐步解析这段代码：

```python
class CustomTabNetClassifier(TabNetClassifier):
    def __init__(self, pos_weight, *args, **kwargs):
        super(CustomTabNetClassifier, self).__init__(*args, **kwargs)  # Initialize the parent TabNetClassifier class
        self.loss_fn = nn.BCEWithLogitsLoss(pos_weight=pos_weight.to(self.device))  # Define a custom loss function with pos_weight to handle class imbalance
    
    def compute_loss(self, y_pred, y_true):
        y_true = y_true.to(self.device)  # Move ground truth labels to the same device as the model
        y_pred = y_pred.squeeze(dim=-1)  # Remove the last dimension from predictions if it's 1 (for compatibility)
        return self.loss_fn(y_pred, y_true)  # Compute and return the loss using the custom loss function
    
    def _train_batch(self, X, y):
        self.network.train()  # Set the network in training mode
        X, y = X.to(self.device), y.to(self.device)  # Move the input data and labels to the device (e.g., GPU)
        for param in self.network.parameters():
            param.grad = None  # Clear the gradients of the network parameters
        output, M_loss = self.network(X)  # Perform forward pass through the network to get the output and the sparsity loss
        loss = self.compute_loss(output, y)  # Compute the main loss using the custom compute_loss function
        loss = loss - self.lambda_sparse * M_loss  # Adjust the loss by subtracting the sparsity loss weighted by lambda_sparse
        loss.backward()  # Perform backpropagation to calculate gradients
        self._optimizer.step()  # Update the network parameters using the optimizer
        return {"loss": loss.item(), "batch_size": X.size(0)}  # Return the loss value and the batch size as a dictionary
```

### 1. **类定义与初始化**
```python
class CustomTabNetClassifier(TabNetClassifier):
    def __init__(self, pos_weight, *args, **kwargs):
        super(CustomTabNetClassifier, self).__init__(*args, **kwargs)
        self.loss_fn = nn.BCEWithLogitsLoss(pos_weight=pos_weight.to(self.device))
```
- `CustomTabNetClassifier` 继承自 `TabNetClassifier`。
- 在 `__init__` 方法中，首先调用了父类的初始化方法 (`super(CustomTabNetClassifier, self).__init__(*args, **kwargs)`)，这样可以确保 `TabNetClassifier` 的所有初始化步骤都正常进行。
- `self.loss_fn` 定义了一个自定义的损失函数，它是 `nn.BCEWithLogitsLoss`，这个损失函数适用于二分类问题。在这里，特别指定了 `pos_weight` 参数，这个参数通常用于处理类别不平衡问题，给正类加权。`pos_weight` 被转换到设备（通常是 GPU）上。

### 2. **计算损失函数**
```python
    def compute_loss(self, y_pred, y_true):
        y_true = y_true.to(self.device)
        y_pred = y_pred.squeeze(dim=-1)
        return self.loss_fn(y_pred, y_true)
```
- `compute_loss` 方法计算预测值 (`y_pred`) 和真实值 (`y_true`) 之间的损失。
- `y_true` 被转移到相同的设备上，以确保计算时在同一设备上进行。
- `y_pred` 使用 `squeeze` 方法去除最后一维度（如果它是 1），以匹配 `y_true` 的形状。
- 返回计算后的损失值。

### 3. **训练单个批次**
```python
    def _train_batch(self, X, y):
        self.network.train()  # 设置网络为训练模式
        X, y = X.to(self.device), y.to(self.device)  # 数据转移到设备上
        for param in self.network.parameters():
            param.grad = None  # 清除之前的梯度
        output, M_loss = self.network(X)  # 前向传播，获取输出和稀疏性损失
        loss = self.compute_loss(output, y)  # 计算损失
        loss = loss - self.lambda_sparse * M_loss  # 加上稀疏性损失项
        loss.backward()  # 反向传播计算梯度
        self._optimizer.step()  # 更新模型参数
        return {"loss": loss.item(), "batch_size": X.size(0)}  # 返回损失值和批次大小
```
- `_train_batch` 方法是对训练过程中单个批次数据的处理。
- `self.network.train()` 将网络设置为训练模式（区别于评估模式）。
- 输入数据 `X` 和标签 `y` 都被转移到设备上（通常是 GPU）。
- 通过 `self.network(X)` 前向传播获取输出 `output` 和稀疏性损失 `M_loss`。
- 计算 `output` 和 `y` 之间的损失 `loss`，并且减去稀疏性损失乘以权重 `lambda_sparse`。
- 通过 `loss.backward()` 进行反向传播，计算梯度。
- 使用优化器 `self._optimizer.step()` 更新模型参数。
- 最后返回一个字典，包含损失值和批次大小。

### 4. **整体逻辑**
这个自定义的分类器通过重写 `compute_loss` 和 `_train_batch` 方法，实现在训练过程中使用自定义的损失函数（考虑了类别不平衡问题）。另外，它还通过 `_train_batch` 方法自定义了训练流程，确保在训练时正确计算损失并更新模型参数。

# 4. 过采样和欠采样的顺序
如果数据量非常大，并且多数类样本占据了绝对主导地位，先进行下采样是一个合理的选择。这有助于控制数据集的规模，使得后续的上采样和模型训练更为高效。然后，可以视情况再进行上采样，以确保少数类样本得到充分的关注。

由于我数据很大，先下采样可以有效去除无用数据（并且原始论文，即生成我使用这个数据集的论文作者提到，他们生成数据时未来防止隐私泄露问题，添加了噪声），因此先下采样可以有效去除无用样本，节省计算资源。

## 4.1 关于smote和CV

在交叉验证过程中自动应用。每次交叉验证划分出新的训练集（例如4折作为训练集）后，这些方法会对新的训练集进行过采样。

使用 SMOTE（Synthetic Minority Over-sampling Technique）作为策略，在交叉验证过程中每次划分训练集后进行过采样，有以下几个优点：

### 1. **基于当前训练集的自适应过采样**
   - **动态处理不平衡**：在每次交叉验证中，SMOTE会根据当前折叠训练集的类别分布进行过采样，这意味着它能自适应地应对训练集中类别不平衡的情况。每次新的训练集可能会有不同的少数类比例，SMOTE能够动态调整生成样本的数量和分布，确保模型在各个折叠上都能接收到足够的少数类样本。
   - **减少过拟合的风险**：由于SMOTE生成的样本是在每个折叠的训练集上进行的，而不是在整个数据集上一次性生成，这可以帮助减少过拟合的风险。模型不会过于依赖某一组特定的生成样本，从而提高泛化能力。

### 2. **提高模型的泛化能力**
   - **增强样本多样性**：每次交叉验证的训练集不同，SMOTE在不同的训练集上生成的新样本也会有所不同。这种多样性有助于模型在训练时接触到更加多样化的少数类样本，从而提高模型的泛化能力。
   - **应对数据不一致性**：在真实世界的数据中，数据集可能在不同的采样中存在不一致性。SMOTE在每个折叠上独立生成数据，可以帮助模型更好地学习应对这些不一致性。

### 3. **更真实的模型评估**
   - **避免数据泄露**：如果在整个数据集上先过采样再进行交叉验证，可能会导致数据泄露问题，即测试集的数据分布可能已经被模型“看过”或“学习”过。而通过在交叉验证的每个折叠中进行过采样，可以确保生成的样本只在训练集中出现，测试集保持完全独立，从而提供更真实的模型评估结果。
   - **反映真实场景**：在实际应用中，模型可能会面对各种不同的数据分布情况。通过在交叉验证期间动态生成数据，模型可以模拟这种变化，从而在真实应用中表现得更加稳健。

### 4. **操作简单且适用性广**
   - **自动化流程**：在交叉验证过程中嵌入SMOTE，可以将过采样过程自动化处理，减少手动调控的复杂性。这使得模型开发流程更加流畅，适合快速迭代和实验。
   - **兼容性好**：SMOTE 可以轻松与各种机器学习模型和框架集成，如 `scikit-learn` 的 `pipeline`，这使得其在实际应用中非常方便，适用于多种不平衡分类任务。

### 5. **避免冗余和浪费计算资源**
   - **局部生成**：SMOTE只在当前的训练集上生成样本，不会浪费计算资源在不必要的样本生成上。这与全局性生成模型（如CTGAN）不同，后者可能需要大量计算资源来生成整个数据集的样本。


在交叉验证中使用SMOTE进行动态过采样，可以根据每个折叠的训练集情况灵活调整，增强模型的泛化能力，提供更真实的评估结果，并有效避免数据泄露和过拟合。这种方法简单、高效且广泛适用于不平衡数据集的分类任务。

## 4.2 关于strategy=‘ctgan'
CTGAN 由于其复杂性，需要在交叉验证之前对整个训练集进行一次性训练，然后生成新的少数类样本。在这种情况下，CTGAN 不会在每个交叉验证折叠中独立训练并生成样本，而是先用整个训练集训练一个模型，再生成合成样本。这些合成样本会与原始训练集一起用于所有的交叉验证折叠。

CTGAN（Conditional Tabular Generative Adversarial Network）是一种用于生成表格数据的生成对抗网络（GAN），它的训练和数据生成过程与像SMOTE和ADASYN这样的传统过采样方法有本质上的不同。这种不同的设计决定了它在应用上的一些特殊性。以下是一些关键原因：

### 1. **CTGAN的复杂性和生成过程**
   - **模型训练需求**：CTGAN 是一个生成模型，需要对整个数据集进行全面学习。它通过模拟数据的复杂分布来生成新的样本，这一过程需要较大的数据量和较长的训练时间。在每次交叉验证的折叠中都单独训练CTGAN模型并生成样本，不仅耗时耗力，而且可能导致生成样本的质量不一致。
   - **生成样本的依赖性**：CTGAN生成的样本质量高度依赖于模型的训练过程。每次折叠中重新训练CTGAN可能会由于训练数据的变化导致生成样本的不一致性，从而影响模型评估的稳定性和可信度。

### 2. **CTGAN的生成方式与目标**
   - **全局数据分布学习**：CTGAN旨在学习整个数据集的全局分布，并基于此生成新的数据。因此，它更适合在使用完整训练集时进行训练，确保它能够学习到数据的全貌。
   - **生成多样性与稳定性**：在生成过程中，CTGAN会利用学到的全局数据分布生成与原始数据相似但不同的样本。这些生成的样本是基于整体数据的分布，因此在交叉验证之前一次性生成样本，更能保证生成数据的多样性和稳定性。

### 3. **与传统方法的对比**
   - **SMOTE/ADASYN的局部生成方式**：像SMOTE和ADASYN这样的算法，它们的原理是通过在少数类样本的局部邻域中生成新样本，这些方法对数据分布的依赖性较小，可以在每个折叠中独立运行而不会显著影响生成结果。
   - **CTGAN的全局生成方式**：CTGAN基于对整体数据分布的理解进行数据生成，因此不适合在每个折叠中单独运行。每次单独训练CTGAN可能导致不一致的数据生成过程，从而影响评估结果的可靠性。

### 4. **效率与可重复性**
   - **时间与资源消耗**：CTGAN训练相对耗时，并且需要大量计算资源。如果在每个交叉验证折叠中都重新训练CTGAN，时间和资源消耗会显著增加，而其生成的样本可能在每次训练中都有所不同，导致评估结果的不一致性。
   - **评估的一致性**：通过在交叉验证之前使用整个训练集生成数据，CTGAN能够确保在整个交叉验证过程中使用相同的合成数据集，从而提高评估结果的可重复性和一致性。

### 总结：
CTGAN 的设计初衷是学习和生成高质量的合成数据，其训练过程复杂且耗时。为了确保生成样本的稳定性、一致性和多样性，CTGAN 通常在交叉验证之前对整个训练集进行一次性训练和数据生成。与之相比，SMOTE和ADASYN更适合在每个折叠中动态生成数据，因为它们的生成过程依赖于局部数据分布，并且不需要像CTGAN那样复杂的模型训练过程。这些差异解释了为什么CTGAN采取不同的处理方式。