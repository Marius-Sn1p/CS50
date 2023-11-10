def main():

    x, y = get_fraction()

    result = (x/y) * 100

    if result <= 1:
        return "E"
    elif result >= 99:
        return "F"
    else:
        return f"{round(result)}%"



def get_fraction():

    while True:

        fraction = input("Fraction: ")


        try:
            x, y = fraction.split('/')
            x = int(x)
            y = int(y)


            if x>y or y==0 or type(x) == 'float' or isinstance(y, float):
                pass
            else:
                break
        except:
            pass

    return x, y

print(main())

