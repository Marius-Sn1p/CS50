def main():
    s = input("Input: ")

    return f"Output: {shorten(s)}"


def shorten(word):

    for i in word:
        if i in "aeiouAEIOU":
            word = word.replace(i,"")

    return word

if __name__ == "__main__":
    main()
