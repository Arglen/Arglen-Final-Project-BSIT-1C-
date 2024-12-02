

def picking():
    print(""" \t\n=============| ARGLEN L. ELUMBA |============\t\n============| COMPILATION PROJECT |============ \n""")
    print("1. Code Challenges")
    print("2. Acivities \n")
    
def intro_code_challenge():

    print("=====CODE CHALLENGES===== \n")
    print("1. Code Challenge ")
    print("2. Code Challenge ")
    print("3. Code Challenge ")
    print("4. Code Challenge ")
    print("5. Code Challenge ")
    print("6. Code Challenge ")
    print("7. Code Challenge ")
    print("8. Code Challenge ")
    print("9. Code Challenge ")
    print("10.Code Challenge \n")
    print("0. Exit")
    print("=========================\n")

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
    

def code_challenge2():
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

# def code_challenge 3 <--------------------

# def coode_challenge 4 <-------------------
    
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

#def code_challenge8():
    #pass

#def code_challenge9():
    #pass
