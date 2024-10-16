manu = {
    "pizza": 80,
    "pasta": 70,
    "coffee": 100,
    "burger": 90,
    "icecream": 90,
    "coldrinks": 70,
    "simple pasta": 50,
    "rigatoni pasta": 70,
    "linguine pasta": 80,
    "fusilli pasta": 110,
    "simple burger": 60,
    "cheese burger": 90,
    "lamb burger": 100,
    "specialty burger": 110,
    "simple dosa": 70,
    "cheese dosa": 90,
    "masala dosa": 80,
    "adai dosa": 110,
    "neer dosa": 120,
}

order_total = 0
order_items = []

def pasta():
    print("============== Pasta =================")
    print("simple pasta  50rs\nrigatoni pasta  70rs\nlinguine pasta  80rs\nfusilli pasta  110rs")

def burger():
    print("============== Burger =================")
    print("simple burger  60rs\ncheese burger  90rs\nlamb burger  100rs\nspecialty burger 110rs")

def dosa():
    print("========== Dosa ============")
    print("simple dosa  70rs\ncheese dosa  90rs\nmasala dosa  80rs\nadai dosa  110rs\nneer dosa  120rs")

def starter_manu():
    print("============== Starter ===============")
    print("Pizza : 80rs\npoha : 70rs\nCoffee : 100rs\nsalad : 90rs\nIce-cream : 90rs\nColdrinks : 70rs")

def exit_program():
    print("Thank you for visiting S.K.T Restaurant!")

def user_item():
    global order_total
    while True:
        item = input("Enter the name of the dish that you want to order: ").strip().lower()
        if item in manu:
            order_items.append(item)
            order_total += manu[item]
            print(f"Your item '{item}' has been added to your order.")
        else:
            print("Sorry, we don't serve that item. Please order another.")

        another_item = input("Do you want to order another item (yes/no): ").strip().lower()
        if another_item != 'yes':
            break

def generate_bill():
    print("\n=========== Bill ===========")
    print("Item\t\tPrice")
    print("---------------------------")
    for item in order_items:
        print(f"{item.capitalize()}\t\t{manu[item]}rs")
    print("---------------------------")
    print(f"Total: {order_total}rs")
    print("===========================")

print("======================================================")
print("''''''''''''' Welcome To S.K.T Restaurant ''''''''''''")
print("======================================================\n")
starter_manu()
print(".............................................................")
print("Press 1. Starter Menu\nPress 2. Pasta\nPress 3. Burger\nPress 4. Dosa\nPress 5. Exit")
user_input = int(input("Enter number how you want to proceed: "))
match user_input:
    case 1:
        starter_manu()
        user_item()
    case 2:
        pasta()
        user_item()
    case 3:
        burger()
        user_item()
    case 4:
        dosa()
        user_item()
    case 5:
        exit_program()

# Generate and print the bill at the end
if order_items:
    generate_bill()
