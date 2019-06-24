con_loop = True
while con_loop:
    amount_input = input("Please enter your amount: \n")
    tax_rate = 0
    if amount_input.isdigit():
        while con_loop:
            tax_rate = input('Please enter tax rate:\n')
            if tax_rate.isdigit() and (1 <= int(tax_rate) <= 99):
                con_loop = False
            else:
                print('Rate is incorrect, try again.')
                con_loop = True
        print('\n', end="")
        print('===== ===== ===== ===== =====')
        print('AMOUNT: ' + str(amount_input) + '$')
        print('RATE: ' + str(tax_rate) + '%')
        tax_amount = int(amount_input) * int(tax_rate)/100
        net_amount = int(amount_input) - tax_amount
        print('===== ===== ===== ===== =====')
        print('TAX: ' + '{:.2f}'.format(tax_amount) + '$')
        print('NET: ' + '{:.2f}'.format(net_amount) + '$')
        print('===== ===== ===== ===== =====')
        exit()
    else:
        print('Number is incorrect, try again.')
        con_loop = True
