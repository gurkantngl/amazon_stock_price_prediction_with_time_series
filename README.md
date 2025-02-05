# Stock Price Prediction API

## Projenin Amacı
Bu proje, Amazon'un hisse senedi fiyatlarını zaman serisi analizi kullanarak tahmin etmeyi amaçlamaktadır. Hedef, geçmiş hisse senedi verilerini kullanarak gelecekteki fiyatları tahmin edebilen bir model oluşturmaktır.

## Kullanılan Teknolojiler
- Python
- Jupyter Notebook
- FastAPI
- Docker
- NLP ve makine öğrenimi algoritmaları

## Gereksinimler
İlk olarak, gerekli kütüphaneleri yükleyin:
```sh
pip install -r requirements.txt
```

API'yi başlatmak için:
uvicorn main:app --reload

API'yi test etmek için:
```sh
curl -X POST "http://localhost:8000/forecast" -H "accept: application/json" -H "Content-Type: application/json" -d '{"days" : 7}'
```


Sonuçları İnceleme


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


Docker ile Çalıştırma:
```sh
docker build -t my-fastapi-app .
```

Run
```sh
docker run -p 8000:8000 my-fastapi-app
```
