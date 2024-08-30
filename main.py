from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib
import pandas as pd
import numpy as np
from statsmodels.tsa.arima.model import ARIMAResults
from datetime import datetime, timedelta

app = FastAPI()

model: ARIMAResults = joblib.load('arima_model.joblib')
last_observation = joblib.load('last_observation.joblib')
best_order = joblib.load('best_order.joblib')

original_data = pd.read_csv('Amazon.csv')
original_data['Date'] = pd.to_datetime(original_data['Date'])
last_date = original_data['Date'].max()

class ForecastRequest(BaseModel):
    days: int

class ForecastResponse(BaseModel):
    forecast: list
    dates: list

@app.post("/forecast", response_model=ForecastResponse)
async def get_forecast(request: ForecastRequest):
    try:
        forecast = model.forecast(steps=request.days)
        
        forecast_cumsum = forecast.cumsum()
        forecast_original_scale = last_observation * np.exp(forecast_cumsum)
        
        date_range = [last_date + timedelta(days=i+1) for i in range(request.days)]
        
        return ForecastResponse(
            forecast=forecast_original_scale.tolist(),
            dates=[date.strftime("%Y-%m-%d") for date in date_range]
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/model_info")
async def get_model_info():
    return {
        "model_type": "ARIMA",
        "order": best_order,
        "last_observation_date": last_date.strftime("%Y-%m-%d"),
        "last_observation_value": float(last_observation)
    }

if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="localhost", port=8000)