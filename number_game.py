print("-----Welcome to Number Game Verse-----")
num = int(input("Enter the First Digit of the Number >> "))
zeroes = int(input(f"How Many Zeroes You Want to Add in {num} >> "))
isspecialdigit = input("Do You want to add any number with in your digit [y|n]?\n>> ")
if isspecialdigit == "y":
    specialdigit = int(input("Tell us the Number you want to add >> "))
    placement = int(input("At which position you want to add >> "))
for i in range(1,(zeroes+1)):
    num*=10
    if(i==placement):
        num+=specialdigit
print(f"Your Desired Number is >> {num} :)")
