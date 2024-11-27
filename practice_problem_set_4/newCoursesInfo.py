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