def main():
    s = input("Input: ")

    return f"Output: {remove_vowels(s)}"


def remove_vowels(text):

    for i in text:
        if i in "aeiouAEIOU":
            text = text.replace(i,"")

    return text

print(main())