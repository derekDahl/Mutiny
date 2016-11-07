#Determines if input is an odd or even integer
def odd_or_even():
    
    while True:
        num = input("Enter a number or q to quit: ")
               
        if num == "q":
            print("Thank you!")
            break
        elif int(num) % 2 == 0:
            print("The number is even!")
        elif int(num) % 2 != 0:
            print("The number is odd!")

odd_or_even()
                  
