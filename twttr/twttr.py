def main():
    text = input("Enter a text: ")
    text_without_vowels = remove_vowels(text)
    print("Text without vowels:", text_without_vowels)


def remove_vowels(text):
    vowels = "aeiouAEIOU"
    return "".join(char for char in text if char not in vowels)


if __name__ == "__main__":
    main()
