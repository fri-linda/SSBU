from imblearn.over_sampling import SMOTE
import numpy as np
import pandas as pd
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import StratifiedKFold, train_test_split
import logging

from machine_learning.data_handling import DataScaler
from machine_learning.model_wrappers import ModelOptimizer, ModelTrainer

# Set up logging to record model accuracies in a CSV file
logging.basicConfig(filename='../outputs/model_accuracies.csv', filemode='w',  level=logging.INFO, format='%(asctime)s, %(message)s')

class Experiment:
    """A class to handle the entire experiment of training and evaluating models."""

    def __init__(self, models, models_params, n_replications=100):
        """
        Initialize the Experiment with models, their parameters, and number of replications.

        Parameters:
        - models: dict, a dictionary of machine learning model instances.
        - models_params: dict, a dictionary of hyperparameters for the models.
        - n_replications: int, the number of training/evaluation cycles to perform.
        """
        self.models = models
        self.models_params = models_params
        self.n_replications = n_replications
        self.results = pd.DataFrame()

    def run(self, X, y):
        """Run the experiment over multiple replications."""
        self.replication_conf_matrices = {model_name: [] for model_name in self.models_params.keys()}

        for replication in range(self.n_replications):
            self.run_single_replication(replication, X, y)

        self.mean_conf_matrices = self.calculate_mean_conf_matrices()
        return self.results

    def run_single_replication(self, replication, X, y):
        """Run a single replication of training and evaluating the models."""
        print(f"Starting replication {replication + 1}/{self.n_replications}.")
        X_resampled, y_resampled = self.balance_dataset(X, y)
        datascaler = DataScaler()  # Instantiate the DataScaler class
        for model_name, model_params in self.models_params.items():
            self.train_and_evaluate_model(model_name, model_params, X_resampled, y_resampled, datascaler, replication)

    def balance_dataset(self, X, y):
        """Balance the dataset using SMOTE."""
        smote = SMOTE()
        return smote.fit_resample(X, y)

    def train_and_evaluate_model(self, model_name, model_params, X_resampled, y_resampled, datascaler, replication):
        """Train and evaluate a single model."""
        skf = StratifiedKFold(n_splits=5, shuffle=True, random_state=0)
        optimizer = ModelOptimizer(self.models[model_name], model_params)
        best_params = optimizer.grid_search(X_resampled, y_resampled, cv=skf)

        # Train the model with the best parameters
        trainer = ModelTrainer(self.models[model_name], best_params)

        # Split the resampled data into training and test sets
        X_train, X_test, y_train, y_test = train_test_split(X_resampled, y_resampled, test_size=0.4,)

        # Scale the data using the DataScaler class
        X_train, X_test = datascaler.scale_data(X_train, X_test)

        # Train and evaluate the model
        trainer.train(X_train, y_train)
        accuracy, f1, roc_auc, predictions = trainer.evaluate(X_test, y_test)

        self.store_results(model_name, replication, accuracy, f1, roc_auc, best_params)
        # Append the confusion matrix to the list for this model
        self.replication_conf_matrices[model_name].append(confusion_matrix(y_test, predictions))

    def store_results(self, model_name, replication, accuracy, f1, roc_auc, best_params):
        """Store the results of a single evaluation."""
        new_row = pd.DataFrame({
            'model': model_name,
            'replication': replication + 1,
            'accuracy': accuracy,
            'f1_score': f1,
            'roc_auc': roc_auc,
            'best_params': [best_params]
        })
        self.results = pd.concat([self.results, new_row], ignore_index=True)
        logging.info(
            f"{model_name}, Replication: {replication}, Accuracy: {accuracy:.4f}, F1: {f1:.4f}, "
            f"ROC AUC: {roc_auc:.4f},  Params: {best_params}")

    def calculate_mean_conf_matrices(self):
        """Calculate the mean confusion matrix for each model."""
        mean_conf_matrices = {model_name: np.mean(np.array(matrices), axis=0)
                              for model_name, matrices in self.replication_conf_matrices.items()}
        return mean_conf_matrices