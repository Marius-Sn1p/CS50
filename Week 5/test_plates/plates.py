def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):

    found_digit = False

    if s.isalnum():

        if 6>=len(s)>=2:

            if s[0].isalpha() and s[1].isalpha():

                for i, char in enumerate(s):

                    if char.isdigit():

                        if not found_digit and char == '0':
                            return False

                        found_digit = True

                    else:
                        if found_digit:
                            return False
            else:
                return False
        else:
            return False
    else:
        return False

    return True


if __name__ == "__main__":
    main()