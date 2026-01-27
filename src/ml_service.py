import numpy as np
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier


class IrisModelService:
    def __init__(self):
        self.model = None
        self.class_names = []
        self._load_or_train_model()

    def _load_or_train_model(self):
        """
        In a real production environment, this would load a serialized model (e.g. from a .pkl file).
        For this demo, we train the model on-the-fly.
        """
        print("Loading Iris dataset and training model...")
        iris = load_iris()
        self.class_names = iris.target_names

        # Train a simple Random Forest
        self.model = RandomForestClassifier(n_estimators=10, random_state=42)
        self.model.fit(iris.data, iris.target)
        print("Model trained and ready.")

    def predict(
        self,
        sepal_length: float,
        sepal_width: float,
        petal_length: float,
        petal_width: float,
    ):
        """
        Predict the species of an iris flower.

        Args:
            sepal_length: Length of sepal
            sepal_width: Width of sepal
            petal_length: Length of petal
            petal_width: Width of petal

        Returns:
            dict: Contains 'class_id' and 'species'
        """
        if self.model is None:
            raise RuntimeError("Model is not loaded")

        # Prepare input for scikit-learn (2D array)
        features = np.array([[sepal_length, sepal_width, petal_length, petal_width]])

        # Predict
        prediction_idx = self.model.predict(features)[0]
        species_name = self.class_names[prediction_idx]

        return {"class_id": int(prediction_idx), "species": species_name}
