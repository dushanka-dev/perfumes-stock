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
        warehouse_option = "View Warehouse Stock\n".strip("")
        transit_stock = "Stock in Transit\n".strip("")

        print("What would you like to do today?\n")
        print(f"{current_stock}{add_sales}{warehouse_option}{transit_stock}")

        print("Tip: Copy & Paste your list selection to ensure no typos :)")
        user_selection = input("Pick a task from list above ^^\n")
        print(f"Selected Option: {user_selection}\n")

        if user_selection == "Add Daily Sales":
            return add_daily_sales()
        if user_selection == "View Current Stock":
            return view_current_stock()
        if user_selection == "View Warehouse Stock":
            return warehouse_stock()
        # if user_selection == "Stock in Transit":
        #     return warehouse_stock()

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
        # if user_selection != "Stock in Transit":
        #     raise ValueError(f"You selected {user_selection}")

    except ValueError as err:
        print(f"Invalid option: {err}. Please try again...")
        return False

    return True


def add_daily_sales():
    """
    User can add daily sale here.
    Once users add sales it will be added to the worksheet.

    """

    daily_sales_sheet = SHEET.worksheet("daily_sales")
    perfume_names = daily_sales_sheet.row_values(1)
    # name_values = "\n".join(perfume_names)
    print("What is today's sales?")

    new_sales_list = []
    for name in perfume_names:
        new_sales = input(f"{name}: ")
        new_sales_list.append(new_sales)

    daily_sales_sheet.append_row(new_sales_list)

    print("Updating Sales...")
    print("Sales Updated Successfully\n")

    user_app_options()

    # return new_sales_list


def view_current_stock():
    """
    When user choose to View Current Stock,
    program will pull current stock data from worksheet.
    """

    store_stock = SHEET.worksheet("store_stock").get_all_values()
    latest_stock = store_stock[-1]
    print(f'Latest Store Stock: {", ".join(latest_stock)}\n')

    user_app_options()


def warehouse_stock():
    """
    This function calculates the latest stock in transit
    from warehouse and display to user.
    """

    warehouse_stock_data = SHEET.worksheet("warehouse_stock").get_all_values()
    latest_warehouse_stock = warehouse_stock_data[-1]

    print(f'Latest Warehouse Stock: {", ".join(latest_warehouse_stock)}\n')

    user_app_options()


# def update_data(new_sales_list, latest_stock):
#     """Calculate latest Data after user adds new sales."""

#     updated_store_data = []
#     for sales in new_sales_list:
#         add_sales_store = latest_stock - int(sales)
#         updated_store_data.append(add_sales_store)

#     latest_stock.append_row(updated_store_data)


# def stock_in_transit(latest_warehouse_stock):
#     """
#     When user adds new sales,
#     all sheets gets updated.
#     """
#     total_stock = []

#     for stock in latest_warehouse_stock:
#         add_stock = range(stock)
#         total_stock.append(add_stock)

#     print(f"Total Transit Stock: {total_stock}")


welcome_user()
user_app_options()

# python3 run.py
# 1, 2, 3, 4, 5, 6, 7
