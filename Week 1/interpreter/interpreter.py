def main ():
    s= input("Expression: ")

    a, b, c = s.split()

    a= float(a)
    c= float(c)

    if b == "+":
        return a + c
    elif b== "-":
        return a - c
    elif b=="*":
        return a*c
    else:
        return a/c

print(main()) 