def main():
    s = convert(input("What time is it?: "))

    if 7 <= s <= 8:
        return "breakfast time"
    elif 12 <= s <= 13:
        return "lunch time"
    elif 18 <= s <= 19:
        return "dinner time"
    else:
        return ""


def convert(time):

    h, m = time.split(':')

    if "p.m." in time:
        m=int(m.split()[0])
        h= int(h)+12
    elif "a.m." in time:
        m=int(m.split()[0])

    m= int(m)/60
    return int(h) + m

if __name__ == "__main__":
    print(main())