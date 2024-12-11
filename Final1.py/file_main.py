import os
from Modules import modules1
from Act_Modules import act_modules1
from Next_Act23_24 import choice23


def main():
    
    while True:
        print(""" \t\n=============| ARGLEN L. ELUMBA |============\t\n============| COMPILATION PROJECT |============ \n""")
        print("1. Code Challenges")
        print("2. Acivities ")
        print("3. 2ND - Activities (21-25)")
        print("4. Exit\n")
        user = str(input("CHOOSE A NUMBER: "))
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
