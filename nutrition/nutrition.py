def main():
    fruit_calories = {
        "bananas": 105,
        "grapes": 62,
        "oranges": 62,
        "strawberries": 49,
         "apple":130,
         "kiwifruit":90,
         "avocado":50,
         "pear":100,
         "sweet cherries":100
        # Add more fruits and their respective calories here
    }

    fruit = input("Enter a fruit: ").lower()
    if fruit in fruit_calories:
         print(fruit_calories[fruit])

if __name__ == "__main__":
    main()
