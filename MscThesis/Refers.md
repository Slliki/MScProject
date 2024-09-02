# References
## 1. (4) Sercan ¨Omer Arik and Tomas Pfister. Tabnet: Attentive interpretable tabular learning.
这篇文章主要介绍了TabNet，一种新的深度学习架构，专门用于处理表格数据。文章讨论了TabNet的核心特点，包括它如何通过逐步注意机制选择在每个决策步骤中要处理的特征，从而实现模型的高效学习和可解释性。TabNet不仅在多个分类和回归任务中表现出色，而且通过实例级的特征选择能力，提供了局部和全局的模型解释。此外，文章还展示了TabNet在自监督学习中的应用，特别是在标签数据较少时的表现提升。总的来说，TabNet不仅在性能上超过了传统的树模型，还具备了更好的可解释性和学习效率。

This article mainly introduces TabNet, a new deep learning architecture specifically designed for processing tabular data. The article discusses the core features of TabNet, including how it selects features to be processed in each decision step through a step-by-step attention mechanism, thereby achieving efficient learning and interpretability of the model. TabNet not only performs well in multiple classification and regression tasks, but also provides local and global model explanations through instance-level feature selection capabilities. In addition, the article also demonstrates the application of TabNet in self-supervised learning, especially the performance improvement when there is less labeled data. In general, TabNet not only outperforms traditional tree models in performance, but also has better interpretability and learning efficiency.

## 2. (15)  S´ergio Jesus, Jos´e Pombal, Duarte Alves, Andr´e Cruz, Pedro Saleiro, Rita Ribeiro, Jo˜ao Gama, and
Pedro Bizarro. Turning the tables: Biased, imbalanced, dynamic tabular datasets for ml evaluation.
这篇文章介绍了一套名为“BAF（Bank Account Fraud）”的数据集套件，该套件用于评估机器学习方法在处理动态、偏斜和不平衡的表格数据时的性能和公平性。文章讨论了当前公平机器学习研究中流行的数据集的不足之处，并提出了BAF数据集作为一种新的资源，旨在更好地反映现实世界中的挑战。

文章重点介绍了如何使用最先进的生成对抗网络（GAN）技术生成BAF数据集，并通过加入噪声和特征选择等方法确保数据的隐私性。BAF数据集的独特之处在于其包含多个具有不同数据偏差的变体，用于测试模型在动态环境下的性能和公平性。

此外，文章还描述了这套数据集的适用性和局限性，并鼓励研究人员和实践者在这一数据集上测试新的机器学习算法和公平性干预方法。文章最后讨论了在使用这些数据集进行模型训练时应注意的隐私保护和信息获取挑战。

This article introduces a suite of datasets called "BAF (Bank Account Fraud)" for evaluating the performance and fairness of machine learning methods when dealing with dynamic, skewed, and unbalanced tabular data. The article discusses the shortcomings of popular datasets in current fair machine learning research and proposes the BAF dataset as a new resource that aims to better reflect real-world challenges.

The article focuses on how to generate the BAF dataset using state-of-the-art generative adversarial network (GAN) techniques and ensure data privacy through methods such as adding noise and feature selection. The BAF dataset is unique in that it contains multiple variants with different data biases to test the performance and fairness of models in dynamic environments.

In addition, the article describes the applicability and limitations of this dataset and encourages researchers and practitioners to test new machine learning algorithms and fairness intervention methods on this dataset. The article finally discusses the privacy protection and information acquisition challenges that should be paid attention to when using these datasets for model training.

## 3. (8) Qizhi Cai and Jiaxin He. Credit payment fraud detection model based on tabnet and xgboot
这篇文章介绍了一种基于TabNet和XGBoost的混合模型，用于信用卡支付欺诈检测。文章讨论了近年来信用卡在电子交易中的广泛使用，以及随之而来的欺诈风险。为了解决这一问题，作者提出了一种结合TabNet和XGBoost的混合模型，并对其在欺诈检测中的表现进行了评估。

TabNet的特征选择与计算：TabNet模型首先通过其注意力机制层（attention transformer layer）选择重要的特征，并使用特征转换层（feature transformer layer）对这些特征进行计算。TabNet模型的设计允许每个样本使用不同的特征集，这在树模型中是无法实现的。TabNet在多个步骤中逐步选择和处理特征，从而构建一个更复杂和灵活的决策流程。

XGBoost的增强树模型：XGBoost是一个广泛应用的增强树模型工具，它通过构建多个决策树来提高模型的预测能力。在这个混合模型中，XGBoost用作模型的另一部分，通过对特征进行进一步的处理和组合来优化预测效果。

混合模型的组合方式：在混合模型中，TabNet首先对输入特征进行处理和选择，生成初步的特征表示。这些表示随后被输入到XGBoost模型中，XGBoost进一步处理这些特征并进行最终的预测。通过这种方式，混合模型结合了TabNet的特征选择能力和XGBoost的强大预测能力，从而提高了欺诈检测的性能。

This article introduces a hybrid model based on TabNet and XGBoost for credit card payment fraud detection. The article discusses the widespread use of credit cards in electronic transactions in recent years and the fraud risks that come with it. To address this issue, the authors proposed a hybrid model combining TabNet and XGBoost and evaluated its performance in fraud detection.

Combination of hybrid models: In the hybrid model, TabNet first processes and selects the input features to generate preliminary feature representations. These representations are then input into the XGBoost model, which further processes the features and makes the final predictions. In this way, the hybrid model combines the feature selection capabilities of TabNet and the strong prediction capabilities of XGBoost, thereby improving the performance of fraud detection.

## 4. (28) Lei Xu, Maria Skoularidou, Alfredo Cuesta-Infante, and Kalyan Veeramachaneni. Modeling tabular data using conditional gan.
这篇文章介绍了CTGAN（条件表格GAN），一种用于生成表格数据的合成数据的新方法。CTGAN通过使用条件生成器和模式特定归一化技术，有效解决了表格数据中的混合类型、不平衡和多模态分布等挑战，在多个数据集上表现优于传统的贝叶斯网络和其他深度学习模型。

This article introduces CTGAN (Conditional Tabular GAN), a new method for generating synthetic data for tabular data. CTGAN effectively addresses challenges such as mixed types, imbalanced, and multimodal distributions in tabular data by using conditional generators and mode-specific normalization techniques, outperforming traditional Bayesian networks and other deep learning models on multiple datasets.


## 5. (10) Tianqi Chen and Carlos Guestrin. Xgboost: A scalable tree boosting system
这篇文章介绍了**XGBoost**，一种高度可扩展的树模型提升系统，广泛应用于数据科学领域。XGBoost通过一系列系统和算法优化，实现了比现有方法更高效的模型训练，能够处理数十亿级别的样本数据。

文章的主要贡献包括：

1. **新颖的稀疏性感知算法**：提出了一种稀疏性感知的算法，用于处理稀疏数据，特别是在数据中有缺失值或是特征经常为零的情况下，提升了算法的性能。

2. **加权分位数草图**：引入了一种加权分位数草图方法，用于在处理具有权重的实例时进行近似树学习，这使得模型在处理不平衡数据时更加高效。

3. **系统设计优化**：通过对缓存访问模式、数据压缩和分片等技术的优化，XGBoost在处理大规模数据时表现出色，能够在内存受限或分布式环境中高效运行。

4. **端到端系统**：XGBoost结合了这些创新技术，构建了一个端到端的系统，可以在极少的资源下处理更大规模的数据。

总的来说，XGBoost凭借其卓越的可扩展性和效率，成为了许多数据科学竞赛中获胜方案的核心组件，被广泛用于各种机器学习任务中。

This paper introduces **XGBoost**, a highly scalable tree model boosting system widely used in data science. XGBoost achieves more efficient model training than existing methods through a series of system and algorithm optimizations, and can handle billions of sample data.

The main contributions of the paper include:

1. **Novel sparsity-aware algorithm**: A sparsity-aware algorithm is proposed to improve the performance of the algorithm for sparse data, especially when there are missing values ​​or features are often zero.

2. **Weighted quantile sketch**: A weighted quantile sketch method is introduced for approximate tree learning when dealing with weighted instances, which makes the model more efficient when dealing with unbalanced data.

3. **System design optimization**: Through optimizations in cache access patterns, data compression, and sharding, XGBoost performs well when dealing with large-scale data and can run efficiently in memory-constrained or distributed environments.

4. **End-to-end system**: XGBoost combines these innovative technologies to build an end-to-end system that can handle larger data with minimal resources.

In general, XGBoost has become the core component of winning solutions in many data science competitions due to its excellent scalability and efficiency, and is widely used in various machine learning tasks.


# Reflection
Based on the comparison between your initial project plan and the current project status, here are some reflections on the progress:

### Achievements
1. **Dataset Exploration and Preprocessing**: 
   - You thoroughly explored the dataset, gaining a deep understanding of its structure, distribution, and potential challenges.
   - You successfully performed necessary preprocessing steps, including handling missing data, feature normalization, and feature selection. This ensured the dataset was well-prepared for model training.

2. **Model Evaluation**:
   - You rigorously evaluated the performance of various models, focusing on tree-based algorithms (XGBoost, LightGBM) and deep learning methods (TabNet).
   - You used appropriate metrics such as F1 scores and ROC curves, which are crucial for assessing model efficacy in fraud detection.
   - By leveraging Kaggle’s cloud computing resources, you overcame local computing limitations and successfully performed cross-validation and hyperparameter tuning.

### Areas Not Fully Explored

1. **Exploring Different Biases**:
   - One of your goals was to test how different biases in the data would affect model performance. The idea was to use the variant datasets from the BAF suite to see how robust the models were in different scenarios.
   - Unfortunately, due to time constraints and some technical hurdles, you didn’t get to dive into this part of the project. This would be a great area to explore in the future to really understand how your models hold up under different conditions.

2. **Trying Out More Resampling Methods**:
   - While you did explore several resampling techniques like random undersampling, NearMiss, SMOTE-NC, and CTGAN, there are still more methods out there that could have been tested.
   - Expanding this exploration could help you find the best ways to handle imbalanced data in fraud detection, so this might be worth revisiting later.

# Future Improvement

1. **Advanced Feature Engineering**: I would explore more sophisticated feature engineering techniques, particularly focusing on deriving new features that could capture complex patterns in the data. For instance, creating interaction terms between key features or applying advanced methods like feature embedding for categorical variables could enhance model performance.

2. **Model Explainability**: I would place a greater emphasis on model interpretability, particularly for the neural network models like TabNet. Techniques such as SHAP (SHapley Additive exPlanations) or LIME (Local Interpretable Model-agnostic Explanations) could be employed to better understand how the model is making decisions, which is crucial in financial applications like fraud detection.

3. **Real-time Model Adaptation**: Given that fraud patterns evolve over time, I would explore online learning techniques that allow models to adapt to new patterns as they emerge, ensuring the model remains effective in a dynamic environment.

4. **Fairness and Bias Mitigation**: Although the project touched on the fairness of models, future work could delve deeper into ensuring that the models do not exhibit any form of bias, especially in sensitive areas like age. Techniques for bias detection and mitigation could be integrated into the model training process.

5. **Enhanced Resampling Techniques**: While the current project used a combination of NearMiss and CTGAN, I would consider experimenting with newer and more advanced resampling techniques or even adaptive synthetic sampling techniques that adjust to the data distribution dynamically during training.

6. **Hybrid Models**: I would also consider the development of hybrid models that combine the strengths of different algorithms, such as integrating tree-based methods with neural networks in a more seamless and structured way, potentially leading to better overall performance.

7. **Scalability and Efficiency**: Considering the large dataset size, I would focus on optimizing the computational efficiency of the models, possibly by leveraging more advanced hardware or distributed computing resources. This could involve parallelizing certain parts of the training process or using more efficient algorithms that are specifically designed to handle large-scale data.

8. **Extended Evaluation Metrics**: I would expand the set of evaluation metrics to include more business-oriented metrics, such as cost-benefit analysis, which takes into account the financial impact of false positives and false negatives in fraud detection. This would ensure that the model is not only accurate but also aligned with business goals.

These improvements could help in developing a more robust, interpretable, and efficient fraud detection system, better suited to the complexities of real-world financial environments.