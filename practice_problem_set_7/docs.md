-> Solution for Practice Problem Set 7: String Merging**

This solution implements the required program in Python, designed for **absolute beginners**. It includes:
- Clear and detailed comments.
- Descriptive labels for input and output.
- Consistent program style with meaningful variable names and proper formatting.
- Full implementation with recursive and non-recursive approaches.

-> Complete Python Program**

```python
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
```

---

-> How This Works (Detailed Explanation for Beginners)**

#-> 1. Recursive Function (`mergeRecursive`)**
- **Base Case:**  
  - If one string is empty, return the other string because there's nothing left to merge.
- **Recursive Case:**  
  - Compare the first characters of both strings (`s1[0]` and `s2[0]`).
  - Take the smaller character, add it to the result, and **recursively call** `mergeRecursive` on the remaining parts of the strings.
  - Think of it as peeling one character at a time from the strings, like picking apples from two baskets in order of size.

#-> 2. Non-Recursive Function (`orderedMerge`)**
- Use a **loop** to merge the strings:
  - Compare the characters at the current positions of both strings (`s1[i]` and `s2[j]`).
  - Append the smaller character to the result string and move the index for that string forward.
  - When one string runs out, append the rest of the other string.

#-> 3. Main Function**
- **Input:** Prompts the user for two ordered strings.  
- **Output:** Displays the input strings and the merged results of both functions.
- Calls both functions and ensures the results are labeled for clarity.

---

-> Sample Input/Output**

#-> Example 1**
```
Enter the first ordered string: acdrt
Enter the second ordered string: bdet
First string: acdrt
Second string: bdet
Result of recursive function: abcddertt
Result of non-recursive function: abcddertt
```

#-> Example 2**
```
Enter the first ordered string: DEab
Enter the second ordered string: BFxz
First string: DEab
Second string: BFxz
Result of recursive function: BDEFabxz
Result of non-recursive function: BDEFabxz
```

---

-> Beginner-Friendly Concepts**
1. **Recursion:**  
   - A function calling itself to solve smaller versions of the problem until it reaches a base case.
   - Analogy: Solving a puzzle piece by piece until it’s complete.

2. **Non-Recursive Approach:**  
   - Uses a loop to control the merging process step-by-step without recursion.
   - Easier to follow for some, as it avoids the complexity of function calls.

3. **String Manipulation:**  
   - Strings are immutable in Python, meaning you can’t change them directly but can build new strings from slices (`s1[1:]`).

4. **Program Structure:**  
   - Functions are like tools; each does a specific job (e.g., merging strings).
   - The `main()` function is the control center that orchestrates everything.
