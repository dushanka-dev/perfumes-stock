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

# # Daily Sales Worksheet
# daily_sales = SHEET.worksheet('daily_sales')
# sales_data = daily_sales.get_all_values()

# # Warehouse Stock Worksheet
# warehouse_stock = SHEET.worksheet('warehouse_stock')
# warehouse_stock_data = warehouse_stock.get_all_values()

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
        current_stock = "View Current Stock\n".strip("")
        add_sales = "Add Daily Sales\n".strip("")
        warehouse_stock = "View Warehouse Stock\n".strip("")

        print("What would you like to do today?\n")
        print(f"{current_stock}{add_sales}{warehouse_stock}")

        print("Tip: Copy & Paste your list selection to ensure no typos :)")
        user_selection = input("Pick a task from list above ^^\n")
        print(f"You've chosen: {user_selection}\n")

        if user_selection == "Add Daily Sales":
            return add_daily_sales()
        if user_selection == "View Current Stock":
            return view_current_stock()

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
        if user_selection != "Add Daily Sales":
            raise ValueError(f"You selected {user_selection}")
        if user_selection != "View Warehouse Stock":
            raise ValueError(f"You selected {user_selection}")

    except ValueError as err:
        print(f"Invalid option: {err}. Please try again...")
        return False

    return True


def add_daily_sales():
    """
    User can add daily sale here.
    Once users add sales it will be added to the worksheet.

    """
    print("Please add ',' after each sale amount")

    user_sales = input("What is today's sales? ")
    new_sales = user_sales.split(",")
    our_new_list = list(new_sales)
    print(our_new_list)

    daily_sales_sheet = SHEET.worksheet("daily_sales")
    daily_sales_sheet.append_row(our_new_list)


def view_current_stock():
    """
    When user choose to View Current Stock,
    program will pull current stock data from worksheet.
    """

    store_stock = SHEET.worksheet("store_stock")
    current_stock_values = store_stock.row_values(6)
    print(current_stock_values)


# def update_sales_sheet(user_sales, sales_worksheet):
#     """Update daily worksheet"""

#     sales_worksheet = SHEET.worksheet("daily_sales")

#     sales_worksheet.append_row(user_sales)

welcome_user()
user_app_options()


# python3 run.py
# 1, 2, 3, 4, 5, 6, 7
