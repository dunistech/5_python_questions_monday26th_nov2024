 <!-- Problem 1: `processStrings.py` -->
This program processes strings of digits to compute the sum, product, and identify characteristics of the digits.

Steps

1. Create the main function:
   - Accept user input in a loop until the user types "quit".
   - Call other functions to process the input string.

2. Create `processStr` function:
   - Compute the sum and product of digits in the string.

3. Create `getHighest` function:
   - Find and return the largest digit.

4. Create `getHasRepeatDigit` function:
   - Check for repeated digits.
   - Call `getHighest` if there are no repeated digits.

---

Code:

```python
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
```

---

## Problem 2: `card_valid.py`
This program validates credit card numbers using a specific algorithm.

Steps

1. Define `isValid` function:
   - Combine all checks for card validity: length, prefix, and validity check.

2. Define `sumDoubleEvenLocation` function:
   - Double every second digit from the right.
   - Adjust for two-digit numbers.

3. Define `sumOddLocation` function:
   - Sum digits at odd positions.

4. Define helper functions:
   - `getDigit`: Handle two-digit numbers.
   - `isPrefix`: Check for a valid prefix.
   - `getSize`: Get the number of digits.
   - `getPrefix`: Extract the first few digits.

---

Code:

```python
# card_valid.py

def isValid(number):
    """Check if the card number is valid."""
    size = getSize(number)
    if size < 13 or size > 16:
        return False
    if not (isPrefix(number, 4) or isPrefix(number, 5) or 
            isPrefix(number, 6) or isPrefix(number, 37)):
        return False
    return (sumDoubleEvenLocation(number) + sumOddLocation(number)) % 10 == 0

def sumDoubleEvenLocation(number):
    """Double every second digit from the right and sum."""
    digits = list(map(int, str(number)))
    total = 0
    for i in range(len(digits) - 2, -1, -2):
        total += getDigit(2 * digits[i])
    return total

def sumOddLocation(number):
    """Sum digits at odd positions."""
    digits = list(map(int, str(number)))
    return sum(digits[-1::-2])

def getDigit(number):
    """Return number if single-digit, or sum of two digits."""
    return number if number < 10 else number // 10 + number % 10

def isPrefix(number, d):
    """Check if the number starts with d."""
    return str(number).startswith(str(d))

def getSize(d):
    """Return the number of digits."""
    return len(str(d))

def getPrefix(number, k):
    """Return the first k digits."""
    return int(str(number)[:k]) if getSize(number) >= k else number

def main():
    card_number = int(input("Enter a credit card number: "))
    if isValid(card_number):
        print("The card number is valid.")
    else:
        print("The card number is invalid.")

if __name__ == "__main__":
    main()

--
Testing

1. Save each script in its respective file: `processStrings.py` and `card_valid.py`.
2. Run the files in Python and test with the provided inputs.