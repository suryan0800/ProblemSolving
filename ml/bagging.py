from random import randint, seed

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
    # implement this
    n = len(x) 
    for classifier in classifiers: 
        indices = bootstrap(n) 
        sampled_x = []
        sampled_y = [] 
        for i in indices: 
            sampled_x.append(x[i])
            sampled_y.append(y[i])
            
        classifier.fit(sampled_x, sampled_y)

def predict(classifiers: list[DecisionTreeClassifier], x: list[list[float]]) -> list[int]:
    """
    Step 3: Assign class labels by a majority vote of the base classifiers.
    """
    # implement this
    y_lst = []
    for classifier in classifiers: 
        y = classifier.predict(x)
        y_lst.append(y)
        
    n = len(x) 
    n_classifiers = len(classifiers)
    y_final = []
    for i in range(n): 
        hsh = {} 
        for j in range(n_classifiers): 
            y_val = y_lst[j][i]
            hsh[y_val] = hsh.get(y_val, 0) + 1
        
        maj_cnt = 0  
        maj_y = None
        for y_val in hsh: 
            if hsh[y_val] >= maj_cnt: 
                maj_cnt = hsh[y_val] 
                maj_y = y_val 
                
        for y_val in hsh: 
            if hsh[y_val] == maj_cnt: 
                if maj_y > y_val: 
                    maj_y = y_val 
        y_final.append(maj_y)
        
    return y_final 
            
        
        
        

def solution(x_train: list[list[float]], y_train: list[int], x_test: list[list[float]], n_estimators: int) -> list[int]:
    """
    Step 4: Pull everything together
    """
    seed(42)
    classifiers = [DecisionTreeClassifier(
        random_state=0) for _ in range(n_estimators)]
    fit(classifiers, x_train, y_train)
    return predict(classifiers, x_test)
