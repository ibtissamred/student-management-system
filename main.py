import sqlite3


def connect_database():
    return sqlite3.connect("students.db")


def create_table():
    connection = connect_database()
    cursor = connection.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER,
        major TEXT,
        year INTEGER,
        email TEXT,
        gpa REAL
    )
    """)

    connection.commit()
    connection.close()


def add_student():
    connection = connect_database()
    cursor = connection.cursor()

    print("\n===== Add Student =====")

    name = input("Enter student name: ")
    age = int(input("Enter student age: "))
    major = input("Enter student major: ")
    year = int(input("Enter student year: "))
    email = input("Enter student email: ")
    gpa = float(input("Enter student GPA: "))

    cursor.execute("""
    INSERT INTO students (name, age, major, year, email, gpa)
    VALUES (?, ?, ?, ?, ?, ?)
    """, (name, age, major, year, email, gpa))

    connection.commit()
    connection.close()

    print("\nStudent added successfully!")


def view_students():
    connection = connect_database()
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()

    print("\n===== All Students =====")

    if not students:
        print("No students found.")
    else:
        for student in students:
            print(
                f"ID: {student[0]} | "
                f"Name: {student[1]} | "
                f"Age: {student[2]} | "
                f"Major: {student[3]} | "
                f"Year: {student[4]} | "
                f"Email: {student[5]} | "
                f"GPA: {student[6]}"
            )

    connection.close()


def search_student():
    connection = connect_database()
    cursor = connection.cursor()

    print("\n===== Search Student =====")

    student_id = int(input("Enter student ID: "))

    cursor.execute(
        "SELECT * FROM students WHERE id = ?",
        (student_id,)
    )

    student = cursor.fetchone()

    if student:
        print("\nStudent Found:")
        print("ID:", student[0])
        print("Name:", student[1])
        print("Age:", student[2])
        print("Major:", student[3])
        print("Year:", student[4])
        print("Email:", student[5])
        print("GPA:", student[6])
    else:
        print("Student not found.")

    connection.close()


def update_student():
    connection = connect_database()
    cursor = connection.cursor()

    print("\n===== Update Student =====")

    student_id = int(input("Enter student ID: "))

    cursor.execute(
        "SELECT * FROM students WHERE id = ?",
        (student_id,)
    )

    student = cursor.fetchone()

    if not student:
        print("Student not found.")
        connection.close()
        return

    print("\nCurrent Student Information:")
    print("Name:", student[1])
    print("Age:", student[2])
    print("Major:", student[3])
    print("Year:", student[4])
    print("Email:", student[5])
    print("GPA:", student[6])

    print("\nEnter the new information:")

    name = input("Enter new name: ")
    age = int(input("Enter new age: "))
    major = input("Enter new major: ")
    year = int(input("Enter new year: "))
    email = input("Enter new email: ")
    gpa = float(input("Enter new GPA: "))

    cursor.execute("""
    UPDATE students
    SET name = ?, age = ?, major = ?, year = ?, email = ?, gpa = ?
    WHERE id = ?
    """, (name, age, major, year, email, gpa, student_id))

    connection.commit()
    connection.close()

    print("\nStudent information updated successfully!")


def delete_student():
    connection = connect_database()
    cursor = connection.cursor()

    print("\n===== Delete Student =====")

    student_id = int(input("Enter student ID: "))

    cursor.execute(
        "SELECT * FROM students WHERE id = ?",
        (student_id,)
    )

    student = cursor.fetchone()

    if not student:
        print("Student not found.")
        connection.close()
        return

    print("Student:", student[1])

    confirm = input("Are you sure you want to delete this student? (yes/no): ")

    if confirm.lower() == "yes":
        cursor.execute(
            "DELETE FROM students WHERE id = ?",
            (student_id,)
        )

        connection.commit()
        print("Student deleted successfully!")
    else:
        print("Deletion cancelled.")

    connection.close()


def main():
    print("\n================================")
    print("   WELCOME TO STUDENT SYSTEM")
    print("================================")

    create_table()

    while True:
        print("\n================================")
        print("     STUDENT MANAGEMENT SYSTEM")
        print("================================")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            update_student()
        elif choice == "5":
            delete_student()
        elif choice == "6":
            print("\nThank you for using the Student Management System!")
            break
        else:
            print("\nInvalid choice. Please try again.")


if __name__ == "__main__":
    main()