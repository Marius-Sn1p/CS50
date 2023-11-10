import validators

def main():
    email = input("What's your email address? ").strip()

    return "Valid" if validators.email(email) else "Invalid"


if __name__ == "__main__":
    print(main())