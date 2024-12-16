import os


def activity24(number):
    fact = 1
    for x in range(number, 0, -1):
        fact *= x

    print("\n\t========================== ACTIVITY 24 ==========================\n")
    print(f"\n THE FACTORIAL OF 4 IS : ----> {fact} \n")

def choices():
    while True:
        print("\n\t=====================================")
        print("\t|          ACTIVITIES MENU          |")
        print("\t=====================================\n")
        print("\t21. Activity \t\t 22. Activity ")
        print("\t23. Activity \t\t 24. Activity ")
        print("\t25. Activity")
        print("\t0. Return\n")
        usr = input("ENTER A NUMBER: ")
        os.system('cls')
        if usr == "21":
            activity21()
        elif usr == "22":
            activity22()
        elif usr == "23":
            print("\n\t========================== ACTIVITY 23 ==========================\n")
            print("\n\tTHE ACTIVITY 23 iS A BODY PROGRAM OF THE ACTIVITY 24, IN WHICH I CANNOT SHOW THE FUNCTION PRGORAM\n")
        elif usr == "24":
            activity24(4)
        elif usr == "25":
            activity25()
        elif usr == "0":  
            print("Return...\n")
            return
        else:
            print("invalid input\n")

#-----------------------------------------------------------------------------------------------------------------------                    
#----------------------------------------------------- ACTIVITY 21 -----------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------

def activity21():
    print("\n\t========================== ACTIVITY 21 ==========================\n")
    tuloy = True
    nameno = 0
    while tuloy == True:
        name = input("Enter a name: ")
        

        if name.lower()=="stop":
            print("Okay tama na\n")
            print(f"You have entered a total of {nameno} names!")
            break

        else:
            print("type 'stop' if you want to terminate the program\n")
            nameno += 1
            continue

#-----------------------------------------------------------------------------------------------------------------------                    
#----------------------------------------------------- ACTIVITY 22 -----------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------

def activity22():
    print("\n\t========================== ACTIVITY 22 ==========================\n")
    print("""\tTHIST PART OF ACTIVITY IS THE COMPILATION OF THE ALL THE ACTIVITIES,\n\tWHERE SIR LEONARD DEMONSTRATE THE USE OF DEFINITION:
          \n\tEXAMPLE: 
          \t def activity1():
          \t    pass
          \t def activity2():
          \t    pass """)

#-----------------------------------------------------------------------------------------------------------------------                    
#----------------------------------------------------- ACTIVITY 23 -----------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------

# def activity23(number):
#     number = 0
#     print("\n\t========================== ACTIVITY 23 ==========================\n")
#     fact = 1
#     for x in range(number, 0 , -1):
#         fact *= 1
#     return fact



#-----------------------------------------------------------------------------------------------------------------------                    
#----------------------------------------------------- ACTIVITY 25 -----------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------

def activity25():
    print("\n\t========================== ACTIVITY 25 ==========================\n")
    #LIST
    #fruits1 = "apple"
    #fruits2 = "banana"
    #fruits3 = "orange"
    #fruits4 = "star apple"
    #fruits5 = "guyabano"
    fruits = ["apples", "banana", "orange", "star apple", "guyabano"]
    print(f"\n\t{fruits}")
    print(f"\n\tMy favorite childhood fruit is {fruits[3]}")
    fruits.append("longgan")
    print(f"\n\t{fruits}")


        
