import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler, StandardScaler

from machine_learning.data_handling import Dataset


def visualize_feature_distributions(X_train, X_train_scaled, feature_names, scale_type='Standardization'):
    """
    Visualizes the distribution of features before and after scaling.

    Parameters:
    - X_train: array-like, original training data.
    - X_train_scaled: array-like, scaled training data according to the 'scale_type'.
    - feature_names: list of str, names of the features in the dataset.
    - scale_type: str, the type of scaling performed ('Standardization' or 'Normalization').
    """
    # Create a figure with two subplots side by side
    fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(16, 6))

    # Plot the original data on the first subplot
    sns.boxplot(data=X_train, ax=axes[0], orient='h')
    # Set feature names as y-tick labels
    axes[0].set_yticks(range(len(feature_names)))
    axes[0].set_yticklabels(feature_names)
    axes[0].set_title(f'Before {scale_type}')

    # Plot the scaled data on the second subplot
    sns.boxplot(data=X_train_scaled, ax=axes[1], orient='h')
    axes[1].set_yticks(range(len(feature_names)))
    axes[1].set_yticklabels(feature_names)
    axes[1].set_title(f'After {scale_type}')

    # Adjust layout for better spacing
    plt.tight_layout()
    plt.show()


def preprocess_data(data, test_size=0.4, stratify=True, scale_type='standard'):
    """
    Preprocesses the data by splitting into train and test sets and scaling.

    Parameters:
    - data: Dataset instance to be processed
    - test_size (float): The proportion of the dataset to include in the test split.
    - stratify (bool): Whether to stratify the split according to the class labels.
    - scale_type (str): Determines the type of scaling ('standard' or 'normalize').

    Returns:
    - X_train_scaled, X_test_scaled: scaled versions of the training and test data.
    - y_train, y_test: training and test labels.
    """
    stratify_param = data.target if stratify else None
    X_train, X_test, y_train, y_test = train_test_split(
        data.data, data.target, test_size=test_size, stratify=stratify_param, random_state=42)

    scaler = StandardScaler() if scale_type == 'standard' else MinMaxScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    return X_train, X_test, X_train_scaled, X_test_scaled


if __name__ == "__main__":
    # Initialize the dataset
    dataset = Dataset()
    feature_names = dataset.feature_names

    # Preprocess and standardize the data
    X_train, _, X_train_std, _ = preprocess_data(dataset,scale_type='standard')
    # Visualize the effect of standardization
    visualize_feature_distributions(X_train, X_train_std, feature_names, 'Standardization')

    # Preprocess and normalize the data
    _, _, X_train_norm, _ = preprocess_data(dataset, scale_type='normalize')
    # Visualize the effect of normalization
    visualize_feature_distributions(X_train, X_train_norm, feature_names, 'Normalization')
