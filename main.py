#############Problem1##########
from fastapi import FastAPI

app = FastAPI()

# Updated product list with 7 items
products = [
    {"id": 1, "name": "Smartphone", "price": 999, "category": "Electronics", "in_stock": True},
    {"id": 2, "name": "Laptop", "price": 1999, "category": "Electronics", "in_stock": False},
    {"id": 3, "name": "Notebook", "price": 99, "category": "Stationery", "in_stock": True},
    {"id": 4, "name": "Pen Set", "price": 49, "category": "Stationery", "in_stock": True},
    {"id": 5, "name": "Laptop Stand", "price": 299, "category": "Electronics", "in_stock": True},
    {"id": 6, "name": "Mechanical Keyboard", "price": 2499, "category": "Electronics", "in_stock": True},
    {"id": 7, "name": "Webcam", "price": 499, "category": "Electronics", "in_stock": True},
]

@app.get("/products")
def get_products():
    return {
        "products": products,
        "total": len(products)
    }
#############problem 2#########
"""from fastapi import FastAPI

app = FastAPI()

# Sample product data with stock status and prices
products = [
    {"id": 1, "name": "Smartphone", "category": "Electronics", "in_stock": True, "price": 999},
    {"id": 2, "name": "Laptop", "category": "Electronics", "in_stock": False, "price": 1999},
    {"id": 3, "name": "Notebook", "category": "Stationery", "in_stock": True, "price": 99},
    {"id": 4, "name": "Pen Set", "category": "Stationery", "in_stock": True, "price": 49},
    {"id": 5, "name": "Headphones", "category": "Electronics", "in_stock": True, "price": 299},
    {"id": 6, "name": "Charger", "category": "Electronics", "in_stock": True, "price": 199},
    {"id": 7, "name": "Mechanical Keyboard", "category": "Electronics", "in_stock": True, "price": 2499},
]

@app.get("/products/category/{category_name}")
def get_by_category(category_name: str):
    result = [p for p in products if p["category"] == category_name]
    if not result:
        return {"error": "No products found in this category"}
    return {
        "category": category_name,
        "products": result,
        "total": len(result)
    }"""
########problem -3#############
"""from fastapi import FastAPI

app = FastAPI()

# Sample product data with stock status
products = [
    {"id": 1, "name": "Smartphone", "category": "Electronics", "in_stock": True},
    {"id": 2, "name": "Laptop", "category": "Electronics", "in_stock": False},
    {"id": 3, "name": "Notebook", "category": "Stationery", "in_stock": True},
    {"id": 4, "name": "Pen", "category": "Stationery", "in_stock": True},
    {"id": 5, "name": "Headphones", "category": "Electronics", "in_stock": True},
    {"id": 6, "name": "Charger", "category": "Electronics", "in_stock": True},
]

# Root endpoint (optional, acts like a homepage for your API)
@app.get("/")
def read_root():
    return {
        "message": "Welcome to the E-commerce API",
        "available_endpoints": [
            "/products/category/{category_name}",
            "/products/instock"
        ]
    }

# Endpoint: Get products by category
@app.get("/products/category/{category_name}")
def get_by_category(category_name: str):
    result = [p for p in products if p["category"] == category_name]
    if not result:
        return {"error": "No products found in this category"}
    return {
        "category": category_name,
        "products": result,
        "total": len(result)
    }

# Endpoint: Get only in-stock products
@app.get("/products/instock")
def get_instock():
    available = [p for p in products if p["in_stock"] is True]
    return {
        "in_stock_products": available,
        "count": len(available)
    }"""
############problem 4##########
"""from fastapi import FastAPI

app = FastAPI()

# Sample product data with stock status
products = [
    {"id": 1, "name": "Smartphone", "category": "Electronics", "in_stock": True},
    {"id": 2, "name": "Laptop", "category": "Electronics", "in_stock": False},
    {"id": 3, "name": "Notebook", "category": "Stationery", "in_stock": True},
    {"id": 4, "name": "Pen", "category": "Stationery", "in_stock": True},
    {"id": 5, "name": "Headphones", "category": "Electronics", "in_stock": True},
    {"id": 6, "name": "Charger", "category": "Electronics", "in_stock": True},
    {"id": 7, "name": "Marker", "category": "Stationery", "in_stock": False},
]

@app.get("/products/category/{category_name}")
def get_by_category(category_name: str):
    result = [p for p in products if p["category"] == category_name]
    if not result:
        return {"error": "No products found in this category"}
    return {
        "category": category_name,
        "products": result,
        "total": len(result)
    }

@app.get("/products/instock")
def get_instock():
    available = [p for p in products if p["in_stock"] is True]
    return {
        "in_stock_products": available,
        "count": len(available)
    }

@app.get("/store/summary")
def store_summary():
    in_stock_count = len([p for p in products if p["in_stock"]])
    out_stock_count = len(products) - in_stock_count
    categories = list(set([p["category"] for p in products]))
    return {
        "store_name": "My E-commerce Store",
        "total_products": len(products),
        "in_stock": in_stock_count,
        "out_of_stock": out_stock_count,
        "categories": categories,
    }"""
##########Problem 5 ##########
"""
from fastapi import FastAPI

app = FastAPI()

# Sample product data with stock status
products = [
    {"id": 1, "name": "Smartphone", "category": "Electronics", "in_stock": True},
    {"id": 2, "name": "Laptop", "category": "Electronics", "in_stock": False},
    {"id": 3, "name": "Notebook", "category": "Stationery", "in_stock": True},
    {"id": 4, "name": "Pen", "category": "Stationery", "in_stock": True},
    {"id": 5, "name": "Headphones", "category": "Electronics", "in_stock": True},
    {"id": 6, "name": "Charger", "category": "Electronics", "in_stock": True},
    {"id": 7, "name": "Wireless Mouse", "category": "Electronics", "in_stock": True},
]

@app.get("/products/category/{category_name}")
def get_by_category(category_name: str):
    result = [p for p in products if p["category"] == category_name]
    if not result:
        return {"error": "No products found in this category"}
    return {
        "category": category_name,
        "products": result,
        "total": len(result)
    }

@app.get("/products/instock")
def get_instock():
    available = [p for p in products if p["in_stock"] is True]
    return {
        "in_stock_products": available,
        "count": len(available)
    }

@app.get("/store/summary")
def store_summary():
    in_stock_count = len([p for p in products if p["in_stock"]])
    out_stock_count = len(products) - in_stock_count
    categories = list(set([p["category"] for p in products]))
    return {
        "store_name": "My E-commerce Store",
        "total_products": len(products),
        "in_stock": in_stock_count,
        "out_of_stock": out_stock_count,
        "categories": categories,
    }

@app.get("/products/search/{keyword}")
def search_products(keyword: str):
    results = [p for p in products if keyword.lower() in p["name"].lower()]
    if not results:
        return {"message": "No products matched your search"}
    return {
        "keyword": keyword,
        "results": results,
        "total_matches": len(results)
    }"""
##########BONUS###############
from fastapi import FastAPI

app = FastAPI()

# Sample product data with stock status and prices
products = [
    {"id": 1, "name": "Smartphone", "category": "Electronics", "in_stock": True, "price": 999},
    {"id": 2, "name": "Laptop", "category": "Electronics", "in_stock": False, "price": 1999},
    {"id": 3, "name": "Notebook", "category": "Stationery", "in_stock": True, "price": 99},
    {"id": 4, "name": "Pen Set", "category": "Stationery", "in_stock": True, "price": 49},
    {"id": 5, "name": "Headphones", "category": "Electronics", "in_stock": True, "price": 299},
    {"id": 6, "name": "Charger", "category": "Electronics", "in_stock": True, "price": 199},
    {"id": 7, "name": "Mechanical Keyboard", "category": "Electronics", "in_stock": True, "price": 2499},
]

@app.get("/products/category/{category_name}")
def get_by_category(category_name: str):
    result = [p for p in products if p["category"] == category_name]
    if not result:
        return {"error": "No products found in this category"}
    return {
        "category": category_name,
        "products": result,
        "total": len(result)
    }

@app.get("/products/instock")
def get_instock():
    available = [p for p in products if p["in_stock"] is True]
    return {
        "in_stock_products": available,
        "count": len(available)
    }

@app.get("/store/summary")
def store_summary():
    in_stock_count = len([p for p in products if p["in_stock"]])
    out_stock_count = len(products) - in_stock_count
    categories = list(set([p["category"] for p in products]))
    return {
        "store_name": "My E-commerce Store",
        "total_products": len(products),
        "in_stock": in_stock_count,
        "out_of_stock": out_stock_count,
        "categories": categories,
    }

@app.get("/products/search/{keyword}")
def search_products(keyword: str):
    results = [p for p in products if keyword.lower() in p["name"].lower()]
    if not results:
        return {"message": "No products matched your search"}
    return {
        "keyword": keyword,
        "results": results,
        "total_matches": len(results)
    }

@app.get("/products/deals")
def get_deals():
    cheapest = min(products, key=lambda p: p["price"])
    expensive = max(products, key=lambda p: p["price"])
    return {
        "best_deal": cheapest,
        "premium_pick": expensive,
    }