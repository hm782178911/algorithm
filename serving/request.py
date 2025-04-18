import requests

data = {
    "UserID": 1,
    "MovieID": 100,
    "Genres": ["Action|Sci-Fi"]
}

response = requests.post("http://localhost:5000/predict", json=data)
print(response.json())  # 输出: {"probability": 0.87}