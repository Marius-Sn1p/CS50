def main():
    s = str(input("Greeting: ")).lower()

    if "hello" in s.split()[0]:
        return "$0"
    elif s[0] == 'h':
        return "$20"
    else:
        return "$100"

print(main(), end='')