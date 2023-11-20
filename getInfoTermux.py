import user_handler
import datetime
import validators


def getnvalidateData():
    data = []
    while True:
        x = input("Name the bot [Any name]: ")
        if not x.isalnum():
            print("Name should only be alphanumeric a-z/A-Z/0-9")
            continue

        elif user_handler.isDuplicate(x):
            print("User already exists")
            continue
        data.append(x)
        break

    while True:
        x = input("Enter movie name [Exactly as given in website]: ")
        if not x.isalnum():
            print("Movie name should only be alphanumeric a-z/A-Z/0-9")
            continue
        data.append(x)
        break

    while True:
        try:
            x = input("Enter date [To check availability, format yyyy-mm-dd]: ")
            d = list(map(int, x.split('-')))
            dateobj = datetime.date(d[0], d[1], d[2])
            if dateobj < datetime.date.today():
                raise ValueError
        except ValueError:
            print("Incorrect date format")
            continue
        data.append(x)
        break

    while True:
        x = input("Enter frequency to check [in mins, min 5 max 59]: ")
        if not x.isnumeric() and (int(x) < 5 or int(x) > 59):
            print("Frequency should be a number in range 5-59")
            continue
        data.append(x)
        break

    while True:
        x = input("Enter Theater Link: ")
        if not validators.url(x):
            print("Invalid Link")
            continue
        data.append(x)
        break
    return data

