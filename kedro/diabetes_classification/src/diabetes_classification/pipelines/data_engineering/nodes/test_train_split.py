import pandas as pd
import logging
from sklearn.model_selection import train_test_split

logger = logging.getLogger(__name__)


def split_train_test(X: pd.DataFrame, Y: pd.DataFrame, test_size: float, random_state: float):
    X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size = test_size, random_state = random_state,
                                                        stratify = Y)
    return X_train, X_test, y_train, y_test
