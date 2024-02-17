# Worksheet for Bayesian Networks
## Q1: 
<img src="C:\Users\yhb\MscProject\AI_TA\AI\images\img_21.png">

1.(a):独立随机变量的例子：掷一枚公平的硬币的结果（正面或反面）和掷一枚公平骰子的结果（1到6）是独立的随机变量，
因为硬币的结果不影响骰子的结果，反之亦然。

2.(b):

3.(c):
- 要求X Y 独立-->P(X,Y)=P(X)P(Y);
- 计算边缘密度P(Y)=P(Y|X=0)P(X=0)+P(Y|X=1)P(X=1)=P(Y=0, X=0)+P(Y=0, X=1)=0.1+0.3=0.4;
- P(Y=1)=1-P(Y=0)=0.6;
- P(X=0)=0.1/0,4=0.25; P(X=1)=0.3/0.4=0.75;
- a=P(Y=1)P(X=0)=0.6* 0.25=0.15; b=P(Y=1)P(X=1)=0.6*0.75=0.45;

## Q2:
<img src="C:\Users\yhb\MscProject\AI_TA\AI\images\img_22.png">

1.(a):What is the posterior probability, P(S = 1|W = 1), that the sprinkler is on
given that the grass is wet?

```python
# 计算 P(S=1|W=1) 需要的概率值
P_C_T = 0.5  # P(C=T)
P_C_F = 0.5  # P(C=F)

# P(S=1|C)
P_S_T_given_C_T = 0.1
P_S_T_given_C_F = 0.5

# 计算 P(S=1)
P_S_1 = P_S_T_given_C_T * P_C_T + P_S_T_given_C_F * P_C_F

# P(R|C)
P_R_T_given_C_T = 0.8
P_R_T_given_C_F = 0.2
P_R_F_given_C_T = 0.2
P_R_F_given_C_F = 0.8

# P(W=1|S,R)
P_W_T_given_S_T_R_T = 0.99
P_W_T_given_S_T_R_F = 0.9
P_W_T_given_S_F_R_T = 0.9
P_W_T_given_S_F_R_F = 0.0

# P(W=1|S=1)
P_W_T_given_S_T = (P_W_T_given_S_T_R_T * P_R_T_given_C_T * P_C_T + 
                   P_W_T_given_S_T_R_F * P_R_F_given_C_T * P_C_T +
                   P_W_T_given_S_T_R_T * P_R_T_given_C_F * P_C_F + 
                   P_W_T_given_S_T_R_F * P_R_F_given_C_F * P_C_F)

# P(W=1)
P_W_1 = (P_W_T_given_S_T_R_T * P_R_T_given_C_T * P_S_T_given_C_T * P_C_T +
         P_W_T_given_S_T_R_F * P_R_F_given_C_T * P_S_T_given_C_T * P_C_T +
         P_W_T_given_S_F_R_T * P_R_T_given_C_T * (1 - P_S_T_given_C_T) * P_C_T +
         P_W_T_given_S_F_R_F * P_R_F_given_C_T * (1 - P_S_T_given_C_T) * P_C_T +
         P_W_T_given_S_T_R_T * P_R_T_given_C_F * P_S_T_given_C_F * P_C_F +
         P_W_T_given_S_T_R_F * P_R_F_given_C_F * P_S_T_given_C_F * P_C_F +
         P_W_T_given_S_F_R_T * P_R_T_given_C_F * (1 - P_S_T_given_C_F) * P_C_F +
         P_W_T_given_S_F_R_F * P_R_F_given_C_F * (1 - P_S_T_given_C_F) * P_C_F)

# 根据贝叶斯规则计算 P(S=1|W=1)
P_S_1_given_W_1 = P_W_T_given_S_T * P_S_1 / P_W_1
P_S_1_given_W_1
```

2.(b):What is the posterior probability, P(S = 1|W = 1, R = 1), that the sprinkler is
on given that the grass is wet and it is raining?

```python
# Calculate P(R=1) using total probability theorem
P_R_T = (P_R_T_given_C_T * P_C_T) + (P_R_T_given_C_F * P_C_F)

# Calculate P(S=0|R=1)
P_S_F_given_R_T = 1 - P_S_T_given_R_T

# Calculate P(W=1|S=0,R=1)
P_W_T_given_S_F_R_T = P_W_T_given_S_F_R_T

# Calculate the numerator P(S=1,W=1,R=1)
P_S_T_W_T_R_T = P_W_T_given_S_T_R_T * P_S_T_given_R_T * P_R_T

# Calculate the denominator P(W=1,R=1)
P_W_T_R_T = (P_W_T_given_S_T_R_T * P_S_T_given_R_T + 
             P_W_T_given_S_F_R_T * P_S_F_given_R_T) * P_R_T

# Now calculate the conditional probability P(S=1|W=1,R=1)
P_S_T_given_W_T_R_T_alternative = P_S_T_W_T_R_T / P_W_T_R_T

P_S_T_given_W_T_R_T_alternative
```

## Q3:
<img src="C:\Users\yhb\MscProject\AI_TA\AI\images\img_23.png">

一个病人可能有一个症状S，这个症状可以由两种不同的疾病A和B引起。已知一个基因G的存在对于疾病A的表现很重要。贝叶斯网络和条件概率表显示在图2中。
- (a) 一个病人患有疾病A的概率是多少？
- (b) 如果我们知道病人患有疾病B，那么这个病人患有疾病A的概率是多少？
- (c) 如果我们知道病人患有疾病B并且有症状S，那么这个病人患有疾病A的概率是多少？

根据提供的贝叶斯网络和条件概率表，我们可以解答以下三个问题：

(a) 患有疾病A的概率  P(A)  可以通过全概率定理计算出来，它是基因G存在和不存在的条件下患病概率的加权和。

P(A) = P(A|G)P(G) + P(A|¬G)P(¬G)

(b) 如果已知病人患有疾病B，那么这个病人患有疾病A的概率 P(A|B) 可以假设由于缺乏疾病间的直接关联信息，我们可以假设疾病A和B是条件独立的，即疾病A的发生不依赖于疾病B的状态。
--> P(A|B) = P(A)

(c) P(A=1|B=1,S=1) = P(S=1|A=1,B=1)P(A=1|B) / P(S=1|B=1)=P(S=1|A=1,B=1)P(A=1) / P(S=1|B=1)

```python
# Correcting the calculation for P(S|B)
P_S_given_B = (
    (P_S_given_A_B * P_A_given_G * P_G) +
    (P_S_given_not_A_B * (1 - P_A_given_G) * P_G) +
    (P_S_given_A_not_B * P_A_given_not_G * P_not_G) +
    (P_S_given_not_A_not_B * (1 - P_A_given_not_G) * P_not_G)
) * P_B + (
    (P_S_given_A_B * P_A_given_G * P_G) +
    (P_S_given_not_A_B * (1 - P_A_given_G) * P_G) +
    (P_S_given_A_not_B * P_A_given_not_G * P_not_G) +
    (P_S_given_not_A_not_B * (1 - P_A_given_not_G) * P_not_G)
) * P_not_B

# Correcting the calculation for P(A|B,S)
P_A_given_B_S = (P_S_given_A_B * P_A) / P_S_given_B

P_S_given_B, P_A_given_B_S

```

## Q4:
<img src="C:\Users\yhb\MscProject\AI_TA\AI\images\img_24.png">

这个问题是关于贝叶斯网络的随机变量的独立性的。问题可以翻译如下：

（网络图中有3行3列的变量，第一行是 `X1,1`, `X1,2`, `X1,3`，第二行是 `X2,1`, `X2,2`, `X2,3`，第三行是 `X3,1`, `X3,2`, `X3,3`，箭头指示了变量之间的依赖方向）

(a) 哪些随机变量独立于 `X3,1`？
(b) 给定 `X1,1` 的情况下，哪些随机变量独立于 `X3,1`？

---

解答：

(a) 在没有给定任何条件的情况下，`X3,1`与除了直接相连的`X2,1`,`X3,2`非独立，与其他
节点都独立。

(b) 给定 `X1,1` 的情况下，`X3,1`与`X1,2`,`X1,3``X2,2`,`X2,3`独立。