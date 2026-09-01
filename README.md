# Product Rating API

A lightweight Flask REST API that filters products from [DummyJSON](https://dummyjson.com/products) by category and minimum rating.

## Endpoints

| Method | Route | Description |
|--------|-------|-------------|
| GET | `/` | Welcome message |
| GET | `/test` | Health check |
| GET | `/<category_type>/<n>` | Products in `category_type` with rating ≥ `n` |

## Example

```
GET /smartphones/4.5
```
Returns all smartphones with a rating of 4.5 or higher.

## Local Development

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

## Deploy to Vercel

```bash
vercel
```
