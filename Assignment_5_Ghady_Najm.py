class Course:
    def __init__(self, code, name, credit_hours, is_core):
        self.code = code
        self.name = name
        self.credit_hours = credit_hours
        self.is_core = is_core

    def __str__(self):
        return f"{self.code}: {self.name} ({self.credit_hours} credits) - {'Core' if self.is_core else 'Elective'}"

    def to_string(self):
        return f"{self.code},{self.name},{self.credit_hours},{self.is_core}"


class Student:
    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name
        self.enrolled_courses = {}

    def enroll(self, course):
        if course.code in self.enrolled_courses:
            raise Exception(f"Already enrolled in course: {course.code}")
        self.enrolled_courses[course.code] = course

    def drop(self, course_code):
        if course_code not in self.enrolled_courses:
            raise Exception(f"Course not found: {course_code}")
        del self.enrolled_courses[course_code]

    def list_courses(self):
        return list(self.enrolled_courses.values())

    def __str__(self):
        return f"{self.student_id}: {self.name}"


class CourseCatalog:
    def __init__(self):
        self.courses = {}

    def add_course(self, course):
        if course.code in self.courses:
            raise Exception(f"Course already exists: {course.code}")
        self.courses[course.code] = course

    def get_course(self, code):
        return self.courses.get(code)

    def list_courses(self):
        return list(self.courses.values())

    def save_to_file(self, filename):
        with open(filename, "w") as file:
            for course in self.courses.values():
                file.write(course.to_string() + "\n")

    def load_from_file(self, filename):
        with open(filename, "r") as file:
            for line in file:
                code, name, credit_hours, is_core = line.strip().split(",")
                course = Course(
                    code, name, int(credit_hours), is_core.lower() == "true"
                )
                self.add_course(course)


class EnrollmentSystem:
    def __init__(self):
        self.course_catalog = CourseCatalog()
        self.students = {}

    def add_student(self, student):
        if student.student_id in self.students:
            raise Exception(f"Student already exists: {student.student_id}")
        self.students[student.student_id] = student

    def enroll_student_in_course(self, student_id, course_code):
        student = self.students.get(student_id)
        course = self.course_catalog.get_course(course_code)
        if not student:
            raise Exception(f"Student not found: {student_id}")
        if not course:
            raise Exception(f"Course not found: {course_code}")
        student.enroll(course)

    def drop_student_course(self, student_id, course_code):
        student = self.students.get(student_id)
        if not student:
            raise Exception(f"Student not found: {student_id}")
        student.drop(course_code)

    def list_student_courses(self, student_id):
        student = self.students.get(student_id)
        if not student:
            raise Exception(f"Student not found: {student_id}")
        return student.list_courses()

    def save_catalog(self, filename):
        self.course_catalog.save_to_file(filename)

    def load_catalog(self, filename):
        self.course_catalog.load_from_file(filename)


def main():
    system = EnrollmentSystem()

    while True:
        print("\nMenu:")
        print("1. Add Course")
        print("2. Enroll Student in Course")
        print("3. Drop Course for Student")
        print("4. List Student Courses")
        print("5. Save Course Catalog")
        print("6. Load Course Catalog")
        print("7. Exit")

        choice = input("Enter your choice: ")

        try:
            if choice == "1":
                code = input("Enter course code: ")
                name = input("Enter course name: ")
                credit_hours = int(input("Enter credit hours: "))
                is_core = input("Is it a core course? (yes/no): ").lower() == "yes"
                course = Course(code, name, credit_hours, is_core)
                system.course_catalog.add_course(course)
                print("Course added successfully.")

            elif choice == "2":
                student_id = input("Enter student ID: ")
                student_name = input("Enter student name: ")
                if student_id not in system.students:
                    student = Student(student_id, student_name)
                    system.add_student(student)
                course_code = input("Enter course code to enroll in: ")
                system.enroll_student_in_course(student_id, course_code)
                print("Student enrolled successfully.")

            elif choice == "3":
                student_id = input("Enter student ID: ")
                course_code = input("Enter course code to drop: ")
                system.drop_student_course(student_id, course_code)
                print("Course dropped successfully.")

            elif choice == "4":
                student_id = input("Enter student ID: ")
                courses = system.list_student_courses(student_id)
                print("Courses enrolled:")
                for course in courses:
                    print(course)

            elif choice == "5":
                filename = input("Enter filename to save catalog: ")
                system.save_catalog(filename)
                print("Course catalog saved successfully.")

            elif choice == "6":
                filename = input("Enter filename to load catalog: ")
                system.load_catalog(filename)
                print("Course catalog loaded successfully.")

            elif choice == "7":
                print("Exiting the program.")
                break

            else:
                print("Invalid choice. Please try again.")

        except Exception as e:
            print(f"Error: {e}")


main()