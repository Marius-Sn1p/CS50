import random


while True:

    try:
        num = int(input("Level: "))
        select = random.randint(1, num)

        while True:

            guess = int(input("Guess: "))

            if select == guess:
                print("Just right!")
                raise EOFError
            elif guess > select:
                print("Too large!")
            else:
                print("Too small!")

    except ValueError:
        pass
    except EOFError:
        break
