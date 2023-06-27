""" 
1) Build a Shopping Cart

You can use either lists or dictionaries. The program should have the following capabilities:

1) Takes in input
2) Stores user input into a dictionary or list
3) The User can add or delete items
4) The User can see current shopping list
5) The program Loops until user 'quits'
6) Upon quiting the program, print out all items in the user's list 


{
  'milk':{
    'quantity': int,
    'price' : bool
  }
}
"""
shopping_cart = {}

def driver():
    shopping = True
    while shopping:
        user_choice = get_input()
        if user_choice in ['a', 'add']:
            get_item_info()
        elif user_choice in ['r','remove']:
            get_remove_info()
        elif user_choice in ['show','s']:
            pass
        else:
            shopping = False
        show()

def get_input():
    while True:
      user_choice = input("What would you like do? [A]dd/[R]emove/[S]how/[Q]uit: ").lower()
      if user_choice in ['a','r','s','q','add','remove','show','quit']:
          return user_choice
      print('Please choose a valid option\n')

def get_item_info():
    item = input('What item are you adding? ')
    while True:
      try:
        quantity = int(input("How many would you like to add? "))
        break
      except:
          print('Please enter quantity in digits')
    while item not in shopping_cart:
        try:
            price = float(input("How much does item cost? "))
            break
            # formatted_number = '{:.2f}'.format(number)
        except:
          print('Please enter price in digits')
    add_item(item, quantity, price)

def add_item(item, quantity, price):
    if item in shopping_cart:
        shopping_cart[item]['quantity'] += quantity
        pass
    else:
        shopping_cart[item] = {
            'quantity': quantity,
            'price': price
        }

def get_remove_info():
    item = input('What item would you like to remove? ')
    while True:
        quantity = input("How many are you removing? ")
        if quantity.isdigit():
            quantity = int(quantity)
            break
        print('Please enter quantity in digits')
        
    remove_item(item,quantity)

def remove_item(item,quantity):
    if item in shopping_cart:
        shopping_cart[item]['quantity'] -= quantity
        if shopping_cart[item]['quantity'] < 1:
            shopping_cart.pop(item)
    else:
        print('Item not in cart')

def show():
    for item,info in shopping_cart.items():
        print(f'Item: {item}\nQuantity: {info["quantity"]}\nPrice: {info["price"]:.2f}')
        
driver()