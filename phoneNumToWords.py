# Main function to take input and process the phone number
def main():
    while True:
        phone_number = input("Enter a 10-digit phone number (including leading 1): ")
        
        # Validate input
        if len(phone_number) == 11 and phone_number[0] == '1' and phone_number[1:].isdigit():
            phone_number = phone_number[1:]
        elif len(phone_number) != 10 or not phone_number.isdigit():
            print("Please enter a valid 10-digit phone number.")
            continue
        break
    
    area_code = phone_number[:3]
    exchange_code = phone_number[3:6]


main()
