# File: string_merge.py

# Function: mergeRecursive
# Description: Recursively merges two ordered strings, leaving characters in ASCII order.
def mergeRecursive(s1, s2):
    # Base cases: If one string is empty, return the other string
    if len(s1) == 0:
        return s2
    if len(s2) == 0:
        return s1
    
    # Recursive case: Compare the first characters of each string
    if s1[0] < s2[0]:
        # Include the smaller character from s1 and recursively merge the rest
        return s1[0] + mergeRecursive(s1[1:], s2)
    else:
        # Include the smaller character from s2 and recursively merge the rest
        return s2[0] + mergeRecursive(s1, s2[1:])

# Function: orderedMerge
# Description: Non-recursively merges two ordered strings, leaving characters in ASCII order.
def orderedMerge(s1, s2):
    # Initialize an empty result string and two indices to track positions in s1 and s2
    result = ""
    i, j = 0, 0

    # Loop through both strings while there are characters left in both
    while i < len(s1) and j < len(s2):
        if s1[i] < s2[j]:
            result += s1[i]  # Add the smaller character from s1
            i += 1  # Move to the next character in s1
        else:
            result += s2[j]  # Add the smaller character from s2
            j += 1  # Move to the next character in s2

    # Add any remaining characters from s1 or s2
    result += s1[i:]
    result += s2[j:]

    return result

# Main Function: Program Entry Point
def main():
    # Input: Prompt the user to enter two ordered strings
    first_string = input("Enter the first ordered string: ")
    second_string = input("Enter the second ordered string: ")

    # Output: Display the input strings
    print(f"First string: {first_string}")
    print(f"Second string: {second_string}")

    # Call and display results of the recursive merge function
    recursive_result = mergeRecursive(first_string, second_string)
    print(f"Result of recursive function: {recursive_result}")

    # Call and display results of the non-recursive merge function
    non_recursive_result = orderedMerge(first_string, second_string)
    print(f"Result of non-recursive function: {non_recursive_result}")

# Run the program
if __name__ == "__main__":
    main()