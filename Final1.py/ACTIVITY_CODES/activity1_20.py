import os


def activity_intro():
    while True:
        print("\n\t\t\t\t\t===============================================")
        print("\t\t\t\t\t|                ACTIVITIES MENU               |")
        print("\t\t\t\t\t===============================================\n")
        print("\t\t\t\t\t|   1. Activity          |   2. Activity       |")
        print("\t\t\t\t\t|   3. Activity          |   4. Activity       |")
        print("\t\t\t\t\t|   5. Activity          |   6. Activity       |")
        print("\t\t\t\t\t|   7. Activity          |   8. Activity       |")
        print("\t\t\t\t\t|   9. Activity          |  10. Activity       |")
        print("\t\t\t\t\t|  11. Activity          |  12. Activity       |")
        print("\t\t\t\t\t|  13. Activity          |  14. Activity       |")
        print("\t\t\t\t\t|  15. Activity          |  16. Activity       |")
        print("\t\t\t\t\t|  17. Activity          |  18. Activity       |")
        print("\t\t\t\t\t|  19. Activity          |  20. Activity       |")
        print("\t\t\t\t\t|----------------------------------------------|")
        print("\t\t\t\t\t|                  0. Return                   |")
        print("\t\t\t\t\t===============================================\n")
        user = str(input("\t\t\t\t\tENTER A NUMBER: "))
        print("\n=========================\n")

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
    print("\n\t\t\t\t\t========================== ACTIVITY 1 ==========================\n")
    print("""\n
        \t\t\t\t\t\t==========TYPING TEST SCORE==========
        \t\t\t\t\t\tt5 Minutes Typing Test: Score
        \t\t\t\t\t\t43 WPM is with 91% ACCURACY\n""")


#-----------------------------------------------------------------------------------------------------------------------                    
#----------------------------------------------------- ACTIVITY 2 ------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------


def activity2():
    print("\n\t\t\t\t\t========================== ACTIVITY 2 ==========================\n")
    neme = input("\t\t\t\t\tPease input a name ---->")
    print(f"\t\t\t\t\tHi {neme} \n")


#-----------------------------------------------------------------------------------------------------------------------                    
#----------------------------------------------------- ACTIVITY 3 ------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------


def activity3():
    print("\n\t\t\t\t\t========================== ACTIVITY 3 ==========================\n")
    name = input("\t\t\t\t\tWhat is your name: ")
    age = input("\t\t\t\t\tHow old are you: ")
    email = input("\t\t\t\t\tWhat is your email: ")
    bday = input("\t\t\t\t\tWhen is your Birthday: ")
    add = input("\t\t\t\t\tEnter your Address: ")
    disc = input("\t\t\t\t\tEnter other description: ")

    print(f"\n\t\t\t\t\tMy name is {name} and I am {age} yrs old. I was born in {bday} And I am from {add}. This is my Email {email}. Other Description: {disc}.\n")
    

#-----------------------------------------------------------------------------------------------------------------------                    
#----------------------------------------------------- ACTIVITY 4 ------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------


def activity4():
    print("\n\t\t\t\t\t========================== ACTIVITY 4 ==========================\n")
    number1 = eval(input("\t\t\t\t\tInput first number here > "))
    number2 = eval(input("\t\t\t\t\tInput 2nd number here > "))
    print(type(number1))
    print(type(number2))
    calc = number1 + number2
    minus = number1 - number2
    product = number1 * number2
    quotient = number1 / number2
    exponent = number1 ** number2
    remainder = number1 % number2
    fdivision = number1 // number2
    print("\n\t\t\t\t\tThe sum of" , number1 , "and" , number2 , "is" , calc)
    print("\t\t\t\t\tThe difference of" , number1 , "and" , number2 , "is" , minus)
    print("\t\t\t\t\tThe product of" , number1 , "and" , number2 , "is" , product)
    print("\t\t\t\t\tThe quotient of" , number1 , "and" , number2 , "is" , quotient)
    print(f"\t\t\t\t\t{number1} , exponent by , {number2} , is , {exponent}")
    print("\t\t\t\t\tThe remainder of" , number1 , "and" , number2 , "is" , remainder)
    print("\t\t\t\t\tThe floor division of" , number1 , "and" , number2 , "is" , fdivision, "\n" ,)


#-----------------------------------------------------------------------------------------------------------------------                    
#----------------------------------------------------- ACTIVITY 5 ------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------


def activity5():
    print("\n\t\t\t\t\t========================== ACTIVITY 5 ==========================\n")
    temp = int(input("\t\t\t\t\tEnter temperature in Fahrenheit: "))
    cel = (temp - 32) * 5 / 9
    cel_r = round(cel, 2)
    print(f"\n\t\t\t\t\tThe conversion of  {temp} degrees Fahrenhet is {cel_r} degrees celsius.\n")


#-----------------------------------------------------------------------------------------------------------------------                    
#----------------------------------------------------- ACTIVITY 6 ------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------


def activity6():
    print("\n\t\t\t\t\t========================== ACTIVITY 6 ==========================\n")
    x = 5
    print(f"\t\t\t\t\t{x}")
    x = x + 10
    print(f"\t\t\t\t\t{x}")
    x = x + 15
    print(f"\t\t\t\t\t{x}")
    x = x + 20
    print(f"\t\t\t\t\t{x}")
    x = x + 25
    print(f"\t\t\t\t\t{x}\n")


#-----------------------------------------------------------------------------------------------------------------------                    
#----------------------------------------------------- ACTIVITY 7 ------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------

def activity7():
    print("\n\t\t\t\t\t========================== ACTIVITY 7 ==========================\n")
    miner = str(input("\t\t\t\t\tEnter you name: "))
    mined = str(input("\t\t\t\t\tDid you mine gold today (yes/no) : "))
    gold = 0
    if mined.lower() == "yes":
        gold += 1
        print(f"\t\t\t\t\tYour total mined today is {gold} gold\n")
    elif mined.lower() == "no":
        print(f"\t\t\t\t\tYou havent mined a gold today\n")
    else:
        print("\t\t\t\t\tInvalid error\n")


#-----------------------------------------------------------------------------------------------------------------------                    
#----------------------------------------------------- ACTIVITY 8 ------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------

def activity8():
    print("\n\t\t\t\t\t========================== ACTIVITY 8 ==========================\n")
    passcode= input("\t\t\t\t\tEnter passkey >>> ") 
    if passcode.lower() == "hi":
        print("\t\t\t\t\tHi")
        print("\t\t\t\t\tLove ya too, mwaa\n")
    else:
        print("\t\t\t\t\twrong passkey!!")
        print("""\t\t\t\t\tHint: HI yung password\n""")

#-----------------------------------------------------------------------------------------------------------------------                    
#----------------------------------------------------- ACTIVITY 9 ------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------

def activity9():
    print("\n\t\t\t\t\t========================== ACTIVITY 9 ==========================\n")
    age = int(input("\t\t\t\t\tEnter your age: "))
    if age <= 1:
        print("\t\t\t\t\tYou are a Toddler\n")
    elif age <= 8:
        print("\t\t\t\t\tYou are a Pre-teen\n")
    elif age <= 14: 
        print("\t\t\t\t\tYou are Teenager\n")
    elif age <= 19:
        print("\t\t\t\t\tYou are in Early adulthood\n")
    elif age <= 32:
        print("\t\t\t\t\tYou are in Mid adulthood\n")
    elif age <= 46:
        print("\t\t\t\t\tYou are in Post adulthood\n")
    elif age >= 60:
        print("\t\t\t\t\tYou are in your Senior\n")
    else:
        print("\t\t\t\t\tInvalid syntax\n")


#-----------------------------------------------------------------------------------------------------------------------                    
#----------------------------------------------------- ACTIVITY 10 -----------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------

def activity10():
    print("\n\t\t\t\t\t========================== ACTIVITY 10 ==========================\n")
    dll = str(input("\t\t\t\t\tAre you a current student from DLL? (yes/no): "))
    if dll.lower() == "yes":
        print("\n\t\t\t\t\tWelcome to DLL BSIT scholarship\n")
        location = str(input("\t\t\t\t\tAre from Barangay 9 (yes/no): "))
        if location.lower() == "yes":
            print("\t\t\t\t\tPlease fill up the additional information")
            year = str(input("\t\t\t\t\tWhat is your current year in DLL (f = freshmen)(p = sophomore)(j = Junior)(s = senior): "))
            if year.lower() == "f":
                print("\t\t\t\t\tHi Freshmen")
            elif year.lower() == "p":
                print("\t\t\t\t\tHi sophomore")
            elif year.lower() == "j":
                print("\t\t\t\t\tHi junior")
            elif year.lower() == "s":
                print("\t\t\t\t\tHi senior")
            else:
                print("\t\t\t\t\tInvalid choice")
            choice = str(input("\t\t\t\t\tDo you need scholarship (yes/no): "))
            if choice.lower() == "yes":
                print("\t\t\t\t\tYou been granted a scholarship\n")
            else:
                print("\t\t\t\t\tYou choose no (meaning you dont need scholarship\n)")
        else:
            print("\t\t\t\t\tInvalid location\n")
    else:
        print("\t\t\t\t\tInvalid choice in location\n")


#-----------------------------------------------------------------------------------------------------------------------                    
#----------------------------------------------------- ACTIVITY 11 -----------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------

def activity11():
    print("\n\t\t\t\t\t========================== ACTIVITY 11 ==========================\n")
    for repeat in range (1,11):
        print("\t\t\t\t\tHello World\n")
    

#-----------------------------------------------------------------------------------------------------------------------                    
#----------------------------------------------------- ACTIVITY 12 -----------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------

def activity12():
    print("\n\t\t\t\t\t========================== ACTIVITY 12 ==========================\n")
    for x in range(10, 1, -1):
        print(f"\t\t\t\t\t{x}\n")

#-----------------------------------------------------------------------------------------------------------------------                    
#----------------------------------------------------- ACTIVITY 13 -----------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------

def activity13():
    print("\n\t\t\t\t\t========================== ACTIVITY 13 ==========================\n")
    number = int(input("\t\t\t\t\tEnter any number: "))
    factorial = 1
    for fact in range(number, 0, -1):
        factorial *= fact 
        rounded = round(factorial, 2)
    print(f"\t\t\t\t\tThe factorial of {rounded}\n")

#-----------------------------------------------------------------------------------------------------------------------                    
#----------------------------------------------------- ACTIVITY 14 -----------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------

def activity14():
    print("\n\t\t\t\t\t========================== ACTIVITY 14 ==========================\n")
    for x in range(1,11, 5):
        print(x, end="3")
    print("\t\t\t\t\tHello World", end=" - ")
    print("\t\t\t\t\tBSIT 1C\n")

    for x in range(1,11):
        print(x, end=" ")
        for y in range(1, 11):
            print("*", end = " ")
        print()


#-----------------------------------------------------------------------------------------------------------------------                    
#----------------------------------------------------- ACTIVITY 15 -----------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------

def activity15():
    print("\n\t\t\t\t\t========================== ACTIVITY 15 ==========================\n")
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
    print("\n\t\t\t\t\t========================== ACTIVITY 16 ==========================\n")
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
    print("\n\t\t\t\t\t========================== ACTIVITY 17 ==========================\n")
    elu = int(input("\t\t\t\t\tEnter a number: "))
    for x in range(1,11):
        for y in range(1, elu + 1):
            print(f"   {x} x {y} = {x*y}", end=" ")
        print() 
    

#-----------------------------------------------------------------------------------------------------------------------                    
#----------------------------------------------------- ACTIVITY 18 -----------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------

def activity18():
    print("\n\t\t\t\t\t========================== ACTIVITY 18 ==========================\n")
    eluh = int(input("\t\t\t\t\tEnter a number: "))
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
    print("\n\t\t\t\t\t========================== ACTIVITY 19 ==========================\n")
    elumbs = True
    while elumbs == True:
        name = str(input("\t\t\t\t\tDo you enter name (yes/ no): "))
        if name.lower() == "no":
            print("\t\t\t\t\tprogram terminated\n")
            break
        else:
            continue

#-----------------------------------------------------------------------------------------------------------------------                    
#----------------------------------------------------- ACTIVITY 20 -----------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------

def activity20():
    print("\n\t\t\t\t\t========================== ACTIVITY 20 ==========================\n")
    condition = True
    num = 0
    while condition == True:
        question = str(input("\t\t\t\t\tDo you want to add triangles (yes/no): "))
        if question.lower() == "no":
            print("\t\t\t\t\tPROGRAM TERMINATED\n")
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

