# WarehouseInventoryManager
A simplified warehouse management system python terminal application.
Used to keep track of the products in storage at a warehouse, and product location in racking/shelving.

## Features
- Display product in stock (by product) listing locations, along with product count
- Add product to stock
- Move a product / change location
- Remove product from stock
- Save stock in external file
- Export product report

View Project Management on Trello for more details on feature development.

## Project Management:
[Trello - Warehouse Inventory Manager](https://trello.com/b/zAEdR9ws/warehouseinventorymanager)

## HELP / Instructions:
### Installation:
Run the following command in terminal from 'src' folder:
./shell.sh
Any necessary packages will be installed in a virtual environment and the program will run.
### Dependencies:
A terminal to run the bash shell script. Python and pip will be installed in a virtual environment.
Currently no other dependencies.
### System / Hardware Requirements:
- Terminal with bash
- Computer that can run Python and pip installer
### Command Line Arguments:
No Command Line Arguments are required/ available.

### Instructions:
#### Products:
Products are the different types of stock that can be stored in the warehouse (e.g. MacBook Pro, Bose Stereo, etc.)
Products require an identification number and a name.
Press 1 from the main menu to view the Products menu. From here you can view products already entered, add a product, and edit or remove a product.
Note: Product cannot be removed if a stock item of this product exists.

#### Stock Items:
Stock items are individual objects stored in a warehouse.
Stock items require an identification number, product number, and location in the warehouse.
Location is in format of Room, Row, Height
Press 2 from the main menu to view the Stock menu. From here you can view stock already added, add stock, move stock location, or remove stock.

#### Save & Load:
Products and Stock Items are saved when exiting the program, and loaded when running the program again.

#### Export Report:
From the View Products / View Stock screens, reports can be exported by pressing 'p'. The report can then be opened in your text editor of choice and printed if needed.

#### 
## GitHub Repo:
[github.com/lzhalloran/WarehouseInventoryManager](https://github.com/lzhalloran/WarehouseInventoryManager)

## Style guide / conventions:
[PEP 8 - Style Guide for Python Code](https://peps.python.org/pep-0008/)