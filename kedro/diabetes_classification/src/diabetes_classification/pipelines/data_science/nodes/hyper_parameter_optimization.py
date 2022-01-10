from sklearn.model_selection import GridSearchCV
from sklearn.neighbors import KNeighborsClassifier
import numpy as np


def params_optimization(X, Y, cv: int):
    param_grid = {'n_neighbors': np.arange(1, 50)}
    knn = KNeighborsClassifier()
    knn_cv = GridSearchCV(knn, param_grid, cv=5)
    knn_cv.fit(X, Y.values.ravel())
    print("Best Score:" + str(knn_cv.best_score_))
    print("Best model: " + str(knn_cv.best_estimator_))
    return None
