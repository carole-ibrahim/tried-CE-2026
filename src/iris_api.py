from fastapi import FastAPI, HTTPException
from contextlib import asynccontextmanager
from src.schemas import IrisInput, IrisPrediction
from src.ml_service import IrisModelService

# Global variable to hold the model service instance
ml_service = None


@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Lifespan context manager to handle startup and shutdown events.
    We load the model when the app starts.
    """
    global ml_service
    # Startup: Load the model
    ml_service = IrisModelService()
    yield
    # Shutdown: Clean up resources if needed
    ml_service = None


# Create the FastAPI application
app = FastAPI(
    title="Iris Classification API",
    description="A professional API to classify iris flowers using a Random Forest model.",
    version="1.0.0",
    lifespan=lifespan,
)


@app.get("/")
def read_root():
    """Health check endpoint."""
    return {"status": "online", "message": "Iris API is running"}


@app.post("/predict", response_model=IrisPrediction)
def predict_species(input_data: IrisInput):
    """
    Predict the species of an iris flower based on its measurements.
    """
    if ml_service is None:
        raise HTTPException(status_code=503, detail="Model service not initialized")

    try:
        # We use a synchronous definition (def) because scikit-learn predict is CPU-bound
        prediction = ml_service.predict(
            input_data.sepal_length,
            input_data.sepal_width,
            input_data.petal_length,
            input_data.petal_width,
        )
        return prediction
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Prediction error: {str(e)}")


if __name__ == "__main__":
    import uvicorn

    # Run the application
    uvicorn.run("src.iris_api:app", host="127.0.0.1", port=8000, reload=True)
