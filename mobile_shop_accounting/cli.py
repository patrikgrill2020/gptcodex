import argparse
import json
from .store import Store, Product


def main():
    parser = argparse.ArgumentParser(description="Mobile shop accounting")
    sub = parser.add_subparsers(dest="cmd", required=True)

    add_p = sub.add_parser("add-product", help="Add a new product")
    add_p.add_argument("id")
    add_p.add_argument("name")
    add_p.add_argument("price", type=float)

    purchase_p = sub.add_parser("purchase", help="Increase product inventory")
    purchase_p.add_argument("id")
    purchase_p.add_argument("quantity", type=int)

    sale_p = sub.add_parser("sale", help="Record a sale")
    sale_p.add_argument("id")
    sale_p.add_argument("quantity", type=int)

    sub.add_parser("report", help="Show inventory and sales report")

    args = parser.parse_args()
    store = Store()

    if args.cmd == "add-product":
        product = Product(args.id, args.name, args.price)
        store.add_product(product)
        print("Product added")
    elif args.cmd == "purchase":
        store.purchase(args.id, args.quantity)
        print("Inventory updated")
    elif args.cmd == "sale":
        store.sale(args.id, args.quantity)
        print("Sale recorded")
    elif args.cmd == "report":
        rep = store.report()
        print(json.dumps(rep, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
