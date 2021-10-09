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

# print(warehouse_stock_data)


def welcome_user():
    """
    Get users name and show welcome message
    """
    users_name = input("What is your name?\n")
    print(f"Hello {users_name}.\nWelcome to your Perfumes Stock App\n")


def user_app_options():
    """
    Give users 3 app options to select from to run the program
    """

    while True:
        view_current_stock = "View Current Stock".strip("")
        add_daily_sales = "Add Daily Sales".strip("")
        view_warehouse_stock = "View Warehouse Stock".strip("")

        print("What would you like to do today?...")
        print(f"{view_current_stock},{add_daily_sales},{view_warehouse_stock}")

        print("Tip: Copy & Paste your list selection to ensure no typos :)")
        user_selection = input("Pick a task from list above\n")
        print(f"You've chosen: {user_selection}\n")
        option_validation(user_selection)


def option_validation(user_selection):
    """
    Validate user has input to ensure users input is strings and not ints.
    Also, check user has only selected the options from the list given
    and throw error if user puts anything else.
    """

    try:
        if user_selection != "View Current Stock":
            raise ValueError(f"You selected {user_selection}")
        elif user_selection != "Add Daily Sales":
            raise ValueError(f"You selected {user_selection}")
        elif user_selection != "View Warehouse Stock":
            raise ValueError(f"You selected {user_selection}")
        else:
            return True
    except ValueError as e:
        print(f"Invalid option: {e}. Please try again...")
        return False


welcome_user()
user_app_options()


# python3 run.py
