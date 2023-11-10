import sys
import random
from pyfiglet import Figlet

figlet = Figlet()

arguments = ["-f","--font"]

def main():


    if len(sys.argv) <2:
        text = input("Input: ")
        font = random.choice(figlet.getFonts())
        render_text(text, font)
    elif len(sys.argv) == 3 and sys.argv[1] in arguments and sys.argv[2] in figlet.getFonts():
        text = input("Input: ")
        font = sys.argv[2]
        render_text(text, font)
    else:
        sys.exit("Invalid input")



def render_text(prompt, f):

    figlet.setFont(font = f)
    result = figlet.renderText(prompt)
    print(f"Output: {result}")

main()

