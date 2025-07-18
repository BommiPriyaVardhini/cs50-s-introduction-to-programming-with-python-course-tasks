MENU = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

def main():
    total_cost = 0
    print_menu()
    print("Start placing your order (press Ctrl-D when done):")
    while True:
        try:
            item = input().title()
            if item in MENU:
                total_cost += MENU[item]
                print(f"Total cost: ${total_cost:.2f}")
            else:
                print("Invalid item. Please enter a valid item from the menu.")
        except EOFError:
            break

def print_menu():
    print("Menu:")
    for item, price in MENU.items():
        print(f"{item}: ${price:.2f}")

if __name__ == "__main__":
    main()
