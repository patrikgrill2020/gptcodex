# Mobile Shop Accounting

This repository contains a small command line application for managing the inventory and sales of a mobile phone shop. The tool is written in Python and stores data in a local JSON file.

## Features

- Add new products with ID, name, and price
- Record purchases to increase inventory
- Record sales to decrease inventory
- Show a simple report including current inventory and total sales

## Usage

```bash
# Add a product
python -m mobile_shop_accounting.cli add-product 001 "Phone Model" 1000.0

# Purchase inventory
python -m mobile_shop_accounting.cli purchase 001 5

# Record a sale
python -m mobile_shop_accounting.cli sale 001 2

# Show report
python -m mobile_shop_accounting.cli report
```

## به فارسی

این ابزار برای حسابداری ساده و مدیریت موجودی یک مغازه موبایل‌فروشی طراحی شده است. برنامه به صورت خط فرمان اجرا می‌شود و اطلاعات را در فایل `store.json` ذخیره می‌کند.

