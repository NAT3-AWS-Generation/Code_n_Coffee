options = ["1.  COLLECTION", "2.  DELIVERY", "3.  EMPLOYEES", "4.  LEAVE"]
menu = ["1. Menu", "2. Books"]
employee_menu = ["1. Remove Drinks/Food", "2. Add Drinks/Foods", "Add/Remove Books"]
menu_items = {'Drinks': ["Ice Coffee", "Coffee", "Juice", "Water", "Hot Chocolate"], 'Foods': ["Muffins", "Croissant", "Sandwiches", "Biscuits", "Fruits"]}
books = ["Rich Dad, Poor Dad", "Harry Potter", "48 Powers", "The Power Of Now", "Diary Of A Wimpy Kid"]
customer_order = []
customer_data = {}

print(f"\n\nWelcome to Code n Coffee, How can we help you\n\n")

name_answer = input(f"Please enter your name:\n").title()
postcode = input(f"Please enter your postcode:\n").upper()
customer_data['first_name'] = name_answer
customer_data['postcode'] = postcode

def main_function():
    option_chosen = input(f"Choose an option:\n\n\n{'     ' .join(options)}\n\n")
# Collection option chosen
    if option_chosen == "1":
         #prompt to enter Name
        collections_order()
        menu_options = input(f"Choose:\n1. Menu\n2. Books\n3. Leave Code n Coffee\n")
# Collections Menu Option Open
        if menu_options == "1":  
            print(f"Which of the following would you like?\n\n")
            for category, items in menu_items.items():
                print(f"{category}:  {'  , '.join(items)}\n\n")
            item_chosen = input(f"What would you like or order?:\n\n").title()
            found = False
            for category, items in menu_items.items():
                if item_chosen in items:
                    customer_order.append(item_chosen)
                    found = True
                    main_function()
            if not found:
                    print(f"\n\nITEM NOT AVAILABLE - TRY AGAIN\n\n")
                    main_function()
        
# Books options open
        elif menu_options == "2":  
            print(f"Which of the following books would you like?:\n\n {'  ,  '.join(books)}\n\n")
            item_chosen = input(f"What book would you like to read?:\n\n").title()
            if item_chosen in books:
                    customer_order.append(item_chosen)
                    main_function()
            else:
                    print("ITEM NOT AVAILABLE - TRY AGAIN")
                    main_function()
# To leave collections
        elif menu_options == "3":
            print(f"Goodbye")
            print(f"{customer_data['first_name']}, you have ordered the following:  {customer_order}")

# Delivery option chosen  
    elif option_chosen == "2":
        menu_options = input(f"Choose:\n1. Menu\n2. Books\n3. Leave Code n Coffee\n")
        if menu_options == "1":
            
            print(f"Which of the following would you like delivered?\n\n")
            for category, items in menu_items.items():
                print(f"{category}:  {'  , '.join(items)}\n\n")
            item_chosen = input(f"What would you like or order for delivery?:\n\n").title()
            
            found = False
            for category, items in menu_items.items():
                if item_chosen in items:
                    customer_order.append(item_chosen)
                    found = True
                    main_function()
            if not found:
                    print("ITEM NOT AVAILABLE - TRY AGAIN")
                    main_function()
            
#Option Books will list books
        elif menu_options == "2":  
            print(f"Which of the following books would you like delivered?:\n {books}")
            item_chosen = input("What book would you like to read?:\n").title()
            if item_chosen in books:
                    customer_order.append(item_chosen)
                    main_function()
            else:
                print("ITEM NOT AVAILABLE - TRY AGAIN")
                main_function()
                            
        elif menu_options == "3":
            print(f"Goodbye")
            print(f"{customer_data['first_name']}, you have ordered the following:  {customer_order}")

    
    # Employees Only 
    elif option_chosen == "3":
        password = input(f"Please enter employee password:\n\n\n")
        if password != "generation":
            print("Incorrect password. Returning to the main menu.")
            main_function()
        else: 
             employee_choice = input(f"\n\n\nChoose:\n 1.Remove Drinks/Foods \n 2.Add Drinks/Foods\n 3.Remove Books\n 4.Add Books\n 5.Leave Code n Coffee\n")
        if employee_choice == "1":
                for category, items in menu_items.items():
                    removed_item = input(f"Please type what you want removed: \n{items}").title()
                    if removed_item in items:
                        items.remove(removed_item)
        elif employee_choice == "2":
                for category, items in menu_items.items():
                    add_item = input(f"Please type what you want to add: \n{items}").title()
                    items.append(add_item)
        
        elif employee_choice == "3":
                    book_choice = input(f"Please type the book name to remove:\n {books}").title()
                    if book_choice in books:
                        books.remove(book_choice)
        elif employee_choice == "4":
                    book_choice = input(f"Please type the book name to add:\n {books}").title()
                    books.append(book_choice)
        elif employee_choice == "5":
                print(f"Goodbye")
     
    elif option_chosen == "5":
            print(f"Goodbye")
            print(f"{customer_data['first_name']}, you have ordered the following:  {customer_order}")


main_function()
    

  