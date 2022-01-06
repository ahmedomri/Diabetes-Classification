import pandas as pd
import logging
from sklearn.preprocessing import StandardScaler

logger = logging.getLogger(__name__)


def scaling_data(diabetes_data_without_null: pd.DataFrame) -> pd.DataFrame:
    sc_X = StandardScaler()
    X = pd.DataFrame(sc_X.fit_transform(diabetes_data_without_null.drop(["Outcome"], axis=1), ),
                     columns=['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin',
                              'BMI', 'DiabetesPedigreeFunction', 'Age'])
    return X


def get_outcome(diabetes_data_without_null: pd.DataFrame) -> pd.DataFrame:
    return diabetes_data_without_null.Outcome
