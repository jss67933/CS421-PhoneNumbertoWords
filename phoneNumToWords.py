def main():
    phone_number = input("Enter a 10-digit phone number (excluding leading 1): ")
    if len(phone_number) != 11 and phone_number[0] != '1' and phone_number.isdigit():
        print("Please enter a valid 10-digit phone number.")
    else:
        print("You entered:", phone_number)

    #result = switch_statement(phone_number)
    #print(result)

main()
