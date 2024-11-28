import os
def code_challenge():
    pass

def activities():
    pass

def part0():
    print("""========= WELCOME TO MY COMPILATION PROJECT ========= \n""")
    welcome = str(input("\t     TYPE (YES) TO CONTINUE: "))
    if welcome == "yes":
        print("\n")
    os.system('cls')

def part1():
    print(""" \t\n=============| ARGLEN L. ELUMBA |============\t\n============| COMPILATION PROJECT |============ \n""")
    print("1. Code Challenges")
    print("2. Acivities \n")
    print("")
    user = str(input("Please Choose a number: "))

    if user == "1": 
        print("\t===== CODE CHALLENGE 1 ======\n")
        name = str(input("What is your first name: "))

        print("""

        \n\n\n\n

        \t\t\t\t\t\t\t\t\t\t*
        \t\t\t\t\t\t\t\t\t*\t*\t*
        \t\t\t\t\t\t\t\t*\t*\t*\t*\t*
        \t\t\t\t\t\t\t\t\t*\t*\t*
        \t\t\t\t\t\t\t\t\t\t*

        """)
        welcome = str(input("\t     TYPE (YES) TO CONTINUE: "))
        if welcome == "yes":
            print("\n")
        os.system('cls')

        print("\t===== CODE CHALLENGE 2 ======\n")
        name = str(input("What is your first name: "))

        print("""

        \n\n\n\n

        \t\t\t\t\t\t\t\t\t\t*
        \t\t\t\t\t\t\t\t\t*\t*\t*
        \t\t\t\t\t\t\t\t*\t*\t*\t*\t*
        \t\t\t\t\t\t\t*\t*\t*""", name ,"""\t*\t*\t*
        \t\t\t\t\t\t\t\t*\t*\t*\t*\t*
        \t\t\t\t\t\t\t\t\t*\t*\t*
        \t\t\t\t\t\t\t\t\t\t*

        \n""")

        welcome = str(input("\t     TYPE (YES) TO CONTINUE: "))
        if welcome == "yes":
            print("\n")
        os.system('cls')
	
        
    elif user == "2":
        print("\t===== ACTIVITY 1 ======")
        print("MY FIRST PROGRAM\n")
        welcome = str(input("\t     TYPE (YES) TO CONTINUE: "))
        if welcome == "yes":
            print("\n")
        os.system('cls')

        print("\t===== ACTIVITY 2 ======")
        print("""\n Arglen L. Elumba\n Arglen L. Elumba\n Arglen L. Elumba\n Arglen L. Elumba\n Arglen L. Elumba\n Arglen L. Elumba\n Arglen L. Elumba\n Arglen L. Elumba\n Arglen L. Elumba\n Arglen L. Elumba\n""")
        welcome = str(input("\t     TYPE (YES) TO CONTINUE: "))
        if welcome == "yes":
            print("\n")
        os.system('cls')
        pass

    else:
        pass
 

part0()
part1()
