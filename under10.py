#Create a list of numbers
#Print a new list only with numbers under 10, then print numbers in list under input
num_list = [1, 2, 4, 4, 5, 9, 10, 12, 13, 22, 36, 45, 77, 144]

def user_compare():
        user_list = []
        user_num = int(input("Enter a numbner: "))
        for num in num_list:
                if num <= user_num:
                        user_list.append(num)
        print(user_list)

        
under_ten = []
for x in num_list:
        if x < 10:
                under_ten.append(x)

print(under_ten)

user_compare()


