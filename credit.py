import cs50

def main():
    # Get the card number as a string
    card_number = cs50.get_string("Number: ")

    # Validate the card number using Luhn's Algorithm
    if is_valid_luhn(card_number):
        # Identify the card issuer
        issuer = identify_issuer(card_number)
        print(issuer)
    else:
        print("INVALID")

def is_valid_luhn(card_number):
    """Validate the card number using Luhn's Algorithm."""
    total = 0
    length = len(card_number)

    for i in range(length):
        digit = int(card_number[length - 1 - i])

        if i % 2 == 1:
            doubled = digit * 2
            if doubled > 9:
                doubled -= 9
            total += doubled
        else:
            total += digit

    return total % 10 == 0

def identify_issuer(card_number):
    """Identify the card issuer based on the card number."""
    length = len(card_number)
    iin = int(card_number[:2])

    if (iin == 34 or iin == 37) and length == 15:
        return "AMEX"
    elif (iin >= 40 and iin <= 49) and (length == 13 or length == 16):
        return "VISA"
    elif (iin >= 51 and iin <= 55) and length == 16:
        return "MASTERCARD"
    else:
        return "INVALID"

if __name__ == "__main__":
    main()
