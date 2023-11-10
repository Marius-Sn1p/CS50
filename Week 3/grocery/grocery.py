def main():

    items = {}

    while True:

        try:
            item = input("").upper()

            if item not in items:
                items[item] = 1
            else:
                items[item] += 1

        except EOFError:
            break


    items = dict(sorted(items.items()))

    for k,v in items.items():
        print(f"{v} {k}")

main()