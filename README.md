# PERFUME STOCK APP

Perfume Stock is a Inventory app designed for businesses which handles inventory on day to day basis. 

The inspiration for this app came from a friend of mine who work for a Luxury French perfume company. She's a Sales Manager. Every day she performs same reptetive tasks. 

Perfume Stock App was born. 

Perfume Stock App has four main features: Add Sales Units, View Current Stock, View Warehouse Stock and Sell-Through Rate.

The app is connected to Google sheets via API. Google worksheets include: Daily sales, Store stock and Warehouse stock.

This app is not just for sales people. It's very useful for stock staff and warehouse staff. They will have their own worksheets updated so it saves time by not having to update worksheets manually.

When user adds a sale unit, all worksheets gets updated in real-time.

# Features

* Welcome the User

* Beginning of the App the user is asked to enter their name.
* The app takes the user name input and gives them a personal welcome to the app.
    <br/>
    <br/>
    ![Users Name](readme-files/screenshots/welcome-user.png)

* User App Options

* User is given four options to choose from.
        
    * Add Daily Sales
    * View Current Stock
    * View Warehouse Stock
    * Sell-Through Rate
        <br/>
        <br/>
* User App Options (Number selection)

* When user wants to select an option all they have to do is select the number before the option name.
* This options was created so user does not have to keep typing the option name every time. This saves time and effort.
* Less repetitive.
* User friendly
    <br/>
    <br/>
    ![App Options](readme-files/screenshots/app-options.png)

* User Selected Option

* This feature let's user know which option was selected.

* Add Daily Sales

* When user selects Add Daily Sales, the terminal displays message asking user to add sales units sold.

* Each perfume will then be displayed letting user input sale unit data.

* Once all the perfumes are added, the users get's display message in terminal letting them know the app is updating sales units.

* Once the update is completed, the user will see message saying sales added successfully.

* When user adds sales, all worksheets gets updated automatically.

* Store Stock sheet will minus current stock from sales.

* Warehouse Stock will minus from the current warehouse stock from sales.
    <br/>
    <br/>
    ![sales-units](readme-files/screenshots/add-sales-units.png)

* View Current Stock

    * User get to see the latest stock in store.
    * This is updated live so if user adds a sales, this worksheet is updated so user always see the latest store stock.
    <br/>
    <br/>
    ![store-stocks](readme-files/screenshots/latest-store-stock.png)
    
    * View Warehouse Stock

* User can see the latest warehouse stock for the day.
* Warehouse stock is updated automatically when user adds a sale. 
* Warehouse staff save time by not having to minus stock in worksheets manually.
    <br/>
    <br/>
    ![warehouse-stocks](readme-files/screenshots/latest-warehouse-stock.png)
* Sell_Through Rate

* Sell-through rate is used by businesses all around the world. It helps with identifying what products are selling and what is not selling that well. It helps business make forwarding decisions in stock to purchase in future. 

* The calculation: sales units / current stock * 100

* This feature uses live data, so if user adds new sales units, the result for this feature will update automatically.
    <br/>
    <br/>
    ![sell-through-rate](readme-files/screenshots/sell-through-rate.png)
    <br/>
    <br/>

* Worksheets Updated Real_time
    ![daily_sales_worksheet](readme-files/screenshots/daily-sales-worksheet.png)
    <br/>
    <br/>
    ![store-stock-worksheet](readme-files/screenshots/store-stock-worksheet.png)
    <br/>
    <br/>
    ![warehouse-stock-worksheet](readme-files/screenshots/warehouse-stock-worksheet.png)

* Error Handling

    * The app will check if user has entered the correct option using a number displayed in the options menu.

    * If error has occured, the user will be displayed what they typed and alert will display example to encourage user to try again.
    <br/>
    <br/>
    ![error-handling](readme-files/screenshots/error-handling.png)

# Deployment

* Visit [Heroku](https://www.heroku.com/)
* Sign Up/Login
* Select Create App
* Name App and select region
* Press Create App
* Go to Settings page
* Add config Vars
* Add Buildpacks Python and Node.js
* Go to Deploy section
* Connect to Github Repo
* Select deploy branch

# Testing

* [PEPE8 Online Testing](http://pep8online.com/):
   W292	210	19	no newline at end of file - I did add new line at line 211 of the file, however, when push the code to github it removes the newline.
   If you copy and paste the actual code from gitpod you will not see any warnings.

* No terminal errors

* Add Daily Sales Testing

    * Added sales units in terminal and checked Daily_Sales worksheet to ensure each sale unit is been added correctly.

    * Checked store_stock and warehouse_stock worksheets to ensure the stock getting calculated in real-time when user adds a sale unit.

* View Current Stock

    * Checked with the worksheet to make sure the result shown to user matches the worksheet.

    * Checked worksheet after adding new sale unit to ensure the worksheet results are the latest stock.

* View Warehouse Stock

    * After user adds sales, checked the warehouse worksheet to ensure it is updated with correct data.

    * Check results with worksheet to make sure user gets the latest result from worksheet.

* Sell-Through Rate

    * Added new sales units to worksheets and then ran the Sell-Through Rate feature to check if the calculation is correct based on latest sales units and store stock.

    * Checked the results by adding different sales units and stock to make sure the results are updated accordingly.

* You may need to refresh Google sheets page to see live data.

## Credits

* [Gitpod](https://www.gitpod.io/)
* [GitHub](https://github.com/)
* [Heroku](https://www.heroku.com/)
* [Google](https://www.google.com/)
* [Google Sheets](https://www.google.co.uk/sheets/about/)
* [Google Cloud Platform](https://cloud.google.com/)
* [gspread](https://docs.gspread.org/en/latest/)
* [Stack Overflow](https://stackoverflow.com/)
* [PEP8 Online](http://pep8online.com/)
* [Lucidchart](https://www.lucidchart.com/pages/)
* [Spell Checker](https://www.internetmarketingninjas.com/online-spell-checker.php)
* [Corporate Finance Institute](https://corporatefinanceinstitute.com/resources/knowledge/ecommerce-saas/sell-through-rate/) (Sell-Through Rate Calculation)
# Notes
![diagram](readme-files/diagram/Perfume-Stock-lucidchart.png)