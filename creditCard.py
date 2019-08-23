def calculate_credit_card_number_check_digit(cc_number):
    cc_digits = list(map(int, list(str(cc_number))))

    cc_digits.reverse()

    sum = 0

    for index in range(len(cc_digits)):
        if index % 2 == 0:
            even_digit = cc_digits[index] * 2

            if even_digit > 9:
                even_digit -= 9

            sum += even_digit
        else: 
            sum += cc_digits[index]

    return str((sum * 9) % 10)

def validate_credit_card_number_check_digit(cc_number):
    expected_check_number = calculate_credit_card_number_check_digit(cc_number[:-1])
    
    if cc_number[-1] == expected_check_number:
        return 'This is a valid credit card number.'
    else:
        return 'This is an invalid credit card number.'