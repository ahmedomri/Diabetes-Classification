import pandas as pd
from diabetes_classification.pipelines.data_engineering.nodes.replace_null_values import replace_null_values 

def test_replace_null_values () :
    data = pd.read_csv('data/01_raw/diab.csv')
    output = replace_null_values(data)
    assert output.isnull().values.any() == False

