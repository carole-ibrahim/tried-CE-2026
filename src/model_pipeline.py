## Imports
import pandas as pd
import numpy as np
from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import Pipeline
from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score, f1_score
import matplotlib.pyplot as plt
import seaborn as sns


def load_and_explore_data()->tuple[np.array, np.ndarray, list, list]:
    """Load the iris dataset and perform basic exploration.
    Returns:        
        tuple: Features, target, feature names, target names
    """
    iris = load_iris()
    
    # Create DataFrame for better handling
    df = pd.DataFrame(iris.data, columns=iris.feature_names)
    df['target'] = iris.target
    df['species'] = df['target'].map({0: iris.target_names[0], 
                                     1: iris.target_names[1], 
                                     2: iris.target_names[2]})
    return iris.data, iris.target, iris.feature_names, iris.target_names


def create_preprocessing_pipeline():
    """Create a simple preprocessing pipeline."""    
    # Simple preprocessing pipeline with scaling
    preprocessor = StandardScaler()
    
    return preprocessor


def create_model_pipeline(preprocessor):
    """Create the complete model pipeline."""    
    # Create pipeline combining preprocessing and model
    pipeline = Pipeline([
        ('scaler', preprocessor),
        ('rf', RandomForestClassifier(
            n_estimators=100,
            random_state=42,
            max_depth=None,
            min_samples_split=2,
            min_samples_leaf=1
        ))
    ], memory=None)
    
    return pipeline

def train_model(pipeline, X_train, y_train):
    """Train the model and evaluate its performance."""
    # Train the model
    pipeline.fit(X_train, y_train)
    return pipeline 


def evaluate_model(pipeline, X_test, y_test):
    """Evaluate the model and print performance metrics."""
    # Make predictions
    y_pred = pipeline.predict(X_test)
    
    # Evaluation metrics
    
    cm = confusion_matrix(y_test, y_pred)
    
    accuracy = accuracy_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred, average='weighted')
    recall = recall_score(y_test, y_pred, average='weighted')
    f1 = f1_score(y_test, y_pred, average='weighted')   
    
    return cm, accuracy, precision, recall, f1


def visualize_results( cm, target_names, feature_importance_df):
    """Create visualizations for model results."""
    print("\nCreating visualizations...")
    
    # Create subplots
    _, axes = plt.subplots(1, 2, figsize=(15, 5))
    
    # Confusion Matrix Heatmap
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', 
                xticklabels=target_names, yticklabels=target_names,
                ax=axes[0])
    axes[0].set_title('Confusion Matrix')
    axes[0].set_xlabel('Predicted')
    axes[0].set_ylabel('Actual')
    
    # Feature Importance Bar Plot
    sns.barplot(data=feature_importance_df, x='importance', y='feature', ax=axes[1])
    axes[1].set_title('Feature Importance')
    axes[1].set_xlabel('Importance')
    
    plt.tight_layout()
    plt.savefig('iris_random_forest_results.png', dpi=300, bbox_inches='tight')
    print("Visualization saved as 'iris_random_forest_results.png'")
    plt.show()
