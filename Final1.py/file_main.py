import os
from CODE_CHALLENGES import modules1
from ACTIVITY_CODES import act_modules1
from ACTIVITY_21_25 import choice23


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
            modules1.intro_code_challenge()

        elif user == "2":
            act_modules1.activity_intro()
        
        elif user == "3":
            choice23.choices()

        elif user == "4":  
            exit()

        else:
            print("Invalid option. Please try again.")

main()
