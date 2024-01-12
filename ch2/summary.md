#Statistical Learning

##What is Statistical Learning?

Statistical learning refers to a vast set of tools for understanding data. These tools can be classified as supervised or unsupervised. Broadly speaking, supervised statistical learning involves building a statistical model for predicting, or estimating, an output based on one or more inputs. Unsupervised statistical learning, on the other hand, involves modeling the relationships between the variables to gain an understanding of the underlying structure of the data.

### Prediction

We can predict Y using the following formula:

$$\hat{Y} = \hat{f}(X)$$

where $\hat{f}$ represents our estimate for $f$, and $\hat{Y}$ represents the resulting prediction for $Y$.

The estimation error is given by:

$E(Y - \hat{Y})^2$ = $E[f(X) + \epsilon - \hat{f}(X)]^2$ = $[f(X) - \hat{f}(X)]^2 + Var(\epsilon)$ 

where $E$ represents the expectation, or average, over all possible values of $X$ and $\epsilon$ is a mean-zero random error term, which is independent of $X$ and has variance $Var(\epsilon)$. The irreducible error is a lower bound on the error rate that any method must have, since $Y$ is a function of $X$ and $\epsilon$.

### Inference

Inference refers to the process of drawing conclusions about a population or process based on a sample. Inference is typically concerned with understanding the relationship between $Y$ and $X$, or understanding which predictors are associated with the response. In general, inference refers to the process of learning about $f$ as a function of $X$.

#### Interpretabilty vs Accuracy

In general, as the flexibility of a method increases, its interpretability decreases. Parametric methods provide low-variance but potentially high-bias models, and tend to be more interpretable. Non-parametric methods provide high-variance but potentially low-bias models, and tend to be less interpretable.


