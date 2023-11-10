import csv, sys, os.path
from tabulate import tabulate


def main():

    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")

    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")

    elif ".csv" not in sys.argv[1]:
        sys.exit("Not a CSV file")

    elif not os.path.isfile(sys.argv[1]):
        sys.exit("File does not exist")

    else:
        print(tabletaze(sys.argv[1]))


def tabletaze(file):

    with open (file) as f:
        r = csv.reader(f)
        table = tabulate(r, headers="firstrow", tablefmt="grid")
        return table

if __name__ == "__main__":
    main()