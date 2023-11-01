import numpy as np

class NaiveBayesClassifier:
    def __init__(self):
        self.class_probabilities = {}
        self.feature_probabilities = {}

    def fit(self, X, y):
        num_samples, num_features = X.shape
        self.classes = np.unique(y)

        for class_ in self.classes:
            self.class_probabilities[class_] = np.sum(y == class_) / num_samples
            self.feature_probabilities[class_] = {}

            for feature in range(num_features):
                feature_values = X[y == class_, feature]
                self.feature_probabilities[class_][feature] = {
                    'mean': np.mean(feature_values),
                    'std': np.std(feature_values)
                }

    def predict(self, X):
        predictions = []

        for sample in X:
            posterior_probabilities = {}
            for class_ in self.classes:
                class_probability = np.log(self.class_probabilities[class_])
                likelihood = 0
                for feature, value in enumerate(sample):
                    mean = self.feature_probabilities[class_][feature]['mean']
                    std = self.feature_probabilities[class_][feature]['std']
                    likelihood += np.log(self.calculate_probability(value, mean, std))
                posterior_probabilities[class_] = class_probability + likelihood

            predicted_class = max(posterior_probabilities, key=posterior_probabilities.get)
            predictions.append(predicted_class)

        return predictions

    def calculate_probability(self, x, mean, std):
        exponent = np.exp(-((x - mean) ** 2 / (2 * std ** 2)))
        return (1 / (np.sqrt(2 * np.pi) * std)) * exponent

# Example usage:
if __name__ == "__main__":
    # Create a synthetic dataset for binary classification
    X = np.array([[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5]])
    y = np.array([0, 0, 0, 0, 0, 1, 1, 1, 1, 1])

    # Initialize and fit the Naive Bayes classifier
    model = NaiveBayesClassifier()
    model.fit(X, y)

    # Make predictions
    new_samples = np.array([[1, 3], [4, 6]])
    predictions = model.predict(new_samples)

    print("Predictions:", predictions)


