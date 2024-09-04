## 1. Research Background
### 1.1 Introduction
With the popularity of the Internet, online transaction volume is growing rapidly. This trend brings new challenges, especially the increasing sophistication of fraud techniques. Therefore, how to effectively identify and prevent fraudulent activities has become a key issue in this field. Our research focuses on how to predict whether an application is fraudulent based on the applicant's existing characteristics, which can greatly enhance banks' ability to prevent fraud.

Regarding how to process tabular data, although deep learning neural networks have achieved remarkable results in fields such as natural language processing and computer vision, in fact, in many cases, tree-based models often outperform deep learning in tabular data tasks. Model. Therefore, our study also highlights the application of these models in fraud detection.
### 1.2.1 Project Aims

1. **Evaluate Resampling Techniques**  
   - Assess the impact of different resampling strategies on model performance in imbalanced fraud detection datasets.

2. **Benchmark Machine Learning Models**  
   - Compare the effectiveness of various machine learning models, including tree-based and neural network approaches.

3. **Contribute to Best Practices**  
   - Develop guidelines for the implementation of effective and fair fraud detection systems in the banking industry.

4. **Establish a Framework for Future Research**  
   - Identify gaps and propose directions for further investigation in the field of fraud detection.

### 1.2.2 Challenges
1. **Data Imbalance**  
   - Fraudulent transactions are rare, leading to highly imbalanced datasets that can skew model performance.

2. **Large Dataset Complexity**  
   - Managing and processing vast amounts of transaction data poses computational and analytical challenges.

3. **Categorical Data Handling**  
   - The presence of numerous categorical variables complicates feature engineering and model training.

4. **Privacy and Security Concerns**  
   - Ensuring the protection of sensitive financial and personal data is crucial while building and deploying fraud detection models.
   - This field is similar to the medical field. Real data can easily lead to user privacy leakage. Therefore, the training data used cannot be completely real data, which is also an important factor affecting the performance of the model.


## 2. Methodology
### 2.1 Tree based models
明白了，我会将PPT的文字内容进一步简化，以确保简洁明了，同时提供适合演讲的更详细说明。

### 补充后的PPT文字介绍部分：

**2.1 Tree-Based Models**

- **Decision Tree:** Baseline model, splits data based on features.
- **Random Forest:** Ensemble of trees, reduces overfitting.
- **XGBoost:** Optimized gradient boosting, excels with structured data.
- **LightGBM:** Fast and efficient gradient boosting, great for large datasets.



**Presentation Script:**

Now, I’ll briefly introduce the four tree-based models we used in our methodology, with the Decision Tree as our baseline.

First, **Decision Tree** is a basic model that splits data into branches based on feature values. We use it as our baseline because it’s straightforward and provides a benchmark for comparing other models.

**Random Forest** takes this concept further by creating an ensemble of decision trees. It combines their outputs to make more accurate predictions, which also helps reduce the risk of overfitting that a single tree might have.

Next, **XGBoost** is an optimized gradient boosting method. It builds trees in a sequence, where each new tree tries to correct the errors made by the previous ones. This model is particularly effective with structured data, making it a strong candidate for our analysis.
- Regularization: L1 and L2 regularization are introduced in the objective function, which helps to prevent the model from overfitting.

Finally, **LightGBM** is another gradient boosting model, but it’s designed for speed and efficiency, especially with large datasets. It allows us to handle complex models without sacrificing performance.
- 直方图算法（Histogram-based Algorithm）：**Discretize continuous eigenvalues ​​into finite intervals, and then build a histogram based on these intervals**. This method can significantly reduce computational complexity and memory usage, especially on high-dimensional data, and improve the speed of model training.
- 基于叶子（Leaf-wise）的生长策略：XGBoost uses a level-wise growth strategy, that is, all nodes in each layer are split at the same time, while LightGBM adopts a leaf-wise growth strategy, that is, always selecting the leaf node with the largest current gain for splitting.


### 2.3 Deep Learning Models
The first one is **FNN**, which stands for Feedforward Neural Network. We used a simple three-layer feedforward network, where each layer is fully connected, and ReLU is used as the activation function. This model serves as a basic approach to deep learning, providing a solid foundation for comparison with more advanced models.

The second model is **TabNet**. TabNet is specifically designed to handle tabular data, which makes it particularly relevant for our task. It uses a novel approach by applying sequential attention, allowing the model to perform dynamic feature selection at each step of the decision-making process. This helps the model to focus on the most important features and improves its performance on tabular datasets.

These two models offer different perspectives on how deep learning can be applied to our problem, with FNN providing a straightforward approach and TabNet offering a more tailored solution for tabular data.


TabNet is a deep learning model specifically designed for tabular data. It combines an attention-based feature selection mechanism with iterative decision steps, allowing the model to select subsets of features and learn from them. This structure improves performance and interpretability, making TabNet particularly suited for tasks involving structured data. Here's a breakdown of TabNet's structure:

#### 1. **Overall Architecture**
TabNet operates through a multi-step decision process where each step selectively chooses a subset of input features to process, producing partial outputs. These outputs are accumulated over the steps to form the final prediction. This iterative feature selection resembles the stepwise splits in tree-based models.

TabNet's architecture consists of:
- **Feature Transformer**: This part transforms the raw input features into meaningful representations, similar to hidden layers in traditional neural networks.
- **Attentive Transformer**: This component applies attention mechanisms to selectively choose which features to focus on in each decision step.
- **Decision Steps**: Multiple decision steps run sequentially, each selecting features and updating the feature representation progressively.

#### 2. **Feature Selection Mechanism (Attention Masks)**
A unique aspect of TabNet is its **feature selection mechanism**, which relies on **attention masks** to determine which input features will be used in each decision step.

In each step:
- The **Attentive Transformer** assigns a weight to each input feature, indicating how relevant the feature is for that step.
- This attention mask, which is a probabilistic distribution over the input features, selects a subset of features by focusing on the most important ones.
- The selected features are then passed through the **Feature Transformer**, which processes them for the current step.

This selective attention mechanism ensures that the model focuses on a few relevant features in each step, enhancing interpretability and preventing over-reliance on unnecessary features.

#### 3. **Sparsity Regularization**
TabNet includes a sparsity loss (`M_loss`) to control the model’s feature selection behavior. This regularization encourages the model to use as few features as possible in each decision step, improving both generalization and interpretability.

- **M_loss** is computed by summing the feature selection weights across all decision steps. 
- By incorporating this sparsity loss into the total loss, TabNet encourages the model to learn efficient feature representations while minimizing the number of features it uses.

#### 4. **Multiple Decision Steps**
TabNet uses multiple **decision steps** to process the input data iteratively. In each step, the model selects a set of features based on the output of the previous step and processes them.

- The output from each step is passed to the next step, allowing the model to refine its feature selection over time.
- The output from all steps is also accumulated, contributing to the final prediction.

Each decision step has its own independent sparsity loss, which helps ensure that each step only selects the most relevant features.

#### 5. **Workflow of TabNet**
The overall workflow of TabNet can be summarized as:
1. **Input Embedding**: The raw input data is embedded into a higher-dimensional space.
2. **Multiple Decision Steps**: The model iteratively selects features through a series of decision steps. Each step consists of a Feature Transformer and an Attentive Transformer.
3. **Sparsity Control**: The model uses sparsity regularization to minimize the number of features selected in each step.
4. **Cumulative Output**: The outputs from all decision steps are accumulated to generate the final prediction.

#### 6. **Interpretability**
A major strength of TabNet is its interpretability. In each decision step, the model explicitly chooses which features to use, and this feature selection can be visualized through the attention masks. Additionally, sparsity regularization encourages the model to use fewer features, making the decision process more transparent.

#### 7. **Advantages of TabNet**
- **Efficiency for Tabular Data**: Compared to traditional deep learning models, TabNet is better suited for structured tabular data and can handle mixed feature types (categorical and numerical).
- **Interpretability**: The attention-based feature selection allows for a clear understanding of which features the model is using to make predictions.
- **Sparsity**: By enforcing sparsity through regularization, TabNet reduces model complexity while maintaining high predictive performance.

#### Conclusion
TabNet combines neural networks with an attention-based feature selection mechanism, allowing it to process tabular data efficiently. It works through a series of decision steps, using attention masks to selectively choose features at each step. The model's interpretability is enhanced by sparsity regularization, which ensures that only the most relevant features are used in each decision step. This makes TabNet an effective and interpretable model for tabular data tasks.

### 2.4 Resampling
#### 1. Under-sampling
Starting with Under-Sampling, we employed two techniques: Random Under-Sampling and NearMiss. Random Under-Sampling involves reducing the number of majority class samples to balance the dataset, which is straightforward but may risk losing important information. **NearMiss, on the other hand, selects majority class samples that are closest to the minority class, which helps in retaining the most informative data while still balancing the classes**.

#### 2. Oversampling
For Over-Sampling, we used SMOTENC and CTGAN. SMOTENC, or Synthetic Minority Over-sampling Technique for Nominal and Continuous features, generates synthetic samples for the minority class by interpolating between existing minority instances. This technique is particularly effective for datasets with both categorical and continuous features. CTGAN, a Conditional Tabular GAN, generates realistic synthetic data based on the distribution of the minority class, offering another approach to over-sampling that captures the complexity of the original data.

## 3. Pipeline
### 3.1 pipeline
This is a diagram of my entire process. Use mixed sampling for preprocessed data, that is, downsampling first and then upsampling. Upsampling needs to be done in CV. Specifically, after CV divides the new training set and validation set, oversampling is performed using the new training set. This helps prevent data leakage and alleviate overfitting.

CV helps us to get the best parameters combination for each model.

### 3.2 Data exploration
Firstly this is the proportion of fraudulent and non-fraudulent samples in the original dataset. You can see the severe data imbalance.

The second graph shows the total number of samples according to age group as well as the number of fraudulent samples per age group and labelled with the fraud rate per age group.
We can see that the majority of fraud samples occur within the 40 and 50 year old age groups and that the fraud rate increases as age increases.

## 4. Evaluation and Results
### 4.1 Treessss
We use three mixed sampling strategies, each with four tree models trained separately. The evaluation method is to use the default classification threshold and a classification threshold that can achieve 5% fpr. We will focus on the indicators of class 1, because all models perform very well for class 0 and the difference is not much.

First is the first strategy. All models under this strategy do not perform very well. The last three are slightly better than the decision tree.

Then the second strategy uses nearmiss instead of random undersampling It can be seen that the performance of each model has been significantly improved, and xgb and lgbm have the best performance. The f1 of both models is about 5% higher than that of random forest.

The last one, we replace the smote with ctgan.The most obvious change is that under this strategy, if the default classification threshold is used, the fpr of the model is significantly reduced and higher precision is obtained. The price is that recall is relatively reduced. However, when using a classification threshold of 5% fpr, the overall performance of the model is still slightly improved compared with the model under the previous strategy.

### 4.2 Neural network
Tabnet is close to fnn in the recognition of class 0, and significantly improves the recognition of class 1. The confusion matrix also shows that tabnet's fpr is lower than fnn, and the number of misclassified class 1 is about 100 less than fnn.

## 5. Conclusion
### 5.1 Summary
In summary, this study makes several important contributions to the field of bank account fraud detection.

First, we provide a comprehensive evaluation of sampling strategies. We demonstrate the effectiveness of hybrid sampling methods, especially in improving model performance on imbalanced datasets.

Second, we benchmark various machine learning models and show that models such as LightGBM and XGBoost consistently outperform other models, especially when combined with advanced sampling methods.

Third, we improve the accuracy of fraud detection by optimizing the parameters of these models using appropriate sampling strategies.

Finally, we provide a framework for future research and highlight areas that need further exploration, such as integrating other data sources or exploring newer neural network architectures.
### 5.2 Limitations and future work
For the limitations of this study, there are a few things to consider. First off, our exploration of resampling methods might not have been thorough enough. In the future, we could dive into more resampling techniques, like using downsampling methods such as TomekLink. Also, while the model we used gave us some valuable insights, it would be beneficial to explore a wider range of model architectures. This could include trying out other neural network models or even more comprehensive approaches, like stacking different models together.

Another thing we could look into is online fraud detection projects. It might be worth exploring how to perform fraud detection through real-time monitoring using cloud services.