import re



def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):

    pattern = "([0-1]?([0-9]?){2}|2[0-4]?[0-9]?|25[0-5]?)"

    matches = re.search(r"^" + pattern + "\." + pattern + "\." + pattern + "\." + pattern + "$", ip)

    if matches:
        return True
    else:
        return False


if __name__ == "__main__":
    main()