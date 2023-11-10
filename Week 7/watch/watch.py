import re


def main():
    url = input("HTML: ")
    return print(parse(url))

def parse(url_link):

    if link:= re.search(r"<iframe src=\"(https?://)?(www\.)?youtube\.com/embed/([a-z0-9]+)\"></iframe>", url_link, re.IGNORECASE):
        return f"https://youtu.be/{link.group(3)}"

    else:
        return None



if __name__ == "__main__":
    main()