import json

FileName = "students.json"

def load_data():
    try:
        # بيحاول يفتح الملف لو موجود
        with open(FileName, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        # لو الملف مش موجود أصلاً، أو موجود بس فاضي
        initial_data = {"students": []}
        # وننشئ الملف ونحفظ
        with open(FileName, "w") as file:
            json.dump(initial_data, file, indent=4)
        return initial_data

def save_data(data):
    with open(FileName, "w") as file:
        json.dump(data, file, indent=4)

# bouns
def log_action(message):
    with open("logs.txt", "a") as file:
        file.write(message + "\n")

def add_student():
    print("\nAdd Student")
    data = load_data()
    try:
        student_id = int(input("Enter Student ID: "))
    except ValueError:
        print("Error: ID must be a number!")
        return

    for u in data["students"]:  # unique id
        if u["id"] == student_id:
            print("Error: Student ID already exists!")
            return

    name = input("Enter Student Name: ").strip()
    try:
        age = int(input("Enter Student Age: "))
    except ValueError:
        print("Error: Age must be a number!")
        return

    track = input("Enter Student Track: ").strip()
    student = {
        "id": student_id,
        "name": name,
        "age": age,
        "track": track
    }
    data["students"].append(student)
    save_data(data)
    log_action(f"Added student {student_id}")
    print("Student added successfully")

def view_students():
    print("\nView All Students")
    data = load_data()
    if not data["students"]:
        print("No students found.")
        return

    for u in data["students"]:
        print(f"ID: {u['id']} | Name: {u['name']} | Age: {u['age']} | Track: {u['track']}")

def search_student():
    print("\nSearch for Student")
    data = load_data()
    try:
        student_id = int(input("Enter Student ID to search: "))
    except ValueError:
        print("Error: ID must be a number!")
        return

    for u in data["students"]:
        if u["id"] == student_id:
            print(f"ID: {u['id']} | Name: {u['name']} | Age: {u['age']} | Track: {u['track']}")
            log_action(f"Searched for student {student_id}")
            return
    print("Student not found.")

def update_student():
    print("\nUpdate Student")
    try:
        student_id = int(input("Enter Student ID to update: "))
    except ValueError:
        print("Error: ID must be a number!")
        return

    data = load_data()

    for u in data["students"]:
        if u["id"] == student_id:
            name = input(f"Enter new name (current: {u['name']}): ").strip()
            if name:
                u["name"] = name

            age_input = input(f"Enter new age (current: {u['age']}): ").strip()
            if age_input:
                try:
                    u["age"] = int(age_input)
                except ValueError:
                    print("Error: Age must be a number! Keeping old age.")

            track = input(f"Enter new track (current: {u['track']}): ").strip()
            if track:
                u["track"] = track

            save_data(data)
            log_action(f"Updated student {student_id}")
            print("Student updated successfully!")
            return

    print("Student not found.")

def delete_student():
    print("\nDelete Student")
    try:
        student_id = int(input("Enter Student ID to delete: "))
    except ValueError:
        print("Error: ID must be a number!")
        return

    data = load_data()

    for u in data["students"]:
        if u["id"] == student_id:
            data["students"].remove(u)
            save_data(data)
            log_action(f"Deleted student {student_id}")
            print(f"Student with ID {student_id} deleted successfully!")
            return

    print("Student not found.")

def main():
    while True:
        print("\nStudent Management System")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search for Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ").strip()

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
            print("Goodbye!")
            break
        else:
            print("Invalid choice! Please choose between 1 and 6.")

if __name__ == "__main__":
    main()