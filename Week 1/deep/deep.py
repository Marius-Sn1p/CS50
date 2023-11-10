def main():
    x = input("What is the Answer to the Great Question of Life, the Universe, and Everything?: ").lower().strip()

    if x == '42' or x== 'forty-two' or x== 'forty two':
        return "Yes"
    else:
        return "No"

print(main())