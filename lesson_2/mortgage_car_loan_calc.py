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

#     WRITE A PROGRAM THAT:
#     Takes the loan amount, the annual percentage rate (APR), loan 
#     duration, and calculates how much the monthly payment will be. 

#     INPUTS: 
#     - Loan amount
#     - APR 
#     - Loan duration 

#     OUTPUTS:
#     - Monthly payment

#     EXPLICIT REQUIREMENTS/RULES:
#     - Calculate the monthly interest rate
#     - Calculate the loan duration in months
#     - Use explicit names for the variables in the formula.
#     - Print the payment amount in dollar & cents format - i.e. $371.00.

#     IMPLICIT REQUIREMENTS/HINTS:
#     - Decide a standard input format - i.e. 5% as `5` or `.05`.
#     - The APR needs to be converted to a monthly interest rate.
#     - "Loan duration" as input should be labeled in years & the 
#       duration in months used for the formula should be labeled 
#       as such to be differentiated.
#     - Think of edge cases - such as no-interest loans or number of 
#       years not in the integer form (such as 3.5 years).

#     CLARIFYING QUESTIONS/EDGE CASES:
#     - Should the numbers be rounded up or down?
#     - What happens if the user inputs a negative number, zero, or an 
#       empty string for the loan amount / APR / loan duration? 
#       In fractional form?
#     - How should very large or very small numbers be handled?


# TEST CASE

#    p = 100_000  # loan amount
#    annual_int_rate = 6  
#    j = annual_int_rate / 12 / 100  # monthly interest rate
#    loan_duration_in_years = 10
#    n = loan_duration_in_years * 12  # loan duration in months

#    m = p * (j / (1 - (1 + j) ** (-n)))

#    print(m)  # 1110.205019416512


p = 100_000  # loan amount
annual_int_rate = 0  
j = annual_int_rate / 12 / 100  # monthly interest rate
loan_duration_in_years = 10
n = loan_duration_in_years * 12  # loan duration in months

m = p * (j / (1 - (1 + j) ** (-n)))

print(m)  # 1110.205019416512


# PSEUDOCODE

# Ask for input 

