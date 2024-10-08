def calculate_tax(amount, is_jedi):
    tax_rate = 0.10
    if is_jedi:
        tax_rate -= 0.05
    return amount * tax_rate

amount = float(input('Enter the amount: '))
is_jedi = input('Are you a Jedi? (yes/no) ') == 'yes'
tax = calculate_tax(amount, is_jedi)
print('Tax to pay:', tax)