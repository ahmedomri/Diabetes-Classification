import pandas as pd
import logging
from sklearn.neighbors import KNeighborsClassifier

logger = logging.getLogger(__name__)


def k_neighbors_classifier(X_train: pd.DataFrame, X_test: pd.DataFrame, y_train: pd.DataFrame, y_test: pd.DataFrame):
    test_scores = []
    train_scores = []

    for i in range(1, 15):
        knn = KNeighborsClassifier(i)
        knn.fit(X_train, y_train.values.ravel())

        train_scores.append(knn.score(X_train, y_train.values.ravel()))
        test_scores.append(knn.score(X_test, y_test.values.ravel()))

    ## score that comes from testing on the datapoints that were split in the beginning to be used for testing solely
    max_test_score = max(test_scores)
    test_scores_ind = [i for i, v in enumerate(test_scores) if v == max_test_score]
    print('Max test score {} % and k = {}'.format(max_test_score * 100, list(map(lambda x: x + 1, test_scores_ind))))

    # Setup a knn classifier with k neighbors
    knn = KNeighborsClassifier(test_scores_ind[0] + 1)
    knn.fit(X_train, y_train.values.ravel())

    return knn
