import pandas as pd
from sklearn.datasets import load_breast_cancer
from sklearn.preprocessing import StandardScaler, MinMaxScaler

class Dataset:
    """
    This class handles loading and preprocessing the breast cancer dataset.
    """

    def __init__(self):
        """
        The constructor for Dataset class.

        Loads the breast cancer dataset, initializes the data attributes,
        and performs initial data cleaning.
        """
        # Load the dataset from sklearn
        data = load_breast_cancer()
        self.data, self.target = data.data, data.target
        self.feature_names = data.feature_names
        # Perform initial data cleaning
        self.__load_and_clean_data()

    def __load_and_clean_data(self):
        """
        Private method to clean the data.

        It creates a DataFrame, removes duplicates, and handles missing values.
        Then it updates the data and target attributes with cleaned data.
        """
        df = pd.DataFrame(self.data, columns=self.feature_names)
        df['target'] = self.target
        df.drop_duplicates(inplace=True)
        df.dropna(inplace=True)
        self.target = df['target'].values
        self.data = df.drop('target', axis=1).values

class DataScaler:
    """
    Utility class to scale data using StandardScaler or MinMaxScaler from sklearn.
    """

    def scale_data(self, X_train, X_test, scale_type='standard'):
        """
        Scales the training and test datasets.

        Parameters:
        - X_train: Training data to fit the scaler.
        - X_test: Test data to transform based on the scaler.
        - scale_type (str): Determines the type of scaling ('standard' or 'normalize').

        Returns:
        - X_train_scaled, X_test_scaled: scaled versions of the training and test data.
        """
        scaler = StandardScaler() if scale_type == 'standard' else MinMaxScaler()
        X_train_scaled = scaler.fit_transform(X_train)
        X_test_scaled = scaler.transform(X_test)

        return X_train_scaled, X_test_scaled
