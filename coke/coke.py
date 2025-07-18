# coke.py

def main():
    amount_due = 50
    accepted_coins = [25, 10, 5]

    while amount_due > 0:
        print(f"Amount Due: {amount_due}")
        try:
            coin = int(input("Insert Coin: "))
            if coin in accepted_coins:
                amount_due -= coin
            else:
                print(f"Coin not accepted: {coin}")
        except ValueError:
            print("Invalid input. Please insert a valid coin.")

    if amount_due < 0:
        print(f"Change Owed: {abs(amount_due)}")
    else:
        print("Change Owed: 0")

if __name__ == "__main__":
    main()

