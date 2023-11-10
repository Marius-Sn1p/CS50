import sys, os.path

def main():

    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")

    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")

    elif ".py" not in sys.argv[1]:
        sys.exit("Not a Python file")

    elif not os.path.isfile(sys.argv[1]):
        sys.exit("File does not exist")

    else:
        print(count_lines(sys.argv[1]))


def count_lines(file):

    with open(file, "r") as f:

        count = 0

        for line in f:

            if line.lstrip().startswith("#") or line.strip() == "":
                pass

            else:
                count+=1

        return count




if __name__ == "__main__":
    main()