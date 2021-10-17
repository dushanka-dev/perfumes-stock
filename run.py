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
        add_sales = "1 - Add Daily Sales\n".strip("")
        current_stock = "2 - View Current Stock\n".strip("")
        warehouse_option = "3 - View Warehouse Stock\n".strip("")
        sell_rate = "4 - Sell-Through Rate\n".strip("")

        print("What would you like to do today?\n")
        print(f"{add_sales}{current_stock}{warehouse_option}{sell_rate}")

        print("Tip: Select number next to option. Eg. 1 to Add Daily Sales :)")
        user_selection = input("Pick a task from list above ^^\n")
        print(f"Selected Option: {user_selection}\n")

        sales_values = get_sales_values()
        store_stock_values = get_stock_values()

        if user_selection == "1":
            return add_daily_sales()
        if user_selection == "2":
            return view_current_stock()
        if user_selection == "3":
            return warehouse_stock()
        if user_selection == "4":
            return sell_through_rate(sales_values, store_stock_values)

        option_validation(user_selection)


def option_validation(user_selection):
    """
    Validate user has input to ensure users input is strings and not ints.
    Also, check user has only selected the options from the list given
    and throw error if user puts anything else.
    """

    try:
        if user_selection != "1":
            raise ValueError(f"You selected {user_selection}")
        if user_selection != "View Current Stock":
            raise ValueError(f"2 {user_selection}")
        if user_selection != "3":
            raise ValueError(f"You selected {user_selection}")
        if user_selection != "4":
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

    latest_store_stock = get_stock_values()
    updated_warehouse_stock = get_latest_warehouse_values()
    update_data(new_sales_list, latest_store_stock, updated_warehouse_stock)
    print("Sales Updated Successfully\n")

    user_app_options()


def view_current_stock():
    """
    When user choose to View Current Stock,
    program will pull current stock data from worksheet.
    """

    current_store_stock = get_stock_values()
    print(f'Latest Store Stock: {", ".join(current_store_stock)}\n')

    user_app_options()


def warehouse_stock():
    """
    This function calculates the latest stock in transit
    from warehouse and display to user.
    """

    warehouse_data = get_latest_warehouse_values()

    print(f'Latest Warehouse Stock: {", ".join(warehouse_data)}\n')

    user_app_options()


def get_sales_values():
    """Get latest sales values from worksheet."""

    latest_sales_data = SHEET.worksheet("daily_sales").get_all_values()
    return latest_sales_data[-1]


def get_stock_values():
    """
    Get latest Store stock values from worksheets.
    """

    store_stock = SHEET.worksheet("store_stock").get_all_values()
    return store_stock[-1]


def get_latest_warehouse_values():
    """
    Get latest Warehouse stock values from worksheets.
    """

    get_warehouse_stock = SHEET.worksheet("warehouse_stock").get_all_values()
    return get_warehouse_stock[-1]


def update_data(new_sales_list, store_stock, get_warehouse_stock):
    """Calculate latest Data after user adds new sales."""

    updated_store_data = []
    updated_warehouse_data = []
    index = 0
    for sales in new_sales_list:
        add_sales_store = int(store_stock[index]) - int(sales)
        add_sales_warehouse = int(get_warehouse_stock[index]) - int(sales)
        index = index + 1
        updated_store_data.append(add_sales_store)
        updated_warehouse_data.append(add_sales_warehouse)

    SHEET.worksheet("store_stock").append_row(updated_store_data)
    SHEET.worksheet("warehouse_stock").append_row(updated_warehouse_data)


def sell_through_rate(latest_sales_data, store_stock):
    """Calculate Sell through rate of stock"""

    sale_data_string = f'{"".join(latest_sales_data)}'
    stock_data_string = f'{"".join(store_stock)}'
    # sales_data_total = float(sale_data_string)
    # stock_data_total = float(stock_data_string)

    # sell_rate = int(sale_data_string) / int(stock_data_string)
    # latest_sell_rate = sum(sell_rate)

    print(f"Latest Sell Rate: {sale_data_string} {stock_data_string}%")


welcome_user()
user_app_options()

# python3 run.py
# 1, 2, 3, 4, 5, 6, 7
