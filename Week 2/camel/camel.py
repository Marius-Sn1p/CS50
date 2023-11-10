def main():
    s = input("camelCase: ")
    r=''

    for i in s:
        if i.isupper():
            r += '_' + i.lower()
        else:
            r+= i.lower()

    return "snake_case: ", r.lower()

print(main())