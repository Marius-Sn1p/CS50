def main():
    amount = 50
    coins = [25, 10, 5]

    while amount != 0:

        print(f"Amount Due: {amount}")

        coin = int(input("Insert coin: "))

        if coin in coins:
            amount -=coin

            if amount < 0:
                amount *= -1
                print(f"Change Owed: {amount}")
                amount = 0
            elif amount == 0:
                print("Change Owed: 0")
        else:
            continue

main()
