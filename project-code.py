print("Welcome to Code n Coffee, How can we help you")

options = ["1 .Collection", "2. Delivery", "3. Employees"]
menu = ["Menu" , "Books"]
employee_menu = ["Add/remove drinks", "Add/remove Foods", "Add/remove books"]
menu_items = {'Drinks' : ["Ice Coffee", "Coffee", "Juice", "Water", "Hot Chocolate"], 'Food' :  ["Muffins", "Croissant", "Sandwiches", "Biscuits", "Fruits"]}
#drinks = ["Ice Coffee", "Coffee", "Juice", "Water", "Hot Chocolate"]
#foods = ["Muffins", "Croissant", "Sandwiches", "Biscuits", "Fruits"]
books = ["Rich Dad, Poor Dad", "Harry Potter", "48 Powers", "The Power Of Now", "Diary Of A Wimpy Kid"]
customer_order = []

option_chosen = input(options)


while True:
    if option_chosen == "1":
        menu_options = input(menu)
        if menu_options == "1":
            item_chosen = input(menu_items)
            for item in menu_items.values():                             
                if item == item_chosen:
                    customer_order.append(item)
        break
    elif option_chosen == "2":
        menu_options = input(menu)
        if menu_options == "2":
            print(books)
        break
    elif option_chosen == "3":
        menu_options = input(employee_menu)
        if menu_options == "3":
            print(employee_menu)
        break
    else:
        print("Try again")
        break





