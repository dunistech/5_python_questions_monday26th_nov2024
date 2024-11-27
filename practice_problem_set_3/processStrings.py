# processStrings.py

def processStr(s):
    """Compute and print the sum and product of digits in the string."""
    digit_sum = sum(int(d) for d in s)
    digit_product = 1
    for d in s:
        digit_product *= int(d)
    print(f"The sum of the digits in {s} is {digit_sum}")
    print(f"The product of the digits in {s} is {digit_product}")

def getHighest(s):
    """Return the largest digit in the string."""
    return max(int(d) for d in s)

def getHasRepeatDigit(s):
    """Check if there are repeated digits."""
    if len(set(s)) == len(s):
        print("The string has no repeated digits.")
        return getHighest(s)
    else:
        print("The string has repeated digits.")
        return 0

def main():
    while True:
        user_input = input("Enter a string of digits to process or 'quit' to stop: ")
        if user_input.lower() == 'quit':
            break
        if user_input.isdigit():
            processStr(user_input)
            highest = getHasRepeatDigit(user_input)
            if highest:
                print(f"The highest digit in the given string is: {highest}")
        else:
            print("Invalid input. Please enter a string of digits.")

if __name__ == "__main__":
    main()
