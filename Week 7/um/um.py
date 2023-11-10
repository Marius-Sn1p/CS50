import re

def main():
    print(count(input("Text: ")))


def count(s):

    pattern = "(^|\W)um($|\W)"

    matches = re.findall(pattern, s, re.IGNORECASE)

    if matches:
        return len(matches)

if __name__=="__main__":
    main()