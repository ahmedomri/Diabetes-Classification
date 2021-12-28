from kedro.pipeline import Pipeline, node
from .nodes.replace_null_values import replace_null_values


def create_pipeline(**kwargs):
    return Pipeline(
        [
            node(
                func=replace_null_values,
                inputs=['diabetes_data'],
                outputs='diabetes_data_without_null',
                name='replace_null_values_node'
            ),
        ]
    )
