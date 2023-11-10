def main():
    s = str(input("Greeting: ")).lower().strip()
    print(f"${value(s)}")


def value(greeting):

    if "hello" in greeting.split()[0]:
        return 0

    elif greeting[0] == 'h':
        return 20

    else:
        return 100


if __name__ == "__main__":
    main()