def main ():
    s = str(input("File name: ")).lower().strip()

    image = ["gif","jpg", "jpeg", "png"]
    application = ["pdf", "zip"]

    extension = s.split('.')[-1]

    if extension in image:
        if extension == "jpg":
            return "image/jpeg"
        else:
            return f"image/{extension}"
    elif extension in application:
        return f"application/{extension}"
    elif extension == "txt":
        return "text/plain"
    else:
        return "application/octet-stream"

print(main())