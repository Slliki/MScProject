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


## 4. evaluate_classifier
```python
def evaluate_classifier(classifier, x_train, y_train, x_test, y_test):
    # Predict the labels for the training set
    y_train_pred = classifier.predict(x_train)
    
    # Predict the labels for the test set using the default threshold (0.5)
    y_pred = classifier.predict(x_test)
    
    # Predict the probability of the positive class for the test set
    y_prob = classifier.predict_proba(x_test)[:, 1]

    # Compute the ROC curve (fpr: false positive rate, tpr: true positive rate, thresholds_roc: thresholds for ROC)
    fpr, tpr, thresholds_roc = roc_curve(y_test, y_prob)
    
    # Compute the Precision-Recall curve (precision, recall: PR curve metrics, thresholds_pr: thresholds for PR curve)
    precision, recall, thresholds_pr = precision_recall_curve(y_test, y_prob)

    # Define the target false positive rate (FPR) for threshold adjustment
    target_fpr = 0.05
    
    # Find the index of the threshold that is closest to the target FPR
    threshold_idx = np.argmin(np.abs(fpr - target_fpr))
    
    # Set the threshold based on the target FPR
    threshold = thresholds_roc[threshold_idx]

    # Apply the new threshold to the predicted probabilities to get the adjusted predictions
    y_pred_threshold = (y_prob >= threshold).astype(int)

    # Print the classification report for the training set
    train_set = print_cls_report(y_train, y_train_pred, title="Train Set")
    
    # Print the classification report for the test set using the default threshold
    default_recall = print_cls_report(y_test, y_pred, title="Default Threshold")
    
    # Print the classification report for the test set using the target FPR threshold
    target_recall = print_cls_report(y_test, y_pred_threshold, title=f'Target Threshold @ {threshold:.2f}')

    # Create a figure with two subplots for the confusion matrices
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))

    # Plot the confusion matrix for the default threshold (0.50)
    default_matrix = plot_con_matrix(ax1, y_test, y_pred, title='Default Threshold @ 0.50')
    
    # Plot the confusion matrix for the target FPR threshold
    target_matrix = plot_con_matrix(ax2, y_test, y_pred_threshold, title=f'Target Threshold @ {threshold:.2f}')

    # Adjust the layout of the plots to avoid overlap
    plt.tight_layout()
    
    # Display the plots
    plt.show()

    # Return the ROC curve metrics, PR curve metrics, and classification reports
    return fpr, tpr, precision, recall, default_recall, target_recall, y_test, y_prob
```

## 5. evaluate_model_with_threshold
```python
def evaluate_model_with_threshold(classifier, X_test, y_test, threshold=0.5):
    # Predict the probability of the positive class for the test set
    y_probs = classifier.predict_proba(X_test)[:, 1]

    # Binarize the predicted probabilities based on the given threshold
    # binarize will convert the probability to 1 if it is greater than the threshold, otherwise 0
    # raval() will convert the 2D array to 1D array
    y_pred = binarize(y_probs.reshape(-1, 1), threshold=threshold).ravel()

    # Generate a classification report comparing the true labels with the predicted labels
    report = classification_report(y_test, y_pred)
    print("Classification Report:\n", report)

    # Compute the confusion matrix comparing the true and predicted labels
    cm = confusion_matrix(y_test, y_pred)

    # Extract true negatives, false positives, false negatives, and true positives from the confusion matrix
    tn, fp, fn, tp = cm.ravel()

    # Calculate the false positive rate (FPR)
    fpr = fp / (fp + tn)

    # Create a figure and axis for plotting the confusion matrix
    fig, ax = plt.subplots(figsize=(8, 6))
    
    # Display the confusion matrix with a color map
    cax = ax.matshow(cm, cmap='GnBu', alpha=0.7)

    # Annotate each cell in the confusion matrix with its count value
    for i in range(cm.shape[0]):
        for j in range(cm.shape[1]):
            # Set text color based on the intensity of the color in the cell
            color = 'white' if cm[i, j] > cm.max() / 2 else 'black'
            ax.text(x=j, y=i, s=cm[i, j], va='center', ha='center', color=color)

    # Set the labels for the x and y axes
    ax.set_xticks([0, 1])
    ax.set_yticks([0, 1])
    ax.set_xticklabels(['No Fraud', 'Fraud'], position=(0.5, 0))
    ax.set_yticklabels(['No Fraud', 'Fraud'])

    # Position the x-axis labels at the bottom of the plot
    ax.xaxis.set_label_position('bottom')
    ax.xaxis.tick_bottom()

    # Set the title and labels for the plot
    plt.title(f'Threshold @ {threshold:.2f} with {fpr * 100:.2f}% FPR')
    plt.xlabel('Predicted Label')
    plt.ylabel('True Label')
    plt.show()

    # Return the classification report and the confusion matrix
    return report, cm
```