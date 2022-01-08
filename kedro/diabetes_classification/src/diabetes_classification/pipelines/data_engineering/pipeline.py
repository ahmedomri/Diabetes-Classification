from kedro.pipeline import Pipeline, node
from .nodes.replace_null_values import replace_null_values
from .nodes.scaling_data import get_outcome, scaling_data
from .nodes.test_train_split import split_train_test

def create_pipeline(**kwargs):
    return Pipeline(
        [
            node(
                func=replace_null_values,
                inputs=['diabetes_data'],
                outputs='diabetes_data_without_null',
                name='replace_null_values_node'
            ),
            node(
                func=get_outcome,
                inputs=['diabetes_data_without_null'],
                outputs='Y',
                name='get_outcome_node'
            ),
            node(
                func=scaling_data,
                inputs=['diabetes_data_without_null'],
                outputs='X',
                name='scaling_data_node'
            ),
            node(
                func=split_train_test,
                inputs=['X', 'Y', "params:test_size", "params:random_state"],
                outputs=['X_train', 'X_test', 'y_train', 'y_test'],
                name='split_train_test_node'
            ),
        ]
    )
