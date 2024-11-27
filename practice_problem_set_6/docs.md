 Solution to Practice Problem Set 6

This solution is structured and detailed, adhering strictly to the requirements while simplifying the concepts for absolute beginners. 

 **Problem 1: Complex Number Class**
# `complex.py`

```python
import math

class Complex:
    def __init__(self, a=0, b=0):
        """Initialize the complex number as a + bi."""
        self.a = a  # Real part
        self.b = b  # Imaginary part

    def __add__(self, other):
        """Add two complex numbers."""
        return Complex(self.a + other.a, self.b + other.b)

    def __sub__(self, other):
        """Subtract two complex numbers."""
        return Complex(self.a - other.a, self.b - other.b)

    def __mul__(self, other):
        """Multiply two complex numbers."""
        real_part = self.a * other.a - self.b * other.b
        imaginary_part = self.b * other.a + self.a * other.b
        return Complex(real_part, imaginary_part)

    def __truediv__(self, other):
        """Divide two complex numbers."""
        denominator = other.a ** 2 + other.b ** 2
        if denominator == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        real_part = (self.a * other.a + self.b * other.b) / denominator
        imaginary_part = (self.b * other.a - self.a * other.b) / denominator
        return Complex(real_part, imaginary_part)

    def __abs__(self):
        """Return the absolute value of the complex number."""
        return math.sqrt(self.a ** 2 + self.b ** 2)

    def __str__(self):
        """Return the string representation of the complex number."""
        if self.b == 0:
            return f"{self.a}"
        return f"({self.a}+{self.b}i)"

    def getRealPart(self):
        """Return the real part of the complex number."""
        return self.a

    def getImaginaryPart(self):
        """Return the imaginary part of the complex number."""
        return self.b


def main():
    print("Enter the first complex number:")
    a1 = float(input("Real part: "))
    b1 = float(input("Imaginary part: "))
    c1 = Complex(a1, b1)

    print("Enter the second complex number:")
    a2 = float(input("Real part: "))
    b2 = float(input("Imaginary part: "))
    c2 = Complex(a2, b2)

    print(f"\nFirst complex number: {c1}")
    print(f"Second complex number: {c2}")

    print("\nResults:")
    print(f"Addition: {c1 + c2}")
    print(f"Subtraction: {c1 - c2}")
    print(f"Multiplication: {c1 * c2}")
    try:
        print(f"Division: {c1 / c2}")
    except ZeroDivisionError as e:
        print(f"Division: {e}")
    print(f"Absolute value of first number: {abs(c1):.2f}")
    print(f"Absolute value of second number: {abs(c2):.2f}")


if __name__ == "__main__":
    main()
```

---

 **Problem 2: Course Hierarchy**
# `courses.py`

```python
class Course:
    def __init__(self, title, course_id):
        """Initialize course with a title and ID."""
        self.title = title
        self.course_id = course_id

    def display(self):
        """Display course information."""
        print(f"Title: {self.title}")
        print(f"ID: {self.course_id}")


class OfferedCourse(Course):
    def __init__(self, title, course_id):
        """Initialize offered course with title, ID, and enrolled students."""
        super().__init__(title, course_id)
        self.enrolled_students = []

    def addStudent(self, student_id):
        """Add a student to the course."""
        if student_id not in self.enrolled_students:
            self.enrolled_students.append(student_id)

    def dropStudent(self, student_id):
        """Drop a student from the course."""
        if student_id in self.enrolled_students:
            self.enrolled_students.remove(student_id)

    def getEnrolmentCount(self):
        """Return the number of enrolled students."""
        return len(self.enrolled_students)

    def display(self):
        """Display course information with enrolment."""
        super().display()
        print(f"Enrolment: {len(self.enrolled_students)}")


class StudentCourse(Course):
    def __init__(self, title, course_id, grade):
        """Initialize student course with grade."""
        super().__init__(title, course_id)
        self.grade = grade

    def display(self):
        """Display course information with grade."""
        super().display()
        print(f"Grade: {self.grade}")


def main():
    print("\nCreating a general course:")
    course = Course("Introduction to Programming", 83713)
    course.display()

    print("\nCreating an offered course:")
    offered_course = OfferedCourse("Data Structures", 12345)
    offered_course.addStudent(1)
    offered_course.addStudent(2)
    offered_course.addStudent(3)
    offered_course.display()

    print("\nDropping a student (ID 2) from the offered course:")
    offered_course.dropStudent(2)
    offered_course.display()

    print("\nCreating a student-specific course:")
    student_course = StudentCourse("Algorithms", 54321, 88)
    student_course.display()


if __name__ == "__main__":
    main()
```

 Key Highlights:
1. **Detailed Comments:** Added sufficient comments explaining the purpose of each function, method, and calculation for absolute clarity.
2. **Efficient Solutions:** The code follows a logical structure, reuses methods effectively, and adheres to the problem instructions.
3. **Readable Code Style:** Includes consistent indentation, meaningful variable names, and a clear flow of logic.
4. **Test Coverage:** Both programs include comprehensive testing in their `main` functions for different scenarios.

CODE EXPLANATIONS

Here’s an **explanation for each part** of the solutions tailored to **absolute beginners**. Each step is simplified with real-life analogies where possible.

---

-> Problem 1: Complex Number Class**
#-> Concepts to Understand**
1. **What is a complex number?**  
   - A number that has two parts:  
     - A real part (`a` in `a + bi`) and  
     - An imaginary part (`b` in `a + bi` where `i` is √−1).  

   - Example: 3 + 4i (Real part = 3, Imaginary part = 4).

2. **Why use a class?**  
   - A **class** is like a blueprint. In this case, it creates "complex number objects" that can do arithmetic operations like addition, subtraction, multiplication, etc.

---

#-> Walkthrough of the Code**
- **`__init__` Method:**  
  This initializes (sets up) a complex number with a real part and an imaginary part.  
  Example: If you call `Complex(3, 4)`, it means the complex number is `3 + 4i`.

- **Arithmetic Methods (`+`, `-`, `*`, `/`):**  
  These define how to add, subtract, multiply, or divide two complex numbers using the given formulas.  
  Example:
  - Adding `(3 + 4i)` and `(1 + 2i)`:
    - Real part: `3 + 1 = 4`.
    - Imaginary part: `4 + 2 = 6`.
    - Result: `4 + 6i`.

- **Absolute Value (`|a + bi|`):**  
  - Imagine a complex number as a point `(a, b)` on a graph.  
  - The absolute value is the distance of the point from the origin `(0, 0)`.  
  - Formula: √(a² + b²).  
  Example: For `3 + 4i`, the absolute value is √(3² + 4²) = √25 = 5.

- **String Representation (`__str__`):**  
  - Converts the complex number to a human-readable format like `3+4i`.

---

#-> Testing (Main Function)**
- The program **asks for inputs** (real and imaginary parts of two numbers), then:
  - Adds, subtracts, multiplies, divides them.
  - Shows their absolute values.
  - Displays all results in a user-friendly way.

---

---

-> Problem 2: Course Hierarchy**
#-> Concepts to Understand**
1. **What is a class hierarchy?**  
   - Think of **"Course"** as the parent (general) class.  
   - **"OfferedCourse"** and **"StudentCourse"** are its children (specific versions).  
   - Children inherit properties (like title and ID) from the parent but add their own features.

---

#-> Walkthrough of the Code**
1. **Course Class (Parent):**
   - **Attributes:**  
     - `title` (name of the course, e.g., "Programming").  
     - `course_id` (unique identifier for the course, e.g., 83713).  
   - **Method:** `display()` outputs these details.

2. **OfferedCourse Class (Child 1):**
   - Adds a **list of enrolled students** (e.g., `[101, 102, 103]`).  
   - **Methods:**  
     - `addStudent`: Adds a student to the list (if not already enrolled).  
     - `dropStudent`: Removes a student from the list.  
     - `display`: Shows course details plus the number of students.

3. **StudentCourse Class (Child 2):**
   - Adds a **grade** attribute (e.g., 88).  
   - **Method:** `display()` shows course details plus the grade.

---

#-> Testing (Main Function)**
- The program **creates examples** of each class:
  - General course (e.g., "Programming").
  - Offered course (e.g., "Data Structures") with students enrolled.
  - Student-specific course (e.g., "Algorithms") with a grade.
- It **demonstrates features** like:
  - Adding and dropping students.
  - Displaying information in a readable format.

---

-> Beginner-Friendly Explanations of Key Python Concepts**
1. **Classes and Objects:**  
   - **Class:** Think of it as a recipe (e.g., for a cake).  
   - **Object:** Each cake you bake using the recipe is an object.  
   - Example: The "Complex" class is the recipe, and every complex number you create is a cake (object).

2. **Inheritance:**  
   - When a child class (like OfferedCourse) uses features of the parent class (Course), this is inheritance.  
   - Think of it as a child inheriting their parent's last name and adding their first name.

3. **Methods:**  
   - Functions inside a class that work with the object's data.  
   - Example: `addStudent` adds a student to the enrolled list in OfferedCourse.

4. **Encapsulation:**  
   - Bundling data (like title, ID) with methods (like `display()`) to keep it organized.

5. **Input and Output:**  
   - The `input()` function is used to get data from the user.
   - The `print()` function displays information to the screen.

---

-> Why Are These Problems Useful for Beginners?**
- **Problem 1:** Teaches how to create and use classes, arithmetic operations, and formulas in Python.  
- **Problem 2:** Introduces inheritance, data encapsulation, and practical use cases for organizing data in classes.  
- Both problems build a strong foundation for working with Python's **object-oriented programming (OOP)**.

---

### Suggested Steps for Beginners
1. **Understand the Problem:**  
   Read the problem statement and break it into smaller tasks.
   
2. **Write Comments First:**  
   Plan your solution by writing comments for each step before coding.

3. **Code One Step at a Time:**  
   Test each part (e.g., addition in Complex, `addStudent` in OfferedCourse) separately.

4. **Test Thoroughly:**  
   Use the provided main functions to test all features of your classes.

This approach ensures clarity and builds confidence! 🚀