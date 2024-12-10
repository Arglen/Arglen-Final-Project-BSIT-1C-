import os


def activity_intro():
    while True:
        print("\t====== ACTIVITIES ====== \n")
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
        print("\t0. Return\n")
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
            activity5()
        elif user == "6":
            activity6()
        elif user == "7":
            activity7()
        elif user == "8":
            activity8()
        elif user == "9":
            activity9()
        elif user == "10":
            activity10()
        elif user == "11":
            activity11()
        elif user == "12":
            activity12()
        elif user == "13":
            activity13()
        elif user == "14":
            activity14()
        elif user == "15":
            activity15()
        elif user == "16":
            activity16()
        elif user == "17":
            activity17()
        elif user == "18":
            activity18()
        elif user == "19":
            activity19()
        elif user == "20":
            activity20()
        elif user == "0":  
            print("Return...\n")
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
    print("The floor division of" , number1 , "and" , number2 , "is" , fdivision, "\n" ,)


#-----------------------------------------------------------------------------------------------------------------------                    
#----------------------------------------------------- ACTIVITY 5 ------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------


def activity5():
    print("\n\t========================== ACTIVITY 5 ==========================\n")
    temp = int(input("Enter temperature in Fahrenheit: "))
    cel = (temp - 32) * 5 / 9
    cel_r = round(cel, 2)
    print(f"\nThe conversion of  {temp} degrees Fahrenhet is {cel_r} degrees celsius.\n")


#-----------------------------------------------------------------------------------------------------------------------                    
#----------------------------------------------------- ACTIVITY 6 ------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------


def activity6():
    print("\n\t========================== ACTIVITY 6 ==========================\n")
    x = 5
    print(f"{x}")
    x = x + 10
    print(x)
    x = x + 15
    print(x)
    x = x + 20
    print(x)
    x = x + 25
    print(f"{x}\n")


#-----------------------------------------------------------------------------------------------------------------------                    
#----------------------------------------------------- ACTIVITY 7 ------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------

def activity7():
    print("\n\t========================== ACTIVITY 7 ==========================\n")
    miner = str(input("Enter you name: "))
    mined = str(input("Did you mine gold today (yes/no) : "))
    gold = 0
    if mined.lower() == "yes":
        gold += 1
        print(f" Your total mined today is {gold} gold\n")
    elif mined.lower() == "no":
        print(f" You havent mined a gold today\n")
    else:
        print("Invalid error\n")


#-----------------------------------------------------------------------------------------------------------------------                    
#----------------------------------------------------- ACTIVITY 8 ------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------

def activity8():
    print("\n\t========================== ACTIVITY 8 ==========================\n")
    passcode= input("Enter passkey >>> ") 
    if passcode.lower() == "hi":
        print("Hi")
        print("Love ya too, mwaa\n")
    else:
        print("wrong passkey!!")
        print("""Hint: HI yung password\n""")

#-----------------------------------------------------------------------------------------------------------------------                    
#----------------------------------------------------- ACTIVITY 9 ------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------

def activity9():
    print("\n\t========================== ACTIVITY 9 ==========================\n")
    age = int(input("Enter your age: "))
    if age <= 1:
        print("You are a Toddler\n")
    elif age <= 8:
        print("You are a Pre-teen\n")
    elif age <= 14: 
        print("You are Teenager\n")
    elif age <= 19:
        print("You are in Early adulthood\n")
    elif age <= 32:
        print("You are in Mid adulthood\n")
    elif age <= 46:
        print("You are in Post adulthood\n")
    elif age >= 60:
        print("You are in your Senior\n")
    else:
        print("Invalid syntax\n")


#-----------------------------------------------------------------------------------------------------------------------                    
#----------------------------------------------------- ACTIVITY 10 -----------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------

def activity10():
    print("\n\t========================== ACTIVITY 10 ==========================\n")
    dll = str(input("Are you a current student from DLL? (yes/no): "))
    if dll.lower() == "yes":
        print("\n\tWelcome to DLL BSIT scholarship\n")
        location = str(input("Are from Barangay 9 (yes/no): "))
        if location.lower() == "yes":
            print("Please fill up the additional information")
            year = str(input("What is your current year in DLL (f = freshmen)(p = sophomore)(j = Junior)(s = senior): "))
            if year.lower() == "f":
                print("Hi Freshmen")
            elif year.lower() == "p":
                print("Hi sophomore")
            elif year.lower() == "j":
                print("Hi junior")
            elif year.lower() == "s":
                print("Hi senior")
            else:
                print("Invalid choice")
            choice = str(input("Do you need scholarship (yes/no): "))
            if choice.lower() == "yes":
                print("You been granted a scholarship\n")
            else:
                print("You choose no (meaning you dont need scholarship\n)")
        else:
            print("Invalid location\n")
    else:
        print("Invalid choice in location\n")


#-----------------------------------------------------------------------------------------------------------------------                    
#----------------------------------------------------- ACTIVITY 11 -----------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------

def activity11():
    print("\n\t========================== ACTIVITY 11 ==========================\n")
    for repeat in range (1,11):
        print("Hello World\n")
    

#-----------------------------------------------------------------------------------------------------------------------                    
#----------------------------------------------------- ACTIVITY 12 -----------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------

def activity12():
    print("\n\t========================== ACTIVITY 12 ==========================\n")
    for x in range(10, 1, -1):
        print(f"{x}\n")

#-----------------------------------------------------------------------------------------------------------------------                    
#----------------------------------------------------- ACTIVITY 13 -----------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------

def activity13():
    print("\n\t========================== ACTIVITY 13 ==========================\n")
    number = int(input("Enter any number: "))
    factorial = 1
    for fact in range(number, 0, -1):
        factorial *= fact 
        rounded = round(factorial, 2)
    print(f"The factorial of {rounded}\n")

#-----------------------------------------------------------------------------------------------------------------------                    
#----------------------------------------------------- ACTIVITY 14 -----------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------

def activity14():
    print("\n\t========================== ACTIVITY 14 ==========================\n")
    for x in range(1,11, 5):
        print(x, end="3")
    print("Hello World", end=" - ")
    print("BSIT 1C\n")

    for x in range(1,11):
        print(x, end=" ")
        for y in range(1, 11):
            print("*", end = " ")
        print()


#-----------------------------------------------------------------------------------------------------------------------                    
#----------------------------------------------------- ACTIVITY 15 -----------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------

def activity15():
    print("\n\t========================== ACTIVITY 15 ==========================\n")
    for x in range(1,11, 5):
        print(x, end=" ")
        for y in range(1, 11):
            print("*", end = " ")
        print("\n")
        print()
    

#-----------------------------------------------------------------------------------------------------------------------                    
#----------------------------------------------------- ACTIVITY 16 -----------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------

def activity16():
    print("\n\t========================== ACTIVITY 16 ==========================\n")
    for x in range(1, 6):
        for y in range(1, x + 1):
            print("  ",end="")
        for z in range(6, y, -1):
            print("^ ",end="")
        for a in range(6, x, -1):
            print("* ",end="")
        for b in range(1, x + 1):
            print(" ",end="")
        print("\n")
    print()


#-----------------------------------------------------------------------------------------------------------------------                    
#----------------------------------------------------- ACTIVITY 17 -----------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------

def activity17():
    print("\n\t========================== ACTIVITY 17 ==========================\n")
    elu = int(input("Enter a number: "))
    for x in range(1,11):
        for y in range(1, elu + 1):
            print(f"{x} x {y} = {x*y}", end="\t")
        print() 
    

#-----------------------------------------------------------------------------------------------------------------------                    
#----------------------------------------------------- ACTIVITY 18 -----------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------

def activity18():
    print("\n\t========================== ACTIVITY 18 ==========================\n")
    eluh = int(input("Enter a number: "))
    for a in range(1,5):
        for x in range(1,eluh +1 ):
            for y in range(1, a + 1):
                print("*", end= " ")

            for z in range(5, a, -1):
                print(" ", end=" ")
        print()

#-----------------------------------------------------------------------------------------------------------------------                    
#----------------------------------------------------- ACTIVITY 19 -----------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------

def activity19():
    print("\n\t========================== ACTIVITY 19 ==========================\n")
    elumbs = True
    while elumbs == True:
        name = str(input("Do you enter name (yes/ no): "))
        if name.lower() == "no":
            print("program terminated\n")
            break
        else:
            continue

#-----------------------------------------------------------------------------------------------------------------------                    
#----------------------------------------------------- ACTIVITY 20 -----------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------

def activity20():
    print("\n\t========================== ACTIVITY 20 ==========================\n")
    condition = True
    num = 0
    while condition == True:
        question = str(input("Do you want to add triangles (yes/no): "))
        if question.lower() == "no":
            print("PROGRAM TERMINATED\n")
            break
        else:
            num += 1
            for a in range(1,5):
                for x in range(1, num+1 ):
                    for y in range(1, a + 1):
                            print("*", end= " ")
                            
                    for z in range(5, a, -1):
                            print(" ", end=" ")
                print()
        continue

