# PERFUME STOCK

Perfume Stock is a Inventory app designed for businesses which handles inventory on day to day basis. 

The inspiration for this app came from a friend of mine who work for a Luxury French perfume company. She work as a Sales Manager and she encounters certain tasks which she does everyday, very reptetive. 

Perfume Stock App was born. 

Stock App has four main programs: Add Daily Sales, View Current Stock, View Warehouse Stock and Sell-Through Rate.

The app is connected to Google sheets via API. Google sheets include: Daily sales sheet, store stock sheet and Warehouse stock sheet.

This app is not just for sales people. It's very useful for stock staff and warehouse staff. They will have their own worksheets updated so it saves time by not having to update worksheets.

When user adds a sale, all worksheets gets updated in real-time.

## Features

* Welcome the User

    * Beginning of the App the user is asked to enter their name.
    * The app takes the user name input and gives them a personal welcome to the app.

* User App Options

    * User is given four options to choose from.
        
        * Add Daily Sales
        * View Current Stock
        * View Warehouse Stock
        * Sell-Through Rate

* User App Options (Number selection)

    * When user wants to select an option all they have to do is select the number before the option name.
    * This options was created so user does not have to keep writing the option name every time. This saves times and effort.
    * Less repetitive.
    * User friendly.

* User Selected Option

    * This feature let's user know which option was selected.

* Add Daily Sales

    * When user selects Add Daily Sales, the terminal displays message asking user to add sales units sold.

    * Each perfume will then be displayed letting user input sale unit data.

    * Once all the perfumes are added, the users get's display message in terminal letting them know the app is updating sales.

    * Once the updated is completed, the user will see message saying sales added successfully.

    * When user adds sales, all worksheets gets updated automatically.

    * Store Stock sheet will minus current stock from sales.

    * Warehouse Stock will minus from the current warehouse stock from sales.