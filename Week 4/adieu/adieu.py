import inflect

lib = inflect.engine()
names = []

while True:
    try:
        name = input("Name: ").strip().title()
        names.append(name)
    except EOFError:
        print("\n" +"Adieu, adieu, to " + lib.join(names))
        break

