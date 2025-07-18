def main():
    grocery_list = {}
    #print("Start making your grocery list (press Ctrl-D when done):")
    while True:
        try:
            item = input()
            if item.lower() in grocery_list:
                grocery_list[item.lower()] += 1
            else:
                grocery_list[item.lower()] = 1
        except EOFError:
            break

    print_grocery_list(grocery_list)


def print_grocery_list(grocery_list):
    sorted_items = sorted(grocery_list.items(), key=lambda x: x[0])
    for item, count in sorted_items:
        print(f"{count} {item.upper()}")


if __name__ == "__main__":
    main()
