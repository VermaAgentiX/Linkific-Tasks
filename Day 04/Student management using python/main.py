from student import Student
from storage import load_students, save_students


def ask_non_empty(prompt):
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("This field cannot be empty.")


def ask_age(prompt="Age: "):
    while True:
        try:
            age = int(input(prompt).strip())
            if 1 <= age <= 120:
                return age
            print("Age must be between 1 and 120.")
        except ValueError:
            print("Enter a whole number for age.")


def add_student(students):
    sid = ask_non_empty("Student ID: ")
    if any(s["sid"].casefold() == sid.casefold() for s in students):
        print("That student ID already exists.")
        return

    name = ask_non_empty("Name: ")
    age = ask_age()
    course = ask_non_empty("Course: ")

    stu = Student(sid, name, age, course)
    students.append(stu.to_dict())
    save_students(students)
    print("Student added successfully.")


def view_students(students):
    if not students:
        print("No students found.")
        return

    print("\n--- Student Records ---")
    for s in students:
        print(
            f'ID: {s["sid"]} | Name: {s["name"]} | '
            f'Age: {s["age"]} | Course: {s["course"]}'
        )


def search_student(students):
    sid = input("Enter student ID: ").strip()
    for s in students:
        if s["sid"].casefold() == sid.casefold():
            print(
                f'ID: {s["sid"]} | Name: {s["name"]} | '
                f'Age: {s["age"]} | Course: {s["course"]}'
            )
            return
    print("Student not found.")


def update_student(students):
    sid = input("Enter student ID to update: ").strip()

    for s in students:
        if s["sid"].casefold() != sid.casefold():
            continue

        print("Press Enter to keep the current value.")
        name = input(f'Name [{s["name"]}]: ').strip()
        age_in = input(f'Age [{s["age"]}]: ').strip()
        course = input(f'Course [{s["course"]}]: ').strip()

        # Validate age before changing any fields.
        new_age = s["age"]
        if age_in:
            try:
                new_age = int(age_in)
                if not 1 <= new_age <= 120:
                    raise ValueError
            except ValueError:
                print("Invalid age. No changes were saved.")
                return

        if name:
            s["name"] = name
        if course:
            s["course"] = course
        s["age"] = new_age

        save_students(students)
        print("Student updated successfully.")
        return

    print("Student not found.")


def delete_student(students):
    sid = input("Enter student ID to delete: ").strip()

    for index, stu in enumerate(students):
        if stu["sid"].casefold() == sid.casefold():
            print(f'Found: {stu["name"]} (ID: {stu["sid"]})')
            confirm = input("Delete this student? (y/n): ").strip().lower()
            if confirm == "y":
                students.pop(index)
                save_students(students)
                print("Student deleted successfully.")
            else:
                print("Deletion cancelled.")
            return

    print("Student not found.")


def main():
    try:
        students = load_students()
    except (OSError, ValueError) as exc:
        print(f"Could not load student records: {exc}")
        return

    actions = {
        "1": add_student,
        "2": view_students,
        "3": search_student,
        "4": update_student,
        "5": delete_student,
    }

    while True:
        print("\n=== Student Management System ===")
        print("1. Add student")
        print("2. View all students")
        print("3. Search student")
        print("4. Update student")
        print("5. Delete student")
        print("6. Exit")

        choice = input("Choose an option: ").strip()
        if choice == "6":
            print("Goodbye!")
            break

        action = actions.get(choice)
        if action is None:
            print("Invalid choice. Enter a number from 1 to 6.")
            continue

        try:
            action(students)
        except OSError as exc:
            print(f"File operation failed: {exc}")


if __name__ == "__main__":
    main()
