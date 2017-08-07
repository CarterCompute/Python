#####################################

#Loan calculator 

#Declare variables based on user input
loanAmount = float(input("Please enter your loan amount: "))
interestRate = float(input("Please enter the percentage of your interest rate: "))
yearsOfLoan = float(input("Please enter the number of years that your loan is for: "))

#convert interestRate into a percent
interestRate = interestRate / 12 / 100
#convert yearOfLoan to number of payments
numberOfPayments = yearsOfLoan * 12

#Calculate the monthly payment based on the formula
monthlyPayment = (loanAmount * interestRate * (1 + interestRate) ** numberOfPayments) / ((1 + interestRate) ** numberOfPayments -1)

#provide the result to the user
print("Your monthly payment will be $%.2f" % monthlyPayment)


#########################################################


## Loan Calculator with correct formula!!
 
## Loan Amount = 'L'
## Interest Rate = 'i'
## Number of years to pay off the loan = 'y'
## No of Payments converted from the year amount = 'n'
## Monthly Payment = 'M'

#L = input('Enter Loan Amount: ')
#i = input('Enter Interest Rate: ')
#i = float(i)/12/100
#y = float(input('Enter number of years to payoff loan: '))
#n = float(y * 12)
 
#M = float(L)*(float(i)*(1+float(i))**float(n))/((1+float(i))**float(n)-1) # FORMULA
 
#M = ('$%.2f' %M) # To print the amount with 2 decimal places.
 
#print ('Your monthly payment is ' + M) # Monthly Payment
