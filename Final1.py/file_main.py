import os
from CODE_CHALLENGES import code_challenges
from ACTIVITY_CODES import activity1_20
from ACTIVITY_21_25 import activity21_25

def main():
    
    while True:
        print("\t\t\t\t\t=========================================================")
        print("\t\t\t\t\t=================== ARGLEN L. ELUMBA ====================")
        print("\t\t\t\t\t=========================================================")
        print("\t\t\t\t\t================== COMPILATION PROJECT ==================")
        print("\t\t\t\t\t=========================================================")
        print("\t\t\t\t\t====|    1. CODE CHALLENGES                         |====")
        print("\t\t\t\t\t====|    2. ACTIVITY 1 - 20                         |====")
        print("\t\t\t\t\t====|    3. ACTIVITY 21 - 25                        |====")
        print("\t\t\t\t\t====|    4. EXIT PROGRAM                            |====")
        print("\t\t\t\t\t=========================================================")
        print("\t\t\t\t\t=========================================================")
        user = str(input("\t\t\t\t\tCHOOSE A NUMBER: "))
        os.system('cls')
        if user == "1":
            code_challenges.intro_code_challenge()

        elif user == "2":
            activity1_20.activity_intro()
        
        elif user == "3":
            activity21_25.choices()

        elif user == "4":  
            exit()

        else:
            print("Invalid option. Please try again.")

main()
