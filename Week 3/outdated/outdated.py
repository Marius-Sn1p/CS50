def main():

    months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
    ]

    while True:
        date = input("Date: ").strip().title()

        try:

            if "/" in date:

                parts = date.split("/")

                if len(parts) != 3:
                    raise ValueError

                if not parts[0].isdigit() or not parts[1].isdigit() or not parts[2].isdigit():
                    raise ValueError

                if int(parts[1]) > 31 or int(parts[0]) > 12:
                    raise ValueError

                month, day, year = parts

                break

            elif "," in date and " " in date:

                parts = date.split(" ")

                if "," in parts[1]:
                    parts[1] = parts[1].replace(",","")

                if parts[0] not in months:
                    pass
                else:
                    parts[0] = str(months.index(parts[0])+1)

                if not parts[0].isdigit() or not parts[1].isdigit() or not parts[2].isdigit():
                    raise ValueError

                if int(parts[1]) > 31 or int(parts[0]) > 12:
                    raise ValueError

                month, day, year = parts

                break

        except (AttributeError, ValueError, NameError, KeyError):
            pass

    return f"{year}-{month.zfill(2)}-{day.zfill(2)}"

print(main())


