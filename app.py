from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib
import numpy as np

app = FastAPI(
    title="Credit Card Fraud Detection API",
    description="""An API that utilises a Machine Learning model that detects if a credit card transaction is fraudulent or not based on the following features: hours, amount, transaction type etc.""",
    version="1.0.0"
)

# Load the model once when the app starts
try:
    model = joblib.load('credit_fraud.pkl')
except Exception as e:
    print(f"Error loading model: {e}")
    model = None

class FraudDetection(BaseModel):
    step: int
    types: int
    amount: float
    oldbalanceorig: float
    newbalanceorig: float
    oldbalancedest: float
    newbalancedest: float
    isflaggedfraud: float

@app.post('/predict')
async def predict(data: FraudDetection):
    if model is None:
        raise HTTPException(status_code=500, detail="Model not loaded")
    
    try:
        features = np.array([[
            data.step,
            data.types,
            data.amount,
            data.oldbalanceorig,
            data.newbalanceorig,
            data.oldbalancedest,
            data.newbalancedest,
            data.isflaggedfraud
        ]])
        
        predictions = model.predict(features)
        
        # Return a proper JSON response
        return {
            "status": "success",
            "prediction": "fraudulent" if predictions[0] == 1 else "not fraudulent"
        }
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Prediction error: {str(e)}")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8501)