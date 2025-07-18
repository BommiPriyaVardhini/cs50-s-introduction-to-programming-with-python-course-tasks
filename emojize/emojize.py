import re

# Dictionary mapping emoji codes/aliases to emojis
emoji_dict = {
    ":thumbs_up:": "👍",
    ":thumbsup:": "👍",
    ":heart:": "❤️",
    ":heart_eyes:": "😍",
    ":laughing:": "😂",
    ":1st_place_medal:":"🥇",
    ":money_bag:":"💰",
    ":smile_cat:":"😸",
    "hello, :earth_asia:":"hello, 🌏",
    ":candy: or :ice_cream:?":"🍬 or 🍨?"
    # Add more emoji codes and aliases as needed
}

def main():
    input_str = input("Enter a string: ")
    emojized_str = emojize(input_str)
    print("Emojized string:", emojized_str)

def emojize(input_str):
    emojized_str = input_str
    for code, emoji in emoji_dict.items():
        emojized_str = re.sub(re.escape(code), emoji, emojized_str, flags=re.IGNORECASE)
    return emojized_str

if __name__ == "__main__":
    main()
