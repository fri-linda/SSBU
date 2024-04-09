from sklearn.metrics import accuracy_score, f1_score, roc_auc_score
from sklearn.model_selection import GridSearchCV


# Define a class for training and evaluating models
class ModelTrainer:
    """A class for training and evaluating machine learning models."""

    def __init__(self, model, parameters):
        """
        Initialize the ModelTrainer instance.

        Parameters:
        - model: scikit-learn model, the machine learning model to be trained.
        - parameters: dict, hyperparameters for the model.
        """
        self.model = model
        self.parameters = parameters

    def train(self, X_train, y_train):
        """
        Train the model on the training data.

        Parameters:
        - X_train: array-like, training features.
        - y_train: array-like, training labels.
        """
        self.model.set_params(**self.parameters)
        self.model.fit(X_train, y_train)

    def evaluate(self, X_test, y_test):
        """
        Evaluate the model on the test data.

        Parameters:
        - X_test: array-like, test features.
        - y_test: array-like, test labels.

        Returns:
        - accuracy: float, accuracy of the model on the test data.
        - f1: float, F1 score of the model on the test data.
        - roc_auc: float, ROC AUC of the model on the test data.
        - predictions: array, predicted labels for the test data.
        """
        predictions = self.model.predict(X_test)
        prob_predictions = self.model.predict_proba(X_test)[:, 1] if hasattr(self.model, "predict_proba") else [0] * len(
            y_test)
        accuracy = accuracy_score(y_test, predictions)
        f1 = f1_score(y_test, predictions)
        roc_auc = roc_auc_score(y_test, prob_predictions)
        return accuracy, f1, roc_auc, predictions


# Define a class for optimizing model hyperparameters
class ModelOptimizer:
    """A class for optimizing hyperparameters of machine learning models."""

    def __init__(self, model, param_grid):
        """
        Initialize the ModelOptimizer instance.

        Parameters:
        - model: scikit-learn model, the machine learning model for which hyperparameters are to be optimized.
        - param_grid: dict, the grid of hyperparameters to search over.
        """
        self.model = model
        self.param_grid = param_grid

    def grid_search(self, X_train, y_train, cv=5, scoring='accuracy'):
        """
        Perform grid search to find the best hyperparameters for the model.

        Parameters:
        - X_train: array-like, training features.
        - y_train: array-like, training labels.
        - cv: int, number of cross-validation folds.
        - scoring: str, scoring metric to optimize.

        Returns:
        - best_params: dict, the best hyperparameters found during grid search.
        """
        grid_search = GridSearchCV(self.model, self.param_grid, cv=cv, scoring=scoring, n_jobs=-1)
        grid_search.fit(X_train, y_train)
        return grid_search.best_params_