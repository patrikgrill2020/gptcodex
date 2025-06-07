# -*- coding: utf-8 -*-
import csv
import datetime
import os

CSV_FILE = 'inventory.csv'
HEADERS = ['date', 'action', 'item', 'quantity', 'project']

# Create file with headers if it doesn't exist
if not os.path.exists(CSV_FILE):
    with open(CSV_FILE, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(HEADERS)

def _append_row(row):
    with open(CSV_FILE, 'a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(row)

def add_item():
    item = input('نام کالا را وارد کنید: ')
    quantity = input('مقدار را وارد کنید: ')
    if not quantity.isdigit():
        print('مقدار نامعتبر است.')
        return
    date = datetime.date.today().isoformat()
    _append_row([date, 'add', item, quantity, ''])
    print('کالا به انبار اضافه شد.')

def _current_inventory():
    inventory = {}
    if not os.path.exists(CSV_FILE):
        return inventory
    with open(CSV_FILE, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            qty = int(row['quantity'])
            key = row['item']
            if row['action'] == 'add':
                inventory[key] = inventory.get(key, 0) + qty
            elif row['action'] == 'assign':
                inventory[key] = inventory.get(key, 0) - qty
    return inventory

def assign_item():
    item = input('نام کالا را وارد کنید: ')
    quantity = input('مقدار را وارد کنید: ')
    if not quantity.isdigit():
        print('مقدار نامعتبر است.')
        return
    project = input('نام پروژه را وارد کنید: ')
    inventory = _current_inventory()
    if inventory.get(item, 0) < int(quantity):
        print('موجودی کافی نیست.')
        return
    date = datetime.date.today().isoformat()
    _append_row([date, 'assign', item, quantity, project])
    print('کالا به پروژه اختصاص داده شد.')

def report_by_date():
    date = input('تاریخ مورد نظر (YYYY-MM-DD) را وارد کنید: ')
    if not os.path.exists(CSV_FILE):
        print('هیچ داده‌ای موجود نیست.')
        return
    with open(CSV_FILE, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        print(f'گزارش برای تاریخ {date}:')
        for row in reader:
            if row['date'] == date:
                if row['action'] == 'add':
                    print(f"{row['item']} - ورود به انبار - مقدار {row['quantity']}")
                else:
                    print(f"{row['item']} - اختصاص به پروژه {row['project']} - مقدار {row['quantity']}")

def main_menu():
    while True:
        print('\nمنوی اصلی:')
        print('1. اضافه کردن کالا به انبار')
        print('2. اختصاص کالا به پروژه')
        print('3. گزارش بر اساس تاریخ')
        print('4. خروج')
        choice = input('انتخاب کنید: ')
        if choice == '1':
            add_item()
        elif choice == '2':
            assign_item()
        elif choice == '3':
            report_by_date()
        elif choice == '4':
            break
        else:
            print('انتخاب نامعتبر است.')

if __name__ == '__main__':
    main_menu()
