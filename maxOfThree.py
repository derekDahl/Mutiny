def max_of_three():
    x = input("Enter first number: ")
    y = input("Enter second number: ")
    z = input("Enter third number: ")
    if x > y and z:
        print(x)
    elif y > x and y > z:
        print(y)
    elif z > x and z > y:
        print(z)

max_of_three()
