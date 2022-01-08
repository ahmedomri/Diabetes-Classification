from kedro.pipeline import Pipeline, node

from .nodes.KNeighbors_classifier import k_neighbors_classifier
from .nodes.predictions import predictions
from .nodes.classification_report import classification_report


def create_pipeline(**kwargs):
    return Pipeline(
        [
            node(
                func=k_neighbors_classifier,
                inputs=['X_train', 'X_test', 'y_train', 'y_test'],
                outputs= 'knn',
                name='k_neighbors_classifier'
            ),
            node(
                func=predictions,
                inputs=['knn', 'X_test'],
                outputs= 'Y_predict',
                name='predictions'
            ),
            node(
                func=classification_report,
                inputs=['y_test', 'Y_predict'],
                outputs= None,
                name='classification_report'
            ),
        ]
    )
