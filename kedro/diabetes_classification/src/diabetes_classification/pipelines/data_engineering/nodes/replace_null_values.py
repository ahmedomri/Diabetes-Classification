import pandas as pd
import logging

logger = logging.getLogger(__name__)


def replace_null_values(diabetes_data: pd.DataFrame) -> pd.DataFrame:
    diabetes_data['Glucose'].fillna(diabetes_data['Glucose'].mean(), inplace=True)
    diabetes_data['BloodPressure'].fillna(diabetes_data['BloodPressure'].mean(), inplace=True)
    diabetes_data['SkinThickness'].fillna(diabetes_data['SkinThickness'].median(), inplace=True)
    diabetes_data['Insulin'].fillna(diabetes_data['Insulin'].median(), inplace=True)
    diabetes_data['BMI'].fillna(diabetes_data['BMI'].median(), inplace=True)
    return diabetes_data
