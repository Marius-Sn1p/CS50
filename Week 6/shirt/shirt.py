import sys, os.path

from PIL import Image, ImageOps


def main():

    formats = ['jpg', 'jpeg', 'png']

    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")

    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    elif sys.argv[1].split('.')[1] not in formats or sys.argv[2].split('.')[1] not in formats:
        print(sys.argv[1].split('.')[1])
        sys.exit("Invalid input")

    elif sys.argv[1].split('.')[1] != sys.argv[2].split('.')[1]:
        sys.exit("Input and output have different extensions")

    elif not os.path.isfile(sys.argv[1]):
        sys.exit("Invalid input")

    else:
        shirt_on(sys.argv[1], sys.argv[2])


def shirt_on(file1, file2):

    shirt = Image.open("shirt.png")

    photo = Image.open(file1)

    photo = ImageOps.fit(photo, shirt.size)

    photo.paste(shirt, shirt)

    photo.save(file2)


if __name__ == "__main__":
    main()