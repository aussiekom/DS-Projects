### Independent Component Analysis 

**ICA is yet another dimensionality reduction technique.** Data variables in the model are linear mixtures of some unknown latent variables and the latent variables are called the independent components of the observed data and are non gaussian and mutually independent in nature. ICA is related to principal component analysis and factor analysis.

**The most important part is that ICA assume statistically independent component rather than uncorrelated (such as PCA)**
Principal Component Analysis (PCA) assume data and components are normally distributed, when this requirement is met PCA components are statistically independent. However, in a general case where data distribution is non-gaussian, ICA is a strong method to find independent components Y (sources) representing the data X (signal).

**The two broadest definitions of independence for ICA are:**

* Minimization of mutual information
* Maximization of non-Gaussianity


ICA is important to blind signal separation and has many practical applications. It is closely related to the search for a factorial code of the data. A special variant of ICA is binary ICA in which both signal sources and monitors are in binary form and observations from monitors are disjunctive mixtures of binary independent sources. The mathematical formulation used for the same is given as
<img width="306" alt="Screenshot 2023-11-06 at 10 14 17 AM" src="https://github.com/aussiekom/Data-Science-Projects/assets/102028836/ede2e0e5-3818-4045-84a7-d8988c3a37dd">

where /\ is Boolean AND and \/ is Boolean OR. Note that noise is not explicitly modelled, rather, can be treated as independent sources.

**Before applying the ICA algorithm, we must first “whiten” our signal. To “whiten” a given signal means that we transform it in such a way that potential correlations between its components are removed (covariance equal to 0) and the variance of each component is equal to 1.**

<img width="652" alt="Screenshot 2023-11-06 at 10 15 45 AM" src="https://github.com/aussiekom/Data-Science-Projects/assets/102028836/bd8151e4-bc24-49be-be87-f6bafcea89b1">

The actual way we set about whitening a signal involves the eigen-value decomposition of its covariance matrix. The corresponding mathematical equation can be described as follows;

<img width="297" alt="Screenshot 2023-11-06 at 10 16 08 AM" src="https://github.com/aussiekom/Data-Science-Projects/assets/102028836/536a5e2c-0edd-449c-8186-9e127d43e326">

here D is diagonal matrix of eigenvalues and E is an orthogonal matrix of eigenvectors.

**here is very briefly list the various steps involved in ICA:**

1. Center x by subtracting the mean from it.
2. Whiten x by following the above said procedure.
3. Initializing the value for matrix w randomly.
4. Calculation of updated value of w.
5. Normalizing value of updated w.
6. If the algorithm has not converged then return to step 4, convergence is considered attained when the dot product of w and its transpose is roughly equal to 1.

Finally take the dot product of w and x to get the independent source signals.

**Some of the applications of ICA:**

* optical Imaging of neurons
* modelling receptive fields of primary visual neurons
* neuronal spike sorting
* mobile phone communications
* predicting stock market prices
* face recognition and more.




















