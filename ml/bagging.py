from random import randint, seed
import numpy as np 

from sklearn.tree import DecisionTreeClassifier


def bootstrap(n: int) -> list[int]:
    """
    Step 1: Bootstrap the train samples for each base classifier.
    """
    # implement this
    lst = []
    for i in range(n): 
        val = randint(0, n-1)
        lst.append(val) 
    return lst


def fit(classifiers: list[DecisionTreeClassifier], x: list[list[float]], y: list[int]):
    """
    Step 2: Train each classifier based on its own bootstrapped samples.
    """
    n = len(x)
    x_np = np.array(x)
    y_np = np.array(y)
    for classifier in classifiers:
        indices = bootstrap(n)
        sampled_x = x_np[indices]
        sampled_y = y_np[indices]
        classifier.fit(sampled_x, sampled_y)

def predict(classifiers: list[DecisionTreeClassifier], x: list[list[float]]) -> list[int]:
    """
    Step 3: Assign class labels by a majority vote of the base classifiers.
    """
    x_np = np.array(x)
    y_lst = np.array([classifier.predict(x_np) for classifier in classifiers])
    predictions_per_sample = y_lst.T
    return [np.bincount(votes).argmax() for votes in predictions_per_sample]

def solution(x_train: list[list[float]], y_train: list[int], x_test: list[list[float]], n_estimators: int) -> list[int]:
    """
    Step 4: Pull everything together
    """
    seed(42)
    np.random.seed(42)
    classifiers = [DecisionTreeClassifier(
        random_state=0) for _ in range(n_estimators)]
    fit(classifiers, x_train, y_train)
    return predict(classifiers, x_test)

# Generate a simple test here
if __name__ == '__main__':
    x_train = [[0, 2], [0, 3], [0, 3], [1, 4], [1, 4], [1, 5]]
    y_train = [0, 0, 0, 1, 1, 1]
    x_test = [[0, 2], [1, 5]]
    n_estimators = 20  # Increased for stability
    predictions = solution(x_train, y_train, x_test, n_estimators)
    print(f"Predictions: {predictions}") # Expected: [0, 1]
    

