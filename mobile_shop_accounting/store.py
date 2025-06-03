import json
from dataclasses import dataclass, asdict
from typing import Dict, List


@dataclass
class Product:
    id: str
    name: str
    price: float
    quantity: int = 0


class Store:
    def __init__(self, db_path: str = "store.json"):
        self.db_path = db_path
        self.products: Dict[str, Product] = {}
        self.sales: List[Dict] = []
        self._load()

    def _load(self):
        try:
            with open(self.db_path, "r", encoding="utf-8") as f:
                data = json.load(f)
                for p in data.get("products", []):
                    self.products[p["id"]] = Product(**p)
                self.sales = data.get("sales", [])
        except FileNotFoundError:
            pass

    def _save(self):
        data = {
            "products": [asdict(p) for p in self.products.values()],
            "sales": self.sales,
        }
        with open(self.db_path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

    def add_product(self, product: Product):
        if product.id in self.products:
            raise ValueError("Product already exists")
        self.products[product.id] = product
        self._save()

    def purchase(self, product_id: str, quantity: int):
        product = self.products.get(product_id)
        if not product:
            raise ValueError("Product not found")
        product.quantity += quantity
        self._save()

    def sale(self, product_id: str, quantity: int):
        product = self.products.get(product_id)
        if not product:
            raise ValueError("Product not found")
        if product.quantity < quantity:
            raise ValueError("Not enough inventory")
        product.quantity -= quantity
        amount = quantity * product.price
        self.sales.append({"id": product_id, "quantity": quantity, "amount": amount})
        self._save()

    def report(self):
        total_sales = sum(s["amount"] for s in self.sales)
        return {
            "inventory": [asdict(p) for p in self.products.values()],
            "sales": self.sales,
            "total_sales": total_sales,
        }
