## pip install AutoClusterML

## from AutoClusterML import AutoCluster

## a=AutoCluster.autocluster(data,labels=None,clusters=None)

# AutoClusterML

This is a python module for automated dimensionality reduction and clustering (both unsupervised and supervised). 

## Features
* Dimensionality reduction techniques applied based on user request for method and number of components.

* Automated implementation of clustering algorithms on the data (with and without the presence of labels).

* Scatter plots for all clustering algorithms

* Metric based bar plot comparison of clustering algorithms

* Contingency matrices for all clustering algorithms

* Confusion matrices for all clustering algorithms

## dim_reducer

### x_p=dim_reducer(x,method='PCA',components=2)

This function automatically reduces the dimension of the data using 10 different dimensionality reduction techniques namely, PCA, factor

analysis, ICA, Incremental PCA, Kernel PCA, Mini Batch Sparse PCA, NMF, Sparse PCA, Mini batch NMF and SVD respectively.

## autocluster

### a=AutoCluster.autocluster(data,labels=None,clusters=None)

This function automatically applies 13 clustering algorithms, namely, kmeans, kmeans-elkan algorithm, bisectingkmeans,

bisectingkmeans-elkan algorithm, minibatchkmeans, agglomerative, agglomerative-single linkage, agglomerative-complete linkage

agglomerative-average linkage,birch-0.05 threshold,birch-0.1 threshold, birch-0.5 threshold and spectral respectively.

If the labels are not given, only three metrics, namely, the silhouette, davies bouldin and calinski harabasz are used for evaluation.

If the labels are given, the following metrics, namely, 'accuracy','precision','recall','f1','rand','adjusted rand','mutual info',

'adjusted mutual info','fowlkes mallows','homogeneity measure','v measure','silhouette','davies-bouldin','calinski-harabasz','contingency 

matrix','confusion matrix' are used for cluster evaluation.

The function finally returns a table that compares the clustering algorithms with the above mentioned metrices.

## plot_confusion_matrix

### plot_confusion_matrix(a)

This function takes the comparative table as input and plots the confusion matrix for all clustering algorithms.

## plot_scatter_plot

### plot_scatter_plot(data,a)

This function takes the comparative table as input and plots the scatter plot for all clustering algorithms.

## get_metric_plot

### get_metric_plot(a,metric)

This function takes the comparative table as input and plot a bar plot of all clustering algorithms based on the given metric.

## plot_contingency_matrix

### plot_contingency_matrix(a)

This function takes the comparative table as input and plots the contingency matrix for all clustering algorithms.


