def main():
    a=(input())
    print(convert(a))

def convert(text):
    result = text.replace(":)", "🙂").replace(":(","🙁")
    return result

main()