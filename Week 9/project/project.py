import sys
import validators
import smtplib
import requests
import random

class Recipe:

    def __init__(self, ingredients, instructions, name, servings):

        self.ingredients = ingredients
        self.instructions = instructions
        self.name = name
        self.servings = servings

    def compose_email(self):

        new_line = "\n"
        return f"{self.name}\n\nServings: {self.servings}\n\nIngredients:\n{(self.ingredients).replace('|', new_line)}{new_line}{new_line}Instructions:\n{self.instructions}\n\n"

    @classmethod
    def get_recipe(cls):

        api_key = "API_KEY_GOES_HERE"
        api_url = f"https://api.api-ninjas.com/v1/recipe?query={cls.meal}"
        response = requests.get(api_url, headers={'X-Api-Key': api_key})

        if response.status_code == requests.codes.ok:

            choices = response.json()
            choice = random.randint(0, len(choices))
            name = choices[choice]['title']
            ingredients = choices[choice]['ingredients']
            servings = choices[choice]['servings']
            instructions = choices[choice]['instructions']

        else:

            sys.exit(response.text)

        return cls(ingredients, instructions, name, servings)

class Breakfast_Meal(Recipe):
    meal = random.choice(["breakfast", "egg", "pancake"])

class Lunch_Meal(Recipe):
    meal = random.choice(["pasta", "salad", "lunch", "quick meal", "sandwich"])

class Dinner_Meal(Recipe):
    meal = random.choice(["dinner", "seafood", "beef", "chicken", "pork"])

class Menu:

    def __init__(self, breakfast, lunch, dinner):

        self.breakfast = breakfast
        self.lunch = lunch
        self.dinner = dinner

    def compose_email(self):

        email_content = ""
        new_line = "\n"

        for meal_type, recipe in [("Breakfast", self.breakfast), ("Lunch", self.lunch), ("Dinner", self.dinner)]:

            email_content += f"{meal_type}\n\n"
            email_content += f"{recipe.name}\n\n"
            email_content += f"Servings: {recipe.servings}\n\n"
            email_content += f"Ingredients:\n{(recipe.ingredients).replace('|', new_line)}{new_line}{new_line}"
            email_content += f"Instructions:\n{recipe.instructions}\n\n"

        return email_content

def main():

    email_address = get_validate_email()
    selection = get_selection()

    if selection == '1':

        send_email(email_address, meal_selection().compose_email())

    elif selection == '2':

        send_email(email_address, generate_menu().compose_email())

def send_email(email_address, body):

    gmail_user = "GMAIL_USERNAME_GOES_HERE"
    gmail_password = "GMAIL_PASSWORD_GOES_HERE"
    to = [email_address]
    subject= "Your recipe(s) for today..."
    email_text = f"Subject: {subject}\n\n{body}"

    try:
        smtp_server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
        smtp_server.ehlo()
        smtp_server.login(gmail_user, gmail_password)
        smtp_server.sendmail(gmail_user, to, email_text.encode('utf-8'))
        smtp_server.close()
        print ("Email sent successfully!")

    except Exception as ex:
        print ("Something went wrong….",ex)

def get_validate_email():

    email_address = input("Please enter your email address: ").strip()

    if validators.email(email_address):

        return email_address

    else:

        sys.exit("Invalid email address provided")

def get_selection():

    selection = input("How many meal recipes would you like to receive?\nOption 1: 1 meal\nOption 2: 3 meals\nYour selection: ").strip().lower()

    if selection == '1' or selection == 'option 1' or selection == '1 meal':

        return '1'

    elif selection == '2' or selection == 'option 2' or selection == '3 meals':

        return '2'

    else:

        sys.exit("Incorrect selection")

def meal_selection():

    meal_type = input("What meal recipe would you like to receive?(Enter coresponsing number)\nOption 1: Breakfast\nOption 2: Lunch\nOption 3: Dinner\nYour selection: ").strip().lower()

    if meal_type == '1' or meal_type == "option 1" or meal_type == "breakfast":

        return Breakfast_Meal.get_recipe()

    elif meal_type == '2' or meal_type == "option 2" or meal_type == "lunch":

        return Lunch_Meal.get_recipe()

    elif meal_type == '3' or meal_type == "option 3" or meal_type == "dinner":

        return Dinner_Meal.get_recipe()

    else:

        sys.exit("Incorrect selection")

def generate_menu():

    breakfast= Breakfast_Meal.get_recipe()
    lunch = Lunch_Meal.get_recipe()
    dinner = Dinner_Meal.get_recipe()

    return Menu(breakfast, lunch, dinner)

if __name__ == "__main__":
    main()