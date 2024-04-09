import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_breast_cancer
from sklearn.ensemble import RandomForestClassifier

def load_data():
    """
    Loads the breast cancer dataset and returns it as a pandas DataFrame,
    along with the target names.
    """
    data = load_breast_cancer()
    df = pd.DataFrame(data.data, columns=data.feature_names)
    df['target'] = data.target
    return df, data.target_names

def plot_class_distribution(df):
    """
    Plots the distribution of classes in the dataset.
    """
    sns.countplot(x='target', data=df)
    plt.title('Class Distribution')
    plt.show()

def plot_feature_distributions(df):
    """
    Plots the distribution for each feature in the dataset.
    """
    df.drop('target', axis=1).hist(bins=20, figsize=(20, 15))
    plt.tight_layout()
    plt.show()

def plot_correlation_matrix(df):
    """
    Plots the correlation matrix of the features in the dataset.
    """
    plt.figure(figsize=(20, 15))
    sns.heatmap(df.corr(), annot=True, fmt=".2f", cmap='coolwarm')
    plt.title('Feature Correlation Matrix')
    plt.show()

def plot_box_plots(df):
    """
    Plots box plots for each feature in the dataset split by target class.
    """
    df_melted = pd.melt(df, id_vars=["target"], var_name="features", value_name='value')
    plt.figure(figsize=(10, 6))
    sns.boxplot(x="features", y="value", hue="target", data=df_melted)
    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.show()

def plot_pair_plot(df, features):
    """
    Plots pair plots for the selected features in the dataset.
    """
    sns.pairplot(df, vars=features, hue="target")
    plt.show()

def feature_importance(df):
    """
    Determines the importance of each feature using a random forest classifier and plots the results.
    """
    X = df.drop('target', axis=1)
    y = df['target']
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X, y)
    importances = model.feature_importances_
    indices = np.argsort(importances)[::-1]
    plt.figure(figsize=(10, 6))
    plt.title('Feature Importances')
    plt.bar(range(X.shape[1]), importances[indices], align='center')
    plt.xticks(range(X.shape[1]), X.columns[indices], rotation=90)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    df, target_names = load_data()
    # Display basic stats about the data
    print(df.describe())
    print(f"Target classes: {target_names}")

    # Visualize the data
    plot_class_distribution(df)
    plot_feature_distributions(df)
    plot_correlation_matrix(df)
    plot_box_plots(df)

    # Select first 5 features for pair plot (5 for demonstration only, this can be modified for different analyses)
    features = df.columns[:5]
    plot_pair_plot(df, features)

    # Plot feature importance
    feature_importance(df)
