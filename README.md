# Modular Flask API with Blueprints

A Flask REST API built with **Flask Blueprints** for modular route segregation, privacy, and security. Deployed on [Vercel](https://vercel.com).

## 🚀 Architecture & Blueprints

The application is structured into isolated Blueprints with URL prefixes:

### 👤 Users Blueprint (`/api/users`)
| Method | Route | Description |
|--------|-------|-------------|
| GET | `/api/users/test` | Test endpoint for the users blueprint |
| GET | `/api/users/profile` | Get user profile data |

### 📦 Products Blueprint (`/api/products`)
| Method | Route | Description |
|--------|-------|-------------|
| GET | `/api/products/test` | Test endpoint for the products blueprint |
| GET | `/api/products/<category_type>/<n>` | Products in `category_type` with rating ≥ `n` |

### 🌐 Root
| Method | Route | Description |
|--------|-------|-------------|
| GET | `/` | API overview & registered blueprint routes |

## 💻 Local Development

```bash
# Create and activate virtual environment
python -m venv venv
venv\Scripts\activate        # Windows
# source venv/bin/activate   # macOS/Linux

# Install dependencies
pip install -r requirements.txt

# Run the dev server
python api/index.py
```

## 🚀 Deploy to Vercel

```bash
npx vercel
```
Or link this repository directly on [vercel.com/new](https://vercel.com/new).
