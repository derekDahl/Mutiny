#Tells the user which year they will turn 100 based on their current age
import time

name = ""
age = int()
def get_name():
    global name
    name = input("What is your name? ")
    return name
    
def get_age():
    age = int(input("Hello " + name + "! \nHow old are you? "))
    return age

while True:
    
    get_name()
    age = get_age()
    curYear = time.localtime(time.time())
    year = str(curYear[0] - age + 100)
    print("You will turn 100 in the year " + str(year))
    want = int(input("How many years would you like to live? "))
    print(str("If you live to be " + str(want) + " years old, you will live until the year " + str(curYear[0] - age + want)))

    


