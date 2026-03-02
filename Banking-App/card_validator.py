def card_valid():
    card_number=input("Enter your credit card number: ")
    card_number = card_number.replace(" ", "").replace("-", "")
    card_number=card_number[::-1]

    if not card_number.isdigit():
        print("Invalid characters!")
        return False

    sum_odd_digits=0
    sum_even_digits=0

    for x in card_number[::2]:
        sum_odd_digits+=int(x)

    for x in card_number[1::2]:
        digit=int(x)*2
        if digit>=10:
            sum_even_digits+=(1+(digit%10))
        else:
            sum_even_digits+=digit

    total=sum_even_digits+sum_odd_digits

    return total%10==0
