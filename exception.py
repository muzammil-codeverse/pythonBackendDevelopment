items = [1,2,3,4,5]
try:
    print("items >> "+str(items[5]))
except IndexError as IE:
    print("Item don't exist in the code :(")
def Division(a,b):
    return a/b    
try:
    print(Division(10,0))
except ZeroDivisionError:
    print(0)