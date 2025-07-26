import random


def random_bias_theta(n_features: int) -> tuple[float, list[float]]:
    """
    STEP 1: Randomly set bias and theta
    """
    b = random.random()
    theta = [random.random() for _ in range(n_features)]
    return b, theta


def calculate_y(b: float, theta: list[float], x: list[float]) -> float:
    """
    STEP 2: Calculate predicted value of Y
    """
    # implement this
    sm = 0 
    # print("b:", b, "theta:", theta, "x:", x)
    for t1, x1 in zip(theta, x): 
        sm += (t1 * x1)
        
    return b + sm


def calculate_d_b(Y: list[float], Y_hat: list[float]) -> float:
    """
    STEP 3: Calculate bias derivative
    """
    # implement this
    n = len(Y)
    sm = 0 
    for y, y_hat in zip(Y, Y_hat): 
        sm += (y - y_hat) 
    return ((-2)/n) * sm 


def calculate_d_theta(X: list[list[float]], Y: list[float], Y_hat: list[float]) -> list[float]:
    """
    STEP 4: Calculate theta derivative
    """
    # implement this
    n = len(Y)
    n_features = len(X[0])
    d_theta = [0] * n_features
    for i in range(n_features):
        sm = 0 
        for x, y, y_hat in zip(X, Y, Y_hat): 
            sm += x[i] * (y - y_hat) 
        d_theta[i] = ((-2)/n) * sm
    return d_theta


def update(X: list[list[float]], Y: list[float], Y_hat: list[float], b_prev: float, theta_prev: list[float], learning_rate: float) -> tuple[float, list[float]]:
    """
    STEP 5: Update gradient and weights
    """

    d_theta = calculate_d_theta(X, Y, Y_hat)
    d_b = calculate_d_b(Y, Y_hat)
    # print(f"Gradient: d_b = {d_b}, d_theta = {d_theta}")
    # implement this
    b_new = b_prev - learning_rate * d_b 
    theta_new = [t1 - learning_rate * dt1  for t1, dt1 in zip(theta_prev, d_theta)]
    return b_new, theta_new


def fit(X: list[list[float]], Y: list[float], num_iterations: int, learning_rate: float = 0.02) -> tuple[float, list[float]]:
    """
    STEP 6: Pulling it together
    """
    b, theta = random_bias_theta(len(X[0]))
    for _ in range(num_iterations):
        # implement this
        Y_hat = [calculate_y(b, theta, x) for x in X]
        # print(f"Iteration {_ + 1}: Y_hat = {Y_hat}")
        b, theta = update(X, Y, Y_hat, b, theta, learning_rate)
    print(f"Iteration {_ + 1}: b = {b}, theta = {theta}")
    return b, theta


def solution(x_train: list[list[float]], y_train: list[float], x_test: list[list[float]], iterations: int = 1000) -> list[float]:
    random.seed(42)
    b, theta = fit(x_train, y_train, iterations)
    return [round(calculate_y(b, theta, x), 2) for x in x_test]



solution(x_train=[[1, 2], [2, 3], [3, 4]], y_train=[1, 2, 3], x_test=[[1, 2], [2, 3], [3, 4]], iterations=1000)
