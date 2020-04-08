import math

# program below calculates the investment earned over a period of time or bond repayment costs


print("""Choose either 'investment' (1) or 'bond' (2) from the menu below to proceed:

1. Investment     - to calculate the amount of interest you'll earn on an investment
2. Bond           - to calculate the amount you'll have to pay on a home loan
""")


while True:
    try:
        
        choice = input("--> ").replace("1", "investment").replace("2", "bond").lower()
        
        assert (choice in ('investment', 'bond'))       # allows user to select options
    except AssertionError:
        print("Invalid option. Please enter 'investment' or 'bond'")
    else:
        break

print(f"You selected {choice}")


if choice in ('investment', '1'):           # initial loop to get users input for 'investment' option
    while True:
        try:
            invest_amt = float(input("\nPlease enter the deposit amount: \n").
             upper().replace("R", "").replace(", ", "").replace(" ", ""))
            break
        except ValueError:                      # parameter set for incorrect entries
            print("That's not a valid number. Please try again")
    

    while True:
        try:
            interest_rate = float(input("\nPlease enter the interest rate: (Only enter the number): \n").   
             replace("%", "").replace(", ", "").replace(" ", ""))
            break
        except ValueError:
            print("That's not a valid number. Please try again")
    
    interest_rate = interest_rate/100       # formula to calculate interest rate

    while True:
        try:
            invest_period = int(input(f"\nHow many years do you will be investing for: \n"))
            break
        except ValueError:
            print("That's not a valid number. Please try again (full years only, no decimals).")


    while True:
        try:
            interest = str(input(f"\nPlease enter 'simple' (1) or 'compound' (2) interest. \n").
             replace("1", "simple").replace("2", "compound").lower())
            assert (interest in ('simple', 'compound'))                      # Allows user to select "simple" or "compound" interest option
        except AssertionError:
            print("Invalid option. Please enter 'simple' or 'compound'.")
        else:
            break
    print(f"You've entered {interest} interest.")

    simple_calc =  invest_amt*(1+interest_rate*invest_period)                  #Simple interest calculation
    compound_calc =  invest_amt* math.pow((1+interest_rate), invest_period)    #Compound interest calculation

    if interest == 'simple':
        final_amt = simple_calc
        

    else:   
        final_amt = compound_calc
    
    print(f"Final Investment Value: R{final_amt}")
    
    

else:               # second loop to accomodate the 'bond' option selected
    while True:
        try:
            current_value = float(input("\nPlease enter the present value of the house? \n").       
             upper().replace("R", "").replace(", ", "").replace(" ", ""))
            break
        except ValueError:
            print("That's not a valid number. Please try again")

    while True:
        try:
            int_rate = float(input("\nPlease enter the interest rate: (Only enter in the number):\n").
             replace("%", "").replace(", ", "").replace(" ", ""))
            break
        except ValueError:
            print("That's not a valid number. Please try again")
    
    int_rate = int_rate/100/12      # bond interest rate calculation

    
    while True:
        try:
            
            term = int(input(f"\nPlease enter the number of months you will be investing for: \n"))
            if term%12 == 0:
                term2 = str(int(term/12)) + " years"
            else:
                term2 = str(math.floor(term/12)) + " years and " + str(term%12) + " months"
            break
        except ValueError:
            
            print("That's not a valid number. Please try again (full months only, no decimals).")
          

    repay = (int_rate/(1-math.pow((1+(int_rate)), -term)))*current_value        # repayment formula 
    
    print(f"Your monthly repayment amount will be: R{repay}")
