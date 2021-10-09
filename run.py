import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]
# APIs
CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('perfumes_stock')

# Daily Sales Worksheet
daily_sales = SHEET.worksheet('daily_sales')
sales_data = daily_sales.get_all_values()

# Store Stock Worksheet
store_stock = SHEET.worksheet('store_stock')
store_stock_data = store_stock.get_all_values()

# Warehouse Stock Worksheet
warehouse_stock = SHEET.worksheet('warehouse_stock')
warehouse_stock_data = warehouse_stock.get_all_values()

print(warehouse_stock_data)

# python3 run.py
