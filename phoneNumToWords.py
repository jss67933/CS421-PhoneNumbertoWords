import enchant
english_dict = enchant.Dict("en_US")

# Digit-to-letter mapping
digit_to_letters = {
    '2': 'ABC', '3': 'DEF', '4': 'GHI', '5': 'JKL',
    '6': 'MNO', '7': 'PQRS', '8': 'TUV', '9': 'WXYZ'
}

###########################################################################################################################################
# Generate letter combinations for a given phone number section
def generate_combinations(phone_section):
    if not phone_section:
        return [""]
    
    first_digit = phone_section[0]
    remaining_section = phone_section[1:]
    letters = digit_to_letters.get(first_digit, "")
    
    combinations = []
    for letter in letters:
        for combination in generate_combinations(remaining_section):
            combinations.append(letter + combination)
    return combinations

############################################################################################################################################
# Generate combinations for specific sections
def generate_10_digit_combinations(phone_number):
    return generate_combinations(phone_number)

def generate_7_digit_whole_combinations(phone_number):
    return generate_combinations(phone_number[3:])

def generate_7_digit_split_combinations(phone_number):
    part1 = generate_combinations(phone_number[3:6])
    part2 = generate_combinations(phone_number[6:])
    return [(p1, p2) for p1 in part1 for p2 in part2]

def generate_exchange_only_combinations(phone_number):
    return generate_combinations(phone_number[3:6])

def generate_number_only_combinations(phone_number):
    return generate_combinations(phone_number[6:])

############################################################################################################################################
# Check if a given combination is a valid English word
def is_word(combination):
    return english_dict.check(combination)

############################################################################################################################################
# Generate meaningful words based on condition
def generateValidWords(condition, phone_number):
    condition_functions = {
        "10-digit": generate_10_digit_combinations,
        "7-digit whole": generate_7_digit_whole_combinations,
        "7-digit split": generate_7_digit_split_combinations,
        "exchange only": generate_exchange_only_combinations,
        "number only": generate_number_only_combinations
    }
    
    generate_combinations_func = condition_functions.get(condition)
    possible_combinations = generate_combinations_func(phone_number) if generate_combinations_func else []
    
    if condition == "7-digit split":
        return [(p1, p2) for p1, p2 in possible_combinations if is_word(p1) and is_word(p2)]
    else:
        return [combination for combination in possible_combinations if is_word(combination)]

############################################################################################################################################
# Main function to take input and process the phone number
def main():
    while True:
        phone_number = input("Enter a 10-digit phone number (excluding leading 1): ")
        
        # Validate input
        if len(phone_number) == 11 and phone_number[0] == '1' and phone_number[1:].isdigit():
            phone_number = phone_number[1:]
        elif len(phone_number) != 10 or not phone_number.isdigit():
            print("Please enter a valid 10-digit phone number.")
            continue
        break
    
    area_code = phone_number[:3]
    exchange_code = phone_number[3:6]
    
    # Process each condition to find meaningful word combinations
    for condition in ["10-digit", "7-digit whole", "7-digit split", "exchange only", "number only"]:
        valid_words = generateValidWords(condition, phone_number)
        
        if valid_words:
            if condition == "10-digit":
                print(f"1-{valid_words[0]}")
            elif condition == "7-digit whole":
                print(f"1-{area_code}-{valid_words[0]}")
            elif condition == "7-digit split":
                # Display the first two valid pairs for 7-digit split
                print(f"1-{area_code}-{valid_words[0][0]}-{valid_words[0][1]}")
                if len(valid_words) > 1:
                    print(f"1-{area_code}-{valid_words[1][0]}-{valid_words[1][1]}")
                return
            elif condition == "exchange only":
                for word in valid_words[:5]:  # Show the first two options
                    print(f"1-{area_code}-{word}-{phone_number[6:]}")
                return
            elif condition == "number only":
                for word in valid_words[:5]:  # Show the first two options
                    print(f"1-{area_code}-{exchange_code}-{word}")
                return
            return
        
    # If no word found, format and print the phone number
    formatted_number = f"1-{area_code}-{exchange_code}-{phone_number[6:]}"
    print(f"{formatted_number}: No word combination available")

main()
