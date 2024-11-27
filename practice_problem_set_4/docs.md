## Problem 1: Lockers Problem (`lockers.py`)

Description:
100 students manipulate 100 lockers following a set pattern. We need to determine which lockers remain open after all students have finished.

---

 Step-by-Step Solution:

1. Initialize Lockers:
   - Use a list of 100 Boolean values (`True` for open, `False` for closed).
   - Initially, all lockers are closed (`False`).

2. Simulate Students:
   - For each student \( S_n \) (where \( n \) ranges from 1 to 100):
     - They toggle lockers starting from \( n \) in steps of \( n \). 
     - If the locker is closed, they open it; if it is open, they close it.

3. Determine Open Lockers:
   - After all students have toggled the lockers, collect the indices of lockers that are still `True` (open).


#  Code:

```python
# lockers.py

def simulate_lockers():
    # Step 1: Initialize lockers (all closed)
    lockers = [False] * 100  # False means closed

    # Step 2: Simulate students toggling lockers
    for student in range(1, 101):  # Students S1 to S100
        for locker in range(student - 1, 100, student):  # Toggle every nth locker
            lockers[locker] = not lockers[locker]

    # Step 3: Determine open lockers
    open_lockers = [i + 1 for i, is_open in enumerate(lockers) if is_open]
    return open_lockers

def main():
    open_lockers = simulate_lockers()
    print("Open lockers after all students have toggled them:")
    print(open_lockers)

if __name__ == "__main__":
    main()
```

---

 Explanation for Beginners:
- Lockers List: Each locker is represented by a Boolean value in a list (`False` = closed, `True` = open).
- Toggling: A locker toggles between open and closed whenever a student interacts with it.
- Open Lockers: Only lockers toggled an odd number of times remain open. This happens for lockers whose positions are perfect squares (e.g., 1, 4, 9, etc.), as they have an odd number of divisors.

---

## Problem 2: New Courses Information (`newCoursesInfo.py`)

Description:
We need to:
1. Calculate the range of marks (difference between highest and lowest) for each course.
2. Calculate the average marks for each student across all courses.

---

 Step-by-Step Solution:

1. Initialize Marks Table:
   - Create a 2D list (`numC x numS`) of random integers between 0 and 100 to represent course marks.

2. Compute Range of Marks for Each Course:
   - For each course (row in the table), find the minimum and maximum marks.
   - Calculate the range as `max - min`.

3. Compute Average Marks for Each Student:
   - For each student (column in the table), calculate the average of their marks across all courses.

4. Output Results:
   - Display the range for each course and the average marks for each student.

---

 Code:

```python
# newCoursesInfo.py
import random

def initializeMarks(numC, numS):
    """Initialize a marks table with random values between 0 and 100."""
    return [[random.randint(0, 100) for _ in range(numS)] for _ in range(numC)]

def findMinForRow(marks, row):
    """Find the minimum value in a row."""
    return min(marks[row])

def findMaxForRow(marks, row):
    """Find the maximum value in a row."""
    return max(marks[row])

def printRangeForCourse(courses, course_index, min_mark, max_mark):
    """Print the range of marks for a specific course."""
    print(f"{courses[course_index]}: {max_mark - min_mark}")

def computeAllRanges(courses, marks):
    """Compute and display the range of marks for each course."""
    print("Courses Range of Marks")
    for i in range(len(courses)):
        min_mark = findMinForRow(marks, i)
        max_mark = findMaxForRow(marks, i)
        printRangeForCourse(courses, i, min_mark, max_mark)

def computeAllAverages(students, marks):
    """Compute and display the average marks for each student."""
    print("\nStudent Name Average Marks")
    for student_index in range(len(students)):
        total_marks = sum(marks[course][student_index] for course in range(len(marks)))
        average_marks = total_marks / len(marks)
        print(f"{students[student_index]}: {average_marks:.1f}")

def main():
    # Step 1: Initialize data
    students = ["Andy Pandy", "Benny Menny", "Kim Simms", "Rolly Polly", "Cindy Mindy", "Geeta Peeta"]
    courses = ["CS101", "CS105", "CS110", "CS115", "CS120"]
    marks = initializeMarks(len(courses), len(students))

    # Step 2: Compute and display ranges
    computeAllRanges(courses, marks)

    # Step 3: Compute and display averages
    computeAllAverages(students, marks)

if __name__ == "__main__":
    main()
```

---

 Explanation for Beginners:
- Marks Table: A 2D list where rows represent courses and columns represent students.
- Random Marks: Marks are generated randomly for simplicity.
- Range of Marks: Calculated as `max - min` for each row (course).
- Average Marks: Computed by summing marks across all courses for a student and dividing by the number of courses.

---

 Example Output:
With randomly generated marks:
```
Courses Range of Marks
CS101: 75
CS105: 92
CS110: 81
CS115: 88
CS120: 88

Student Name Average Marks
Andy Pandy: 51.4
Benny Menny: 32.2
Kim Simms: 90.6
Rolly Polly: 57.4
Cindy Mindy: 74.4
Geeta Peeta: 56.8
```

---

These programs are clear, efficient, and follow all the guidelines provided.
