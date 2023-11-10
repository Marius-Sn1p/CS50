def main():
    items = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
    }

    total = 0

    while True:

        try:
            choices = input("Item: ").title()
        except EOFError:
            return 0

        try:
            total += items[choices]
            print(f"Total: ${total:.2f}")
        except KeyError:
            pass

main()