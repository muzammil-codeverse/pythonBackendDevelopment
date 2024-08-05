yourName = "\nYes My Name is Mohtashim Hassan"
with open("file.txt",'r+') as file:
    firstLine = file.readline()
    print(firstLine)
    file.write(yourName)