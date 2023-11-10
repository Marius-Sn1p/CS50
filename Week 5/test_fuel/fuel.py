def main():

    fraction = input("Fraction: ")
    percentage = convert(fraction)
    print(gauge(percentage))

def convert(fraction):
    x, y = fraction.split("/")

    if int(x)/int(y) > 1:
        raise ValueError

    elif int(y) == 0:
        raise ZeroDivisionError

    return int(int(x)/int(y)*100)

def gauge(percent):

    try:
        if 0 <= percent <= 1:
            return "E"

        elif 99 <= percent <= 100:
            return "F"

        elif 1 < percent < 99:
            return f"{percent}%"

        else:
            raise TypeError

    except TypeError:
        pass



if __name__ == "__main__":
    main()
