# Create a mortgage/car loan calculator that determines the monthly payment 
# assuming that interest is compounded monthly.

# Needed Info:
# - The loan amount
# - The Annual Percentage Rate (APR)
# - The loan duration

# From the above, calcuate:
# - monthly interest rate (APR / 12)
# - loan duration in months

# Python formula:
# m = p * (j / (1 - (1 + j) ** (-n)))

# m = monthly payment
# p = loan amount
# j = monthly interest rate
# n = loan duration in months



# PEDAC

# UNDERSTAND THE PROBLEM

# WRITE A PROGRAM THAT:
# Takes the loan amount, the annual percentage rate (APR), loan 
# duration, and calculates how much the monthly payment will be. 


# INPUTS: 
# - Loan amount
# - APR 
# - Loan duration 


# OUTPUTS:
# - Monthly payment


# EXPLICIT REQUIREMENTS/RULES:
# - Calculate the monthly interest rate

# - Calculate the loan duration in months

# - Use explicit names for the variables in the formula.

# - Print the payment amount in dollar & cents format - i.e. $371.00.



# IMPLICIT REQUIREMENTS/HINTS:
# - Decide a standard input format - i.e. 5% as `5` or `.05`.

# - The APR needs to be converted to a monthly interest rate.

# - "Loan duration" as input should be labeled in years & the 
#     duration in months used for the formula should be labeled 
#     as such to be differentiated.

# - Think of edge cases - such as no-interest loans or number of 
#     years not in the integer form (such as 3.5 years).



# CLARIFYING QUESTIONS/EDGE CASES:
# - Should the numbers be rounded up or down?

# - What happens if the user inputs a negative number, zero, or an 
#     empty string for the loan amount / APR / loan duration? 
#     In fractional form?

# - How should very large or very small numbers be handled?



# TEST CASES

# EXPECTED CASES

# p = 100_000  # loan amount
# annual_int_rate = 6  
# j = annual_int_rate / 12 / 100  # monthly interest rate
# loan_duration_in_years = 10
# n = loan_duration_in_years * 12  # loan duration in months

# m = p * (j / (1 - (1 + j) ** (-n)))

# print(m)  # 1110.205019416512 (correct)


# p = 150_293  # loan amount
# annual_int_rate = 6
# j = annual_int_rate / 12 / 100  # monthly interest rate
# loan_duration_in_years = 5
# n = loan_duration_in_years * 12  # loan duration in months

# m = p * (j / (1 - (1 + j) ** (-n)))

# print(m)  # 2905.584740262364 (correct)



# EDGE CASES


# NEGATIVE LOAN INPUT [HANDLE - 1]
# p = -100_000  # loan amount
# annual_int_rate = 6
# j = annual_int_rate / 12 / 100  # monthly interest rate
# loan_duration_in_years = 10
# n = loan_duration_in_years * 12  # loan duration in months

# m = p * (j / (1 - (1 + j) ** (-n)))

# print(m)  # - 1110.205019416512  


# NEGATIVE APR INPUT [HANDLE - 1]
# p = 100_000  # loan amount
# annual_int_rate = -6
# j = annual_int_rate / 12 / 100  # monthly interest rate
# loan_duration_in_years = 10
# n = loan_duration_in_years * 12  # loan duration in months

# m = p * (j / (1 - (1 + j) ** (-n)))

# print(m)  # 606.1611273057622   


# NO-INTEREST LOAN (ZERO AS INPUT) [HANDLE - 2]
# p = 100_000  # loan amount
# annual_int_rate = 0
# j = annual_int_rate / 12 / 100  # monthly interest rate
# loan_duration_in_years = 10
# n = loan_duration_in_years * 12  # loan duration in months

# m = p * (j / (1 - (1 + j) ** (-n)))

# print(m)  # ZeroDivisionError: float division by zero 


# APR NOT IN INTEGER FORM
# p = 100_000  # loan amount
# annual_int_rate = 6.7   
# j = annual_int_rate / 12 / 100  # monthly interest rate
# loan_duration_in_years = 10
# n = loan_duration_in_years * 12  # loan duration in months

# m = p * (j / (1 - (1 + j) ** (-n)))

# print(m)  # 1145.682278716137 (correct)


# LOAN AMOUNT NOT IN INTEGER FORM 2
# p = 100_000.976  # loan amount
# annual_int_rate = 8
# j = annual_int_rate / 12 / 100  # monthly interest rate
# loan_duration_in_years = 7
# n = loan_duration_in_years * 12  # loan duration in months

# m = p * (j / (1 - (1 + j) ** (-n)))

# print(m)  # 1558.6366524122225 (correct)


# LOAN DURATION NOT IN INTEGER FORM 
# p = 100_000  # loan amount
# annual_int_rate = 8
# j = annual_int_rate / 12 / 100  # monthly interest rate
# loan_duration_in_years = 7.85
# n = loan_duration_in_years * 12  # loan duration in months

# m = p * (j / (1 - (1 + j) ** (-n))) 

# print(m) # 1481.1704158197379 (correct)


# EMPTY STRING INPUT
# p = ""  # loan amount
# annual_int_rate = 6
# j = annual_int_rate / 12 / 100  # monthly interest rate
# loan_duration_in_years = 10
# n = loan_duration_in_years * 12  # loan duration in months

# m = p * (j / (1 - (1 + j) ** (-n)))

# print(m) # TypeError: can't multiply sequence by non-int of type 'float'


# WHITE SPACE INPUT [HANDLE - 1]
# p = " "  # loan amount
# annual_int_rate = 6
# j = annual_int_rate / 12 / 100  # monthly interest rate
# loan_duration_in_years = 10
# n = loan_duration_in_years * 12  # loan duration in months

# m = p * (j / (1 - (1 + j) ** (-n)))

# print(m) # TypeError: can't multiply sequence by non-int of type 'float'


# VERY SMALL NUMBER INPUT
# p = 0.0000000000014  # loan amount
# annual_int_rate = 8
# j = annual_int_rate / 12 / 100  # monthly interest rate
# loan_duration_in_years = 8
# n = loan_duration_in_years * 12  # loan duration in months

# m = p * (j / (1 - (1 + j) ** (-n)))

# print(m)  # 1.979135095636287e-14



# PSEUDOCODE

# Create function `prompt(message)`
#     Precede `message` with "==> {message}", print.

# Create function `input_as_float(input)`
#     Transform `input` into float form (dollars & cents), reassign.
#     Return `input`

# Create function `calculate_rate(apr)`
#     If `apr` is 0, return `apr`.
#     Divide `apr` with 12 (convert to monthly rate), reassign.
#     Divide `apr` with 100 (convert to percentage to decimal form), 
#     reassign.
#     Return `apr`

# Create function `transform_duration(yrs)`
#     Multiply `yrs` with 12.0,
#     Return `yrs`


# Call `prompt()` on 'Welcome to the Mortgage Calculator!'


# Ask for input with `prompt()`: What is the loan amount?
# Assign input to variable called `loan_amount`.

# Start loop
#     If input isn't a positive number, 
#     print with `prompt`: "Please enter a valid loan amount."
#     Reassign `loan_amount` with new user input. 

# Output '${loan_amount}'

# Call `input_as_float()` on `loan_amount`, reassign.

# Ask for input with `prompt()`: What is the Annual Percentage Rate (APR)?
# - on new line - 'Enter 12 for 12% or 1.5 for 1.5%'
# Assign input to variable called `annual_int_rate`

# Start loop
#     If input isn't zero or a positive number, 
#     print with `prompt`: "Please enter a valid Annual Percentage Rate (APR)."
#     Reassign `annual_int_rate` with new user input. 

# Output '{annual_int_rate}%'

# Call `calculate_rate()` on  `annual_int_rate`, 
# assign result to variable called `monthly_int_rate`

# Ask for input with `prompt()`: What is the loan duration in years? 
# Assign input to variable called `loan_duration_in_yrs`

# Start loop
#     If input isn't a positive number, 
#     print with `prompt`: "Please enter a valid loan duration in years."
#     Reassign `loan_amount` with new user input. 

# Output '{loan_duration_in_yrs} years'

# Call `transform_duration()` on `loan_duration_in_yrs`, 
# assign result to variable called `loan_duration_in_months`.

# If `monthly_int_rate` is not 0, use this formula:
# monthly_payment = loan_amount * (monthly_int_rate / (1 - (1 + monthly_int_rate) ** (loan_duration_in_months)))
# If it IS zero, use this formula:
# monthly_payment = loan_amount / loan_duration_in_months

# Round `monthly_payment` to two decimal places.

# Output 'Your monthly payment: ${monthly_payment}' 


# FORMALIZE PSEUDOCODE 

# START

# SET prompt(message)
#     PRINT '==> {message}'

# SET input_as_float(input)
#     input = float(input)
#     RETURN input 

# SET calculate_rate(apr)
#     IF apr == 0,
#         return apr
#     ELSE 
#         apr = apr / 12  # Convert to monthly rate.
#         apr = apr / 100  # Convert percentage to decimal.
#         RETURN apr

# SET transform_duration(yrs)
#     yrs = yrs * 12.0
#     RETURN yrs


# PRINT prompt('Welcome to the Mortgage Calculator!')

# PRINT prompt('What is the loan amount?')
# loan_amount = GET 

# WHILE loan_amount =! positive number, 
#     PRINT prompt('Please enter a valid loan amount.')
#     loan_amount = GET 

# PRINT '${loan_amount}'

# PRINT prompt('What is the Annual Percentage Rate (APR)?
#     new line - 'Enter 12 for 12% or 1.5 for 1.5%'')
# annual_int_rate = GET

# WHILE annual_int_rate == 0 or positive number, 
#     PRINT prompt('Please enter a valid Annual Percentage Rate (APR).')
#     annual_int_rate = GET

# PRINT '{annual_int_rate}%'

# monthly_int_rate = READ calculate_rate(annual_int_rate)

# PRINT prompt('What is the loan duration in years?')
# loan_dur_in_yrs = GET

# WHILE loan_dur_in_yrs =! positive number,
#     PRINT prompt('Please enter a valid loan duration in years.')
#     loan_dur_in_yrs = GET

# PRINT '{loan_dur_in_yrs} years'

# loan_dur_in_mos = READ transform_duration(loan_dur_in_yrs)

# IF monthly_int_rate =! 0, 
#     monthly_payment = loan_amount * (
#         monthly_int_rate / 
#             (1 - (1 + monthly_int_rate) ** (loan_dur_in_mos))
#     )
#     PRINT monthly_payment 
# ELSE 
#     monthly_payment = loan_amount / loan_duration_in_months
#     PRINT monthly_payment



def prompt(message):
    print(f'==> {message}')

def input_as_float(input):
    input = float(input)
    return input 

def calculate_rate(apr):
    if apr == 0:
        return apr
    else:
        apr = apr / 12  # Convert to monthly rate.
        apr = apr / 100  # Convert percentage to decimal.
        return apr

def transform_duration(yrs):
    yrs = yrs * 12.0
    return yrs


print(prompt('Welcome to the Mortgage Calculator!'))

# PRINT prompt('What is the loan amount?')
# loan_amount = GET 

# WHILE loan_amount =! positive number, 
#     PRINT prompt('Please enter a valid loan amount.')
#     loan_amount = GET 

# PRINT '${loan_amount}'

# PRINT prompt('What is the Annual Percentage Rate (APR)?
#     new line - 'Enter 12 for 12% or 1.5 for 1.5%'')
# annual_int_rate = GET

# WHILE annual_int_rate == 0 or positive number, 
#     PRINT prompt('Please enter a valid Annual Percentage Rate (APR).')
#     annual_int_rate = GET

# PRINT '{annual_int_rate}%'

# monthly_int_rate = READ calculate_rate(annual_int_rate)

# PRINT prompt('What is the loan duration in years?')
# loan_dur_in_yrs = GET

# WHILE loan_dur_in_yrs =! positive number,
#     PRINT prompt('Please enter a valid loan duration in years.')
#     loan_dur_in_yrs = GET

# PRINT '{loan_dur_in_yrs} years'

# loan_dur_in_mos = READ transform_duration(loan_dur_in_yrs)

# IF monthly_int_rate =! 0, 
#     monthly_payment = loan_amount * (
#         monthly_int_rate / 
#             (1 - (1 + monthly_int_rate) ** (loan_dur_in_mos))
#     )
#     PRINT monthly_payment 
# ELSE 
#     monthly_payment = loan_amount / loan_duration_in_months
#     PRINT monthly_payment