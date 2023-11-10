import random


def main():
    score = 0
    count = 10
    tries = 3
    l = get_level()

    while count != 0:

        if tries == 3:
            x,y = generate_integer(l)

            try:
                guess = int(input(f"{x} + {y} = "))

                if guess == x+y:
                    count -= 1
                    score += 1
                    tries = 3
                else:
                    raise ValueError

            except (ValueError, NameError):
                print("EEE")
                tries -= 1
                pass

            if tries == 0:
                print(f"{x} + {y} = {x+y}")
                tries = 3
                count-=1

    print(f"Score: {score}")

def get_level():


    while True:

        try:
            level = int(input("Level: "))

            if 0<level<4:
                break
            else:
                pass
        except ValueError:
            pass

    return level




def generate_integer(level):

    if level == 1:
        x = random.randint(0, 9)
        y = random.randint(0, 9)
    elif level == 2:
        x = random.randint(10, 99)
        y= random.randint(10, 99)
    else:
        x = random.randint(100,999)
        y = random.randint(100,999)

    return x, y


if __name__ == "__main__":
    main()
