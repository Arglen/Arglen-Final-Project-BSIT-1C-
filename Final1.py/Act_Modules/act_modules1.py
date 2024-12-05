import os

def activity_intro():
    while True:
        print("====== ACTIVITIES ====== \n")
        print("\t1. Activity \t\t 2. Activity ")
        print("\t3. Activity \t\t 4. Activity ")
        print("\t5. Activity \t\t 6. Activity ")
        print("\t7. Activity \t\t 8. Activity ")
        print("\t9. Activity \t\t 10. Activity ")
        print("\t11. Activity \t\t 12. Activity ")
        print("\t13. Activity \t\t 14. Activity ")
        print("\t15. Activity \t\t 16. Activity ")
        print("\t17. Activity \t\t 18 Activity ")
        print("\t19. Activity \t\t 20. Activity ")
        print("\t30. Exit\n")
        user = str(input("ENTER A NUMBER: "))
        print("=========================\n")

        os.system('cls')

        if user == "1":
            activity1()
        elif user == "2":
            activity2()
        elif user == "3":
            activity3()
        elif user == "4":
            activity4()
        elif user == "5":
            pass
        elif user == "6":
            pass
        elif user == "7":
            pass
        elif user == "8":
            pass
        elif user == "9":
            pass
        elif user == "10":
            pass
        elif user == "11":
            pass
        elif user == "12":
            pass
        elif user == "13":
            pass
        elif user == "14":
            pass
        elif user == "15":
            pass
        elif user == "16":
            pass
        elif user == "0":  
            print("Return...")
            return
        else:
            print("Invalid option. Please try again.")
            print("=========================\n")

#-----------------------------------------------------------------------------------------------------------------------                    
#----------------------------------------------------- ACTIVITY 1 ------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------


def activity1():
    print("\n\t========================== ACTIVITY 1 ==========================\n")
    print("""\n
        \t==========TYPING TEST SCORE==========
        \t\tt5 Minutes Typing Test: Score
        \t\t43 WPM is with 91% ACCURACY\n""")


#-----------------------------------------------------------------------------------------------------------------------                    
#----------------------------------------------------- ACTIVITY 2 ------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------


def activity2():
    print("\n\t========================== ACTIVITY 2 ==========================\n")
    neme = input("Pease input a name ---->")
    print(f"\tHi {neme} \n")


#-----------------------------------------------------------------------------------------------------------------------                    
#----------------------------------------------------- ACTIVITY 3 ------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------


def activity3():
    print("\n\t========================== ACTIVITY 3 ==========================\n")
    name = input("What is your name: ")
    age = input("How old are you: ")
    email = input("What is your email: ")
    bday = input("When is your Birthday: ")
    add = input("Enter your Address: ")
    disc = input("Enter other description: ")

    print(f"\nMy name is {name} and I am {age} yrs old. I was born in {bday} And I am from {add}. This is my Email {email}. Other Description: {disc}.\n")
    
#-----------------------------------------------------------------------------------------------------------------------                    
#----------------------------------------------------- ACTIVITY 4 ------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------

def activity4():
    print("\n\t========================== ACTIVITY 4 ==========================\n")
    number1 = eval(input("Input first number here > "))
    number2 = eval(input("Input 2nd number here > "))
    print(type(number1))
    print(type(number2))
    calc = number1 + number2
    minus = number1 - number2
    product = number1 * number2
    quotient = number1 / number2
    exponent = number1 ** number2
    remainder = number1 % number2
    fdivision = number1 // number2
    print("\nThe sum of" , number1 , "and" , number2 , "is" , calc)
    print("The difference of" , number1 , "and" , number2 , "is" , minus)
    print("The product of" , number1 , "and" , number2 , "is" , product)
    print("The quotient of" , number1 , "and" , number2 , "is" , quotient)
    print(number1 , "exponent by" , number2 , "is" , exponent)
    print("The remainder of" , number1 , "and" , number2 , "is" , remainder)
    print("The floor division of" , number1 , "and" , number2 , "is" , fdivision)
