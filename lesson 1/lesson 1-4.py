
def bank(deposit_sum, number_of_years, percent):

    number_of_days_on_deposit = number_of_years * 365
    final_sum = deposit_sum + deposit_sum * percent * number_of_days_on_deposit / 365 / 100

    return print('Your deposit amount', final_sum)


while True:
    user_deposit = input('Enter your deposit sum ')
    user_percent = input('Enter your percent ')
    user_deposit_term = input('Enter your deposit term ')

    if all([user_percent.isdigit(), user_percent.isdigit(), user_deposit_term.isdigit()]):
        bank(int(user_deposit), int(user_deposit_term), int(user_percent))
        break

    else:
        print('Please enter correct data')
        continue