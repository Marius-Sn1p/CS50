import sys, csv, os.path

def main():

    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")

    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    elif not os.path.isfile(sys.argv[1]):
        sys.exit(f"Could not read {sys.argv[1]}")

    elif ".csv" not in sys.argv[1]:
        sys.exit("Not a CSV file")

    else:
        clean(sys.argv[1], sys.argv[2])


def clean(file, output):

    with open (file) as input:
        r = csv.DictReader(input)

        with open(output,"w") as output:
            header = ["first", "last", "house"]
            w = csv.DictWriter(output, fieldnames = header)
            w.writeheader()

            for student in r:
                lastname, firstname = student["name"].split(", ")
                house = student["house"]
                w.writerow({"first": firstname, "last":lastname, "house":house})


if __name__ == "__main__":
    main()
