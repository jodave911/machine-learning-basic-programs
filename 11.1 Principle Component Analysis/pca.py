
from sklearn.decomposition import PCA
import numpy as np
import matplotlib.pyplot as plt

# Create an array with random values
X = np.random.rand(100,5)

# Fit PCA on X
pca = PCA().fit(X)

# Calculate Variance Explained
var_exp = pca.explained_variance_ratio_

# Calculate Cumulative Variance Explained
cum_var_exp = np.cumsum(var_exp)

# Plot Scree Plot
plt.plot(range(1,len(var_exp)+1), pca.explained_variance_ratio_, 'ro-', linewidth=2)
plt.title('Scree Plot')
plt.xlabel('Principal Component')
plt.ylabel('Variance Explained')
plt.show()

