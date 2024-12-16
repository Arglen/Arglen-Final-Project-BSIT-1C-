import os

def intro_code_challenge():
    while True:
        print("\n\t=====================================")
        print("\t|          CODE CHALENGE MENU        |")
        print("\t=====================================\n")
        print("1. Code Challenge ")
        print("2. Code Challenge ")
        print("3. Code Challenge ")
        print("4. Code Challenge ")
        print("5. Code Challenge ")
        print("6. Code Challenge ")
        print("7. Code Challenge ")
        print("8. Code Challenge ")
        print("9. Code Challenge ")
        print("10.Code Challenge ")
        print("11.Code Challenge ")
        print("12.Code Challenge ")
        print("13.Code Challenge ")
        print("14.Code Challenge ")
        print("15.Code Challenge ")
        print("16.Code Challenge ")
        print("0. Return\n")
        user = str(input("ENTER A NUMBER: "))
        print("=========================\n")

        os.system('cls')

        if user == "1":
            code_challenge1()
        elif user == "2":
            code_challenge2()
        elif user == "3":
            code_challenge3()
        elif user == "4":
            code_challenge4()
        elif user == "5":
            code_challenge5()
        elif user == "6":
            code_challenge6()
        elif user == "7":
            code_challenge7()
        elif user == "8":
            code_challenge8()
        elif user == "9":
            code_challenge9()
        elif user == "10":
            code_challenge10()
        elif user == "11":
            code_challenge11()
        elif user == "12":
            code_challenge12()
        elif user == "13":
            code_challenge13()
        elif user == "14":
            code_challenge14()
        elif user == "15":
            code_challenge15()
        elif user == "16":
            Code16()

        elif user == "0":  
            print("Return...")
            return
        else:
            print("Invalid option. Please try again.")
            print("=========================\n")



#-----------------------------------------------------------------------------------------------------------------------                    
#----------------------------------------------- CODE CHALLENGE 1 ------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------

def code_challenge1():
    print("""
          
    \t\t\t\t\t\t\t\t===== CODE CHALLENGE 1 ======
          
    \n\n\n\n

    \t\t\t\t\t\t\t\t\t\t*
    \t\t\t\t\t\t\t\t\t*\t*\t*
    \t\t\t\t\t\t\t\t*\t*\t*\t*\t*
    \t\t\t\t\t\t\t\t\t*\t*\t*
    \t\t\t\t\t\t\t\t\t\t*

    \n""")
    
#-----------------------------------------------------------------------------------------------------------------------                    
#----------------------------------------------- CODE CHALLENGE 2 ------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------
def code_challenge2():
    print("\t\t\t\t\t\t\t\t===== CODE CHALLENGE 2 ======")
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

#-----------------------------------------------------------------------------------------------------------------------                    
#----------------------------------------------- CODE CHALLENGE 3 ------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------


#ELUMBA, ARGLEN L.
#BSIT - 1C
# ================PERSONAL DATA===================
def code_challenge3():
    first_name = str(input("First Name : "))
    surname = str(input("Last Name : "))
    m_initial = str(input("Middle Initial : "))
    age = int(input("Age: "))
    address = str(input("Permanent Address : "))
    plc_birth = str(input("Place of Birth : "))
    gender = str(input("Gender M/F: "))
    religion = str(input("Religion : "))
    height = int(input("Height(cm): "))
    weight = int(input("Weight(kg) : "))

    #==================FAMILY BACKGROUND====================

    f_n = str(input("Father's Fullname : "))
    o = str(input("Occupation : "))
    p_n = int(input("Phone Number : "))

    m_n = str(input("Mother's Fullname : "))
    o = str(input("Occupation : "))
    p_n = int(input("Phone Number : "))

    #=====================BIO-DATA==========================

    print(f" \n\t\t\t BIO DATA \n\n \t\t\tPERSONAL BACKGROUND \n\n Fullname: {first_name} {m_initial} {surname} \n Age: {age} \n Permanent Address: {address} \n Place of Birth: {plc_birth} \n Gender: {gender} \n Religion: {religion} \n Height: {height} \n Weight: {weight} \n")
    print(f" \n\t\t\t Family Background \n Father's Name: {f_n} \n Occupation: {o} \n Phone Number: {p_n} \n")
    print(f" Mother's Name: {m_n} \n Occupation: {o} \n Phone Number: {p_n} \n")


#-----------------------------------------------------------------------------------------------------------------------                    
#----------------------------------------------- CODE CHALLENGE 4 ------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------

def code_challenge4():

    number1 = int(input("Enter a number: "))
    number2 = int(input("Enter another number: "))

    sum = number1 + number2
    minus = number1 - number2
    mlt = number1 * number2
    dvd = number1 / number2
    expo = number1 ** number2
    mod = number1 % number2 
    fl_dvd = number1 // number2
    rounded = (round(expo, 2))

    print(f"The sum of {number1} and {number2} is : {sum}")
    print(f"The difference of {number1} and {number2} is : {minus}")
    print(f"The product of {number1} and {number2} is : {mlt}")
    print(f"The quotient of {number1} and {number2} is : {dvd}")
    print(f"The exponent of {number1} by {number2} is : {rounded}")
    print(f"The flood division of {number1} and {number2} is : {fl_dvd}")


#-----------------------------------------------------------------------------------------------------------------------                    
#----------------------------------------------- CODE CHALLENGE 5 ------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------

def code_challenge5():
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

#-----------------------------------------------------------------------------------------------------------------------                    
#----------------------------------------------- CODE CHALLENGE 6 ------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------

def code_challenge6():
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
        print(f"Your average is {round_ave}")

    else:
        print("You failed the requirements")

#-----------------------------------------------------------------------------------------------------------------------                    
#----------------------------------------------- CODE CHALLENGE 7 ------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------

def code_challenge7():
    grocery = str(input("Di you buy a grocery (yes/no): "))
    name = str(input("What is your name: "))

    chicken = 200.00
    pork = 250.00
    beef = 300.00

    if grocery.lower() == "yes":
        print("\n What is the purchase item: \n [chicken = CHICKEN TENDER] \n [pork = PORK TENDER] \n [beef = BEEF TENDER] \n")
        pruchase_item = str(input("Name of the item: ")) 
        addons = str(input("Would you like to add more (yes/no)"))  
        customer_age = int(input("Enter your age: "))
        
        if pruchase_item.lower() == "chicken":
            print(f"The price of the item is {chicken} \n")
            amount = int(input("Enter your amount money: "))

            tax = chicken * 0.123
            total_price = chicken + tax
            
            if customer_age >= 60:
                print("You have a senior discount if 5.2% ")
                discount = 0.052 * total_price
                discount_price = total_price - discount
                change_discount = amount - discount_price
                rounded = (round(change_discount, 2))
                print(f"You change is {rounded}")
                print(f"\nHi customer, you purchased CHICKEN TENDER,\n with a price of {chicken} plus 12.3% \n and minus 5.2% for senior discount \n total of: {chicken} \n Amount given: {amount} \n Change: {rounded}")

            elif customer_age <= 60:
                change = amount - total_price
                print(f"Your change is {change} with 12.3% tax")
                print(f"\nHi customer, you purchased CHICKEN TENDER, with a price of {chicken} plus 12.3% \n total of: {chicken} \n Amount given: {amount} \n Change: {change} ")
            else:
                print("Invalid purchase")
        
        elif pruchase_item.lower() == "pork":
            print(f"The price of the item is {pork}")
            amount = int(input("Enter your amount money: "))

            tax = pork * 0.123
            total_price = pork + tax

            if customer_age >= 60:
                print("You have a senior discount if 5.2% ")
                discount = 0.052 * pork
                discount_price = pork - discount
                change_discount = amount - discount_price
                rounded = (round(change_discount, 2))
                print(f"You change is {change_discount}")
                print(f"\nHi customer, you purchased CHICKEN TENDER, with a price of {pork} plus 12.3% and minus 5.2% for senior discount \n total of: {pork} \n Amount given: {amount} \n Change: {rounded}")

            elif customer_age <= 60:
                change = amount - total_price
                print(f"Your change is {change}")
                print(f"\nHi customer, you purchased CHICKEN TENDER, with a price of {pork} plus 12.3% \n total of: {pork} \n Amount given: {amount} \n Change: {change} ")

            else:
                print("Invalid purchase")

        elif pruchase_item.lower() == "beef":
            print(f"The price of the item is {beef}")
            amount = int(input("Enter your amount money: "))

            tax = beef * 0.123
            total_price = beef + tax

            if customer_age >= 60:
                print("You have a senior discount if 5.2% ")
                discount = 0.052 * beef  
                discount_price = beef - discount
                change_discount = amount - discount_price
                rounded = (round(change_discount, 2))   
                print(f"You change is {change_discount}")
                print(f"\nHi customer, you purchased CHICKEN TENDER, with a price of {beef} plus 12.3% and minus 5.2% for senior discount \n total of: {beef} \n Amount given: {amount} \n Change: {rounded} ")

            elif customer_age <= 60:
                change = amount - total_price
                print(f"Your change is {change}")
                print(f"\nHi customer, you purchased CHICKEN TENDER, with a price of {beef} plus 12.3% \n total of: {beef} \n Amount given: {amount} \n Change: {change} ")

            else:
                print("Invalid purchase")
        else:
            print("invalid purchase")
    else:
        ("invalid purchase1")

#-----------------------------------------------------------------------------------------------------------------------                    
#----------------------------------------------- CODE CHALLENGE 8 ------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------

def code_challenge8():
    odd = 0
    even = 0
    sum = 0
    for x in range (1,11):
        number = eval(input(f"Proceed with number ({x}): "))
        print(x, "=", number)
        sum += number
        if odd % 2 == 0:
            odd += number
            
        else:
            even += number
        print("\tTotal Odd", odd)
        print("\tTotal Even", even)
        print("\tTotal", sum)

#-----------------------------------------------------------------------------------------------------------------------                    
#----------------------------------------------- CODE CHALLENGE 9 ------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------

def code_challenge9():
    set = eval(input("put number: "))

    for x in range(set,0,-1):
        for y in range(set,x,-1):
            print("  ",end="")
        print(" *" * x )

#-----------------------------------------------------------------------------------------------------------------------                    
#----------------------------------------------- CODE CHALLENGE 10 -----------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------

def code_challenge10():
    for r in range(1,7):
        for i in range(7,r, -1):
            print(" ",end="")
        for j in range(0, r):
            print("*", end="")
        for k in range(r,7, -1):
            print("*", end="")
        for l in range(0,r):
            print("*", end="")
        print()

    for t in range(1,7):
        for x in range(1,t + 1):
            print(" ", end="")
        for y in range(7,t, -1):
            print("*", end="")
        for y in range(7,t, -1):
            print("*", end="")    
        print()

#-----------------------------------------------------------------------------------------------------------------------                    
#----------------------------------------------- CODE CHALLENGE 11 -----------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------

def code_challenge11():
    for a in range(1, 6):
        for b in range(6, a, -1):
            print(" ", end=" ")
        for b in range(0, a):
            print("*", end=" ")
        
        print("    ", end="")  
        
        for c in range(a, 6, -1):
            print("*", end=" ")
        for d in range(2, a):
            print("*", end="  ")
        print()

    print()  

    for x in range(1, 6):
        for y in range(-1, x + 1):
            print(" ", end=" ")
        for z in range(5, x, -1):
            print("*", end=" ")
        
        print("  ", end="")  
        
        for my in range(3, x, -1):
            print("*", end=" ")
        print()

#-----------------------------------------------------------------------------------------------------------------------                    
#----------------------------------------------- CODE CHALLENGE 12 -----------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------

def code_challenge12():
    for a in range(1, 6):
        for b in range(6, a, -1):
            print(" ", end=" ")
        for b in range(0, a):
            print("*", end=" ")
        
        print("", end="")
        
        for d in range(0, a):
            print("*", end=" ")
        print()

    for _ in range(5):
        print("         * * *")
    print()

#-----------------------------------------------------------------------------------------------------------------------                    
#----------------------------------------------- CODE CHALLENGE 13 -----------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------

def code_challenge13():
    for a in range(1, 7):
        for b in range(7, a, -1):
            print(" ", end=" ")
        for b in range(a, 0, -1):
            print(b, end=" ")
        for c in range(2, a + 1):
            print(c, end=" ")
        print()

    for x in range(5, 0, -1):
        for y in range(7, x, -1):
            print(" ", end=" ")
        for z in range(x, 0, -1):
            print(z, end=" ")
        for w in range(2, x + 1):
            print(w, end=" ")
        print()

#-----------------------------------------------------------------------------------------------------------------------                    
#----------------------------------------------- CODE CHALLENGE 14 -----------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------

def code_challenge14():
    tuloy = True
    a = 0
    while tuloy == True:
        number = eval(input("Enter a number [0 to terminate] --->  "))   
        print
        if number == 0:
            print("Program Terminated")
            print(f"The total of the number you enter is {a}")
            break

        else:
            a += number
            continue

#-----------------------------------------------------------------------------------------------------------------------                    
#----------------------------------------------- CODE CHALLENGE 15 -----------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------

def code_challenge15():
    isContinue = True
    no = 0
    while isContinue == True:
        ask = input("Would you like to add another triangle (yes / no )--> ")

        if ask.lower() == "no":
            print("PROGRAM TERMINATED")
            break
            isContinue = False
        elif ask.lower() == "yes":
            os.system('cls')
            no += 1
            for x in range (1, 6):
                for r in range (1 , no + 1):
                    for y in range (1 , x + 1):
                        print("*", end=" ")
                    for z in range (6, x, -1):
                        print(" ",end=" ")
                print()
        else:
            print("INVALID ANSWER it's only (yes/no)")


#-----------------------------------------------------------------------------------------------------------------------                    
#----------------------------------------------- CODE CHALLENGE 16 -----------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------

# BANK SIMULATION PROGRAM
# Create new account
# if account exists, deposit, withdraw, check balance -- function
# if deposit, enter amount, give Filipino denomination breakdown
# if withdraw, you cannot withdraw if balance is lower than withdraw amount
# deposit, ask how much? and show current balance
# continue to repeat the process until user opts out or exits the program, use while loop
# you will create a function that will break down a Filipino denomination and then print it
# Create a Python program that can create banking accounts, with the following information:
# initial deposit, name
# user can also deposit, withdraw, and every deposit program should be able to display the current balance
# program will only terminate if user choose to terminate the program

def Code16():
    denominations = [1000, 500, 200, 100, 50, 20, 10, 5, 1]

    accounts = {}

    def create_account(name, initial_deposit):
        if name in accounts:
            print(f"Account with name '{name}' already exists.")
        else:
            accounts[name] = initial_deposit
            print(f"Account created for '{name}' with an initial deposit of PHP {initial_deposit}.")

    def check_balance(name):
        if name in accounts:
            print(f"Current balance for '{name}': PHP {accounts[name]}")
        else:
            print("Account does not exist.")

    def denomination_breakdown(amount):
        print("Denomination breakdown:")
        for denom in denominations:
            count = amount // denom
            if count > 0:
                print(f"{denom} x {count}")
            amount %= denom

    def deposit(name, amount):
        if name in accounts:
            accounts[name] += amount
            print(f"Deposited PHP {amount} to '{name}'. New balance: PHP {accounts[name]}")
            denomination_breakdown(amount)
        else:
            print("Account does not exist.")

    def withdraw(name, amount):
        if name in accounts:
            if accounts[name] >= amount:
                accounts[name] -= amount
                print(f"Withdrew PHP {amount} from '{name}'. New balance: PHP {accounts[name]}")
            else:
                print("Insufficient balance!")
        else:
            print("Account does not exist.")

    def main():
        while True:
            print("\n--- BANK SIMULATION PROGRAM ---")
            print("1. Create Account")
            print("2. Deposit Money")
            print("3. Withdraw Money")
            print("4. Check Balance")
            print("5. Exit Program")

            choice = input("Choose an option: ")

            if choice == "1":
                name = input("Enter account name: ")
                initial_deposit = eval(input("Enter initial deposit: "))
                create_account(name, initial_deposit)
            elif choice == "2":
                name = input("Enter account name: ")
                amount = eval(input("Enter amount to deposit: "))
                deposit(name, amount)
            elif choice == "3":
                name = input("Enter account name: ")
                amount = eval(input("Enter amount to withdraw: "))
                withdraw(name, amount)
            elif choice == "4":
                name = input("Enter account name: ")
                check_balance(name)
            elif choice == "5":
                print("Thank you for using the Bank Simulation Program. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")
    main()
