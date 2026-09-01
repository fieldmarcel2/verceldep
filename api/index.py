from flask import Flask, Blueprint, request, jsonify
import requests

app = Flask(__name__)

# ==========================================
# 1. Users Blueprint (/api/users)
# ==========================================
users_bp = Blueprint("users", __name__, url_prefix="/api/users")


@users_bp.get("/test")
def users_test():
    return jsonify({
        "status": "success",
        "blueprint": "users",
        "message": "Users route is isolated and working!",
        "endpoint": "/api/users/test"
    })


@users_bp.get("/profile")
def users_profile():
    return jsonify({
        "status": "success",
        "blueprint": "users",
        "data": {
            "id": 101,
            "username": "demo_user",
            "role": "member",
            "status": "active"
        }
    })


# ==========================================
# 2. Products Blueprint (/api/products)
# ==========================================
products_bp = Blueprint("products", __name__, url_prefix="/api/products")
DUMMYJSON_URL = "https://dummyjson.com/products"


@products_bp.get("/test")
def products_test():
    return jsonify({
        "status": "success",
        "blueprint": "products",
        "message": "Products route is working!",
        "endpoint": "/api/products/test"
    })


@products_bp.get("/<category_type>/<n>")
def get_ratings(category_type, n):
    try:
        response = requests.get(DUMMYJSON_URL, timeout=10)
        data = response.json()

        prod = []
        for item in data.get("products", []):
            if (
                item.get("category") == category_type
                and float(item.get("rating", 0)) >= float(n)
            ):
                prod.append(item)

        return jsonify(prod)
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500


# ==========================================
# Register Blueprints on App
# ==========================================
app.register_blueprint(users_bp)
app.register_blueprint(products_bp)


# Root route
@app.get("/")
def get_home():
    return jsonify({
        "message": "Welcome to Product & User API (Flask Blueprints)",
        "routes": {
            "users_blueprint": [
                "/api/users/test",
                "/api/users/profile"
            ],
            "products_blueprint": [
                "/api/products/test",
                "/api/products/<category_type>/<n>"
            ]
        }
    })


if __name__ == "__main__":
    app.run(debug=True)