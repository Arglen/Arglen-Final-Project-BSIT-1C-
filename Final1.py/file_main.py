import os
from Modules import modules1

def main():
    
    while True:
        print(""" \t\n=============| ARGLEN L. ELUMBA |============\t\n============| COMPILATION PROJECT |============ \n""")
        print("1. Code Challenges")
        print("2. Acivities ")
        print("3. Exit Program")
        user = str(input("CHOOSE A NUMBER: "))
            
        if user == "1":
            modules1.intro_code_challenge()

        elif user == "2":
            pass

        elif user == "3":  
            exit()

        else:
            print("Invalid option. Please try again.")

main()
