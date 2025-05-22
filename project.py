# initial_amount = float(input('the initial amount of money: '))
# interest_rate = float(input('annual interest rate: '))
# years=int(input('number of years: '))
#
# result= initial_amount * (1+interest_rate / 100)**years
# print(round(result,2))

# sumRes=float(input('sum of money: '))
# interest_rate=float(input('annual interest rate: '))
# percentage=sumRes/(1+interest_rate/100)
#
# print(round(percentage,2))

income=float(input('Enter income: '))
needs_percent = 50
wants_percent = 30
savings_percent = 20

print('needs_percent:', income*(needs_percent/100))
print('wants_percent:', income*(wants_percent/100))
print('savings_percent:', income*(savings_percent/100))