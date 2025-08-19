import time

def hello_message():
    print("Hello everyone!")
    print("===============")
    print("Welcome to our Restaurant.")
    print("=========================")
    print("We are here to take your order!")
    print("===============================")
    print("What would you like to choose from the menu:")
    print("Pizza, Hamburger, Hot Dog")
    print("=========================")

def menu():
    choices = ["Pizza", "Hamburger", "Hot Dog"]
    request = input("Please make your choice from the menu:")
    if request in choices:
        print(request, "has been ordered.")
    else:
        print("Processing....")
        time.sleep(1)
        print(request, "Sorry this item is not available!")
        print("Please try again with an item from the menu!")
        menu() #Retry


def pizza_topping():
    topping = ["Mushrooms", "Onions", "Anchovies", "Pineapples", "Chorizo"]
    request = input("Please enter your topping from the menu: ")
    if request in topping:
        print(request, "Topping is available")
        print("Topping request has been added to your order!")
    else:
     print("Processing...")
     time.sleep(1)
     print(request, "Sorry, topping is not available!")
     request = input("Please make your choice from the menu:")
     pizza_topping() #Retry

def soft_drink():
    print("Please order your drinks")
    drinks = ["Cola", "Fanta", "Sprite", "Beer"]
    request = input("Enter your drink choice: ")
    if request in drinks:
        print(request, "Is available and has been added to your order!")
        thank_customer()
    else:
        print("Processing.. ")
        time.sleep(2)
        print(request, "is not currently available")
        print("Please choose again an item from the menu:")
        soft_drink() #Retry


def thank_customer():
    print("Thank you for choosing us, Enjoy your meal!")

# Run the program

hello_message()
menu()
pizza_topping()
soft_drink()