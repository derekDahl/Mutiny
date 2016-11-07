#FIZZBUZZ
#Counts to 100
#Numbers with multiples of 3 print fizz
#Numbers with multiples of 5 print buzz
#Numbers with multiples of 5 and 3 print fizzbuzz

def fizz_buzz():
        
        for x in range(1, 101):
                if x % 3 == 0 and x % 5 == 0:
                        print("FIZZBUZZ")
                elif x % 3 == 0:
                        print("FIZZ")
                elif x % 5 == 0:
                        print("BUZZ")
                else:
                        print(x)

fizz_buzz()
