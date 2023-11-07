### Feature Selection

When building a predictive model, we often have many features or variable in our dataset that can be used to train our model. However, just because the feature exists in our dataset does not mean that it is relevant for our model or that we should use it.

How do we know which features to use in our model?

This is where feature selection comes in. **Feature selection is simply a process that reduces the number of input variables, in order to keep only the most important ones.**

There is an advantage in reducing the number of input features, as it simplifies the model, reduces the computation cost, and it can also improve the model’s performance.

Now, how do we decide which feature is important? What does it mean for a feature to be important?

There is no clear answer for that, so we need to experiment with different methods and see which gives the best results.

Here we are going to explore and implement three different feature selection methods:

* variance threshold
* K best features
* recursive feature elimination (RFE)
