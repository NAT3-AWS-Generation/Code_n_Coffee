options = ["1.  COLLECTION", "2.  DELIVERY", "3.  EMPLOYEES", "4.  CHECKOUT"]
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
    option_chosen = input(f"\n\nChoose an option:\n\n\n{'     ' .join(options)}\n\n")
# Collection option chosen
    if option_chosen == "1":
         #prompt to enter Name
        collections_order()
    if option_chosen == "2":
         #prompt to enter Name
        delivery_order()
    if option_chosen == "3":
         #prompt to enter Name
        employee_password()
    if option_chosen == "4":
        print(f"Goodbye")
        print(f"{customer_data['first_name']}, you have ordered the following:  {'  ,  '.join(customer_order)} and will be delivered to {customer_data['postcode']}")


def collections_order():
    while True:
        menu_options = input(f"\n\nChoose an option:\n\n1.  Menu     2.  Books     3.  Return To Main Menu\n\n".upper())
        if menu_options == "1":  
            print(f"Which of the following would you like?\n\n")
            for category, items in menu_items.items():
                print(f"{category.upper()}:  {'  , '.join(items)}\n\n")
            item_chosen = input(f"What would you like to order?:\n\n").title()
            found = False 
            for category, items in menu_items.items():
                if item_chosen in items:
                    customer_order.append(item_chosen)
                    found = True
                    break  
            if not found:
                print(f"\n\nITEM NOT AVAILABLE - TRY AGAIN\n\n")
        elif menu_options == "2":  
            print(f"Which of the following books would you like?:\n\n {'  ,  '.join(books)}\n\n")
            item_chosen = input(f"What book would you like to read?:\n\n").title()
            found = False
            for book in books:
                if item_chosen == book:
                    customer_order.append(item_chosen)
                    found = True
                    break
            if not found:
                    print("ITEM NOT AVAILABLE - TRY AGAIN")
                    
# To leave collections
        elif menu_options == "3":
            print(f"\n\n\nReturning main menu\n\n\n".upper())
            print(f"\n\n{customer_data['first_name']}, you have ordered the following:  {'  ,  '.join(customer_order)}\n\n")
            main_function()
            break
            
def delivery_order():
    while True:
        menu_options = input(f"\n\nChoose an option:\n\n1.  Menu     2.  Books     3.  Return To Main Menu\n\n".upper())
        if menu_options == "1":  
            print(f"Which of the following would you like delivered?\n\n")
            for category, items in menu_items.items():
                print(f"{category.upper()}:  {'  , '.join(items)}\n\n")
            item_chosen = input(f"What would you like to order for delivery?:\n\n").title()
            found = False 
            for category, items in menu_items.items():
                if item_chosen in items:
                    customer_order.append(item_chosen)
                    found = True
                    break  
            if not found:
                print(f"\n\nITEM NOT AVAILABLE - TRY AGAIN\n\n")
        elif menu_options == "2":  
            print(f"Which of the following books would you like delivered?:\n\n {'  ,  '.join(books)}\n\n")
            item_chosen = input(f"What book would you like to read?:\n\n").title()
            found = False
            for book in books:
                if item_chosen == book:
                    customer_order.append(item_chosen)
                    found = True
                    break
            if not found:
                    print("ITEM NOT AVAILABLE - TRY AGAIN")
                    
# To leave 
        elif menu_options == "3":
            print(f"\n\n\nReturning main menu\n\n\n".upper())
            print(f"{customer_data['first_name']}, you have ordered the following:  {' , '.join(customer_order)} and will be delivered to {customer_data['postcode']}")
            main_function()
            break


def employee_password():
        password = input(f"Please enter employee password:\n\n\n")
        if password != "generation":
            print("Incorrect password. Returning to the main menu.")
            main_function()
        else:
            employee_area() 
def employee_area():
    employee_choice = input(f"\nChoose:\n 1. Remove Drinks/Foods \n 2. Add Drinks/Foods\n 3. Remove Books\n 4. Add Books\n 5. Return To Main Menu\n")

    if employee_choice == "1":
        for category, items in menu_items.items():
            removed_item = input(f"Please type what you want removed from {category}: \n{items}").title()
            if removed_item in items:
                items.remove(removed_item)
                print(f"\n\n\nItem Removed {category}: {removed_item}\n\n\n")
            else:
                print(f"{removed_item.upper()} NOT AVAILABLE! ")
        employee_area()

    elif employee_choice == "2":
        for category, items in menu_items.items():
            add_item = input(f"Please type what you want to add to {category}: \n{items}").title()
            items.append(add_item)
            print(f"\n\n\nItem Added to {category}: {add_item}\n\n\n")
        
        employee_area()
        
    elif employee_choice == "3":
        book_choice = input(f"Please type the book name to remove:\n {books}").title()
        if book_choice in books:
                books.remove(book_choice)
                print(f"\n\n\Book Removed to {book_choice}\n\n\n")
        else:
                print(f"{removed_item.upper()} NOT AVAILABLE! ")
        
        employee_area()

    elif employee_choice == "4":
        book_choice = input(f"Please type the book name to add:\n {books}").title()
        books.append(book_choice)
        print(f"\n\nBook Added to {book_choice}\n\n")

        employee_area()

    elif employee_choice == "5":
            print(f"\n\nReturning back to main menu\n\n".upper())
            main_function()
                

main_function()