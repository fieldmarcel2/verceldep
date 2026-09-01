
from flask import Flask, request
import requests

app = Flask(__name__)


# Home route
@app.get("/")
def get_home():
    return "Welcome to Product Rating API"


# Test route
@app.get("/test")
def test():
    return {
        "status": "success",
        "message": "API is working!"
    }


# Product API
URL = "https://dummyjson.com/products"


@app.get("/<category_type>/<n>")
def get_ratings(category_type, n):

    response = requests.get(URL)
    data = response.json()

    prod = []

    for i in data["products"]:
        if (
            i["category"] == category_type
            and float(i.get("rating", 0)) >= float(n)
        ):
            prod.append(i)

    return prod


if __name__ == "__main__":
    app.run(debug=True)
    