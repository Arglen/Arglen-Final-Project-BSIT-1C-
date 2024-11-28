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

        #code challenge 3 (STILL NOT DONE) <-----------------------------------------------------------------
        #code challenge 4 (STILL NOT DONE) <-----------------------------------------------------------------
        
        print("\t===== CODE CHALLENGE 5 ======\n")

        name = str(input("Enter your name: "))
        amount = int(input("Enter your amount deposit: "))

        a1 = amount // 1000
        remaining = amount - a1 * 1000

        b1 = remaining // 500
        remaining -= b1 * 500

        c1 = remaining // 200
        remaining -= c1 * 200

        d1 = remaining // 100
        remaining -= d1 * 100

        e1 = remaining // 50
        remaining -= e1 * 50

        f1 = remaining // 20
        remaining -= f1 * 20

        g1 = remaining // 10
        remaining -= g1 * 10

        h1 = remaining // 5
        remaining -= h1 * 5

        i1 = remaining // 1
        remaining -= i1 * 1

        print(f"Hi, {name}, your deposit is:")
        print(f"{a1} - 1000")
        print(f"{b1} - 500")  
        print(f"{c1} - 200")  
        print(f"{d1} - 100")  
        print(f"{e1} - 50")  
        print(f"{f1} - 20")  
        print(f"{g1} - 10")  
        print(f"{h1} - 5")  
        print(f"{i1} - 1\n")  

        welcome = str(input("\t     TYPE (YES) TO CONTINUE: "))
        if welcome == "yes":
            print("\n")
        os.system('cls')

        print("\t===== CODE CHALLENGE 6 ======\n")


        prelim = int(input("Enter your grade in prelim: "))
        midterm = int(input("Enter your grade in midterm: "))
        semi = int(input("Enter your grade in semifinal: "))
        final = int(input("Enter your grade in final: "))
        quiz = int(input("Enter your grade in quiz: "))
        project = int(input("Enter your grade in project: "))

        sem_grade = ((prelim * 0.15) + (midterm * 0.15) + (semi * 0.15) + (final * 0.15) + (quiz * 0.15) + (project * 0.15))
        average = (prelim + midterm + semi + final + quiz + project) / 6
        round_ave = (round(average, 1))

        if sem_grade >= 75  and sem_grade <= 100:
            print("Congratulations! You passed the course")
            print(f"Your average is {round_ave}")
        elif sem_grade <= 75 and sem_grade >= 100:
            print("Unfornately, You failed the course")
            print(f"Your average is {round_ave}\n")

        else:
            print("You failed the requirements")
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
