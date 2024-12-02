import os
from Modules import modules1

def main():
    while True:
        modules1.picking()
        user = str(input("CHOOSE A NUMBER: "))
        
        if user == "1":
            modules1.intro_code_challenge()
            user = str(input("ENTER A NUMBER: "))

            if user == "1":
                modules1.code_challenge1()
            elif user == "2":
                modules1.code_challenge2()
            #code_challenge 3
            elif user == "4":
                modules1.code_challenge4()
            elif user == "5":
                modules1.code_challenge5()
            elif user == "6":
                modules1.code_challenge6()
            elif user == "7":
                modules1.code_challenge7()
            elif user == "8":
                modules1.code_challenge8()
            #code challenge 91\1
            
            elif user == "0":  
                print("Exiting the program...")
                break
            else:
                print("Invalid option. Please try again.")

        elif user == "0":  
            print("Exiting the program...")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()