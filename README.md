# Stock Price Prediction API

First, install the required libraries:

pip install -r requirements.txt



Run the API:

uvicorn main:app --reload


Test the API:

curl -X POST "http://localhost:8000/forecast" -H "accept: application/json" -H "Content-Type: application/json" -d

  '{"days" : 7}'



Review the Results:

{
    "forecast": [
        671.9352329335125,
        672.4893563311103,
        673.333475751795,
        675.1806842154775,
        675.589080411661,
        676.9868138519806,
        678.3802022698071
    ],
    "dates": [
        "2020-08-01",
        "2020-08-02",
        "2020-08-03",
        "2020-08-04",
        "2020-08-05",
        "2020-08-06",
        "2020-08-07"
    ]
}





# Run with Docker

Build:
docker build -t my-fastapi-app . 


Run:
docker run -p 8000:8000 my-fastapi-app
