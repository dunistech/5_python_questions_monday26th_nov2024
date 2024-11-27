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