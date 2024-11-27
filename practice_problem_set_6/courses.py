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