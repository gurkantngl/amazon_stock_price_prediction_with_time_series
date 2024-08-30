FROM tiangolo/uvicorn-gunicorn-fastapi:python3.11

WORKDIR /app

COPY main.py .
COPY arima_model.joblib .
COPY best_order.joblib .
COPY last_observation.joblib .
COPY requirements.txt .
COPY Amazon.csv .

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]