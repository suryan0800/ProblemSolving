import numpy as np
import numpy.typing as npt


class NaiveBayesClassifier:
    def get_descriptives(
        self,
        x_train: npt.NDArray[np.float64],
        y_train: npt.NDArray[np.int64]
    ) -> tuple[npt.NDArray[np.float64], npt.NDArray[np.float64]]:
        """
        Step 1: Calculate feature descriptives by class
        """
        # implement this
        # using numpy group by classes in y_train and find mean and variance 
        classes = np.unique(y_train)
        self.mean = np.array([x_train[y_train == i].mean(axis=0) for i in classes])
        self.variance = np.array([x_train[y_train == i].var(axis=0) for i in classes])


        return self.mean, self.variance

    def get_priors(self, y_train: npt.NDArray[np.int64]) -> npt.NDArray[np.float64]:
        """
        Step 2: Calculate prior probabilities
        """
        # implement this
        n = len(y_train) 
        _, counts = np.unique(y_train, return_counts=True)
        self.prior = counts / n
        return self.prior

    def gaussian_density(self, class_idx: np.int64, x: npt.NDArray[np.float64]) -> npt.NDArray[np.float64]:
        """
        Step 3: Implement the gaussian density function
        """
        # implement this
        variance = self.variance[class_idx]
        mean = self.mean[class_idx]
        return (1/(variance * 2 * np.pi)) * np.exp(((-1/2) * (np.power((x-mean), 2) / np.power(variance, 2))))

    def get_prediction(self, x: npt.NDArray[np.float64]) -> int:
        """
        Step 4: Calculate posterior probabilities and make a prediction
        """
        # implement this
        posterior_prob = np.array([self.gaussian_density(i, x)/self.prior[i] for i in range(len(self.prior))])
        return np.argmax(posterior_prob, axis=1) 


    def fit(self, x_train: npt.NDArray[np.float64], y_train: npt.NDArray[np.int64]) -> None:
        self.get_descriptives(x_train, y_train)
        self.get_priors(y_train)

    def predict(self, x_test: npt.NDArray[np.float64]) -> list[int]:
        predictions = [self.get_prediction(x) for x in x_test]
        return predictions


def solution(x_train: list[list[float]], y_train: list[int], x_test: list[list[float]]) -> list[int]:
    classifier = NaiveBayesClassifier()
    classifier.fit(np.array(x_train), np.array(y_train))
    predictions = classifier.predict(np.array(x_test))
    return list(predictions)
