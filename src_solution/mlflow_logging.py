import mlflow

def setup_mlflow(experiment_name="Iris_Classification", mlflow_dir="mlflow"):
    """
    Set up MLflow experiment and tracking URI.

    Parameters:
    - experiment_name (str): Name of the MLflow experiment.
    - mlflow_dir (str): Directory to store MLflow tracking data.

    Returns:
    None
    """
    mlflow.set_tracking_uri(f"file://{mlflow_dir}")
    mlflow.set_experiment(experiment_name)
    print(f"MLflow experiment '{experiment_name}' is set up at '{mlflow_dir}'.")

def log_model_to_mlflow(model, model_name="iris_classifier"):
    """
    Log a trained model to MLflow.

    Parameters:
    - model: Trained machine learning model.
    - model_name (str): Name to register the model under in MLflow.

    Returns:
    None
    """
    mlflow.sklearn.log_model(
        sk_model=model,
        artifact_path="model",
        registered_model_name=model_name
    )
    print(f"Model '{model_name}' logged to MLflow.")
    mlflow.set_tag("model_family", "random_forest")
    mlflow.set_tag("dataset", "iris")
    