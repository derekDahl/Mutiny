
import random
#menu that will allow user to chose between single player, 2 players, or quitting
def menu():
    while True:
        global choice
        choice = input("Welcome to rock, paper, scissors! \nWould you like 1 or 2 players? \nTo quit enter q: ")
        if choice == "1":
            single_player()
        elif choice == "2":
            two_player()
        elif choice == "q":
            print("Thank you for playing!")
            break
        else:
            print("Invalid input")

def single_player():
    #Declarations of possible inputs and outputs for gameplay
    win = " You win!"
    lose = " You lose!"
    r = "rock"
    p = "paper"
    s = "scissors"
    rps = ["rock", "paper", "scissors"]
    
    while True:
        #p1 is the user, p2 is the cpu
        #randomly chooses words contained in rps
        p2_choice = random.choice(rps)
        statement = "The computer chose " + p2_choice
        p1_choice = input("Enter q to quit... Enter rock, paper, or scissors: ")

        if p1_choice == "q":
            print("Thank you for playing!")
            menu()
            
        #Logic for finding and declaring a winner in each round  
        elif p1_choice == p2_choice:
            print(statement + " It's a tie!")
        elif p1_choice == r and p2_choice == s:
            print(statement + win)
        elif p1_choice == r and p2_choice == p:
            print(statement + lose)
        elif p1_choice == s and p2_choice == p:
            print(statement + win)
        elif p1_choice == s and p2_choice == r:
            print(statement + lose)
        elif p1_choice == p and p2_choice == r:
            print(statement + win)
        elif p1_choice == p and p2_choice == s:
            print(statement + lose)
        else:
            print("Invalid input")

def two_player():

    win = " You win!"
    lose = " You lose!"
    r = "rock"
    p = "paper"
    s = "scissors"
    rps = ["rock", "paper", "scissors"]
    
    while True:
        #Slightly modified for two real players. 
        p1_wins = "PLAYER 1 WINS!"      
        p2_wins = "pLAYER 2 WINS!"
        p1_choice = input("Player 1, Enter q to quit... Enter rock, paper, or scissors: ")
        p2_choice = input("Player 2  Enter q to quit... Enter rock, paper, or scissors: ")
        if p1_choice == "q" or p2_choice == "q":
            print("Thank you for playing!")
            menu()
        elif p1_choice == p2_choice:
            print(" It's a tie!")
        elif p1_choice == r and p2_choice == p:
            print(p2_wins)
        elif p1_choice == r and p2_choice == s:
            print(p1_wins)
        elif p1_choice == s and p2_choice == p:
            print(p1_wins)
        elif p1_choice == s and p2_choice == r:
            print(p2_wins)
        elif p1_choice == p and p2_choice == r:
            print(p1_wins)
        elif p1_choice == p and p2_choice == s:
            print(p2_wins)
        else:
            print("Invalid input") 
    

menu()






