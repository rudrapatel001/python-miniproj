menu = {
    'pizza': 60,
    'pasta': 40,
    'burger': 60,
    'salad': 70,
    'coffee': 80,
}

print("----------Welcome to Rudra's Restaurant----------\n")
print("--------------------Our Menu--------------------\n")


for item, price in menu.items():
    print(f"{item.capitalize()}: {price} Rs")

order_total = 0
order_list = []

while True:
    item = input("\nWhat would you like to order (type 'done' to finish, 'delete' to remove an item)? ").lower().strip()

    if item == "done":
        break
    elif item == "delete":
        if not order_list:
            print("Your order list is empty. You cannot delete an item.")
            continue
        delete_item = input("Which item would you like to delete? ").lower().strip()
        if delete_item in order_list:
            order_list.remove(delete_item)
            order_total -= menu[delete_item]
            print(f"{delete_item.capitalize()} has been removed from your order.")
            print(f"Current total: {order_total} Rs")
        else:
            print(f"Sorry, {delete_item} is not in your order list.")
    elif item in menu:
        order_list.append(item)
        order_total += menu[item]
        print(f"You have selected {item}.")
        print(f"Current total: {order_total} Rs")
    elif not item:
        print("Please enter a valid menu item.")
    else:
        print(f"Sorry, {item} is not available in the restaurant.")

print(f"\nThe total amount to pay is {order_total} Rs")
