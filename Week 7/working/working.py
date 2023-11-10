import re


def main():
    print(convert(input("Hours: ")))


def convert(s):

    pattern = r"(0?[1-9]|1[0-2]):?\.?([0-5][0-9])? (AM|PM)"
    matches = re.search(r"^" + pattern + " to " + pattern + "$", s)

    if matches:

        starting_time = am_pm(matches.group(1),matches.group(2),matches.group(3))
        ending_time= am_pm(matches.group(4),matches.group(5),matches.group(6))
        return f"{starting_time} to {ending_time}"

    else:
        raise ValueError

def am_pm(hours, minutes, zone):

    if hours == "12":

        if zone == "AM":
            hours = "00"

        else:
            hours = "12"

    else:

        if zone == "AM":
            hours = f"{int(hours):02}"

        else:
            hours = f"{int(hours)+12}"

    if not minutes:
        minutes = "00"

    else:
        minutes = f"{int(minutes):02}"

    return f"{hours}:{minutes}"



if __name__ == "__main__":
    main()