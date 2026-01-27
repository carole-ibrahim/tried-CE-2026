from pydantic import BaseModel, Field


class IrisInput(BaseModel):
    """
    Input schema for Iris flower measurements.
    """

    sepal_length: float = Field(..., gt=0, description="Sepal length in cm")
    sepal_width: float = Field(..., gt=0, description="Sepal width in cm")
    petal_length: float = Field(..., gt=0, description="Petal length in cm")
    petal_width: float = Field(..., gt=0, description="Petal width in cm")

    class Config:
        schema_extra = {
            "example": {
                "sepal_length": 5.1,
                "sepal_width": 3.5,
                "petal_length": 1.4,
                "petal_width": 0.2,
            }
        }


class IrisPrediction(BaseModel):
    """
    Output schema for Iris classification.
    """

    class_id: int = Field(..., description="predicted class id (0, 1, 2)")
    species: str = Field(
        ..., description="Predicted species name (setosa, versicolor, virginica)"
    )
