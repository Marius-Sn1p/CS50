from datetime import date
import sys
import inflect

p = inflect.engine()

def main():
    try:

        birth_date = input("Date of Birth: ")
        difference = date.today() - date.fromisoformat(birth_date)
        print(get_minutes(difference.days))

    except ValueError:

        sys.exit("Invalid date")

def get_minutes(num):

    total = num * 24 * 60
    return f'{p.number_to_words(total, andword="").capitalize()} minutes'

if __name__ == "__main__":
    main()


"""from datetime import datetime
import sys
import inflect

def main():
    print(get_minutes(input("Date of Birth: ")))

def get_minutes(birth_date):

    p = inflect.engine()

    date_format = "%Y-%m-%d"

    today = datetime.today().date()

    try:
        final  = datetime.strptime(birth_date, date_format)

    except:
        sys.exit("Invalid date")

    total_minutes= ((today-final.date()).total_seconds())/60

    return f'{p.number_to_words(int(total_minutes), andword="").capitalize()} minutes'


if __name__ == "__main__":
    main()
"""