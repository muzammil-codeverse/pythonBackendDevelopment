age = int(input("Enter your age >> "))
match age:
    case 18:
        print("You are 18 years old")
    case 19 | 20:
        print("You are either 19 or 20 year old")
    case 26:
        print("You are 26 years old")
    case 30:
        print("You are 30 years old")
    case _:
        print("Invalid age entered")
