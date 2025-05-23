enter_number = float(input('enter number: '))
if enter_number < 10:
    print('enter number less than 10')
elif 10 < enter_number < 20:
    print('enter number between 10 and 20')
elif enter_number > 20:
    print('enter number greater than 20')