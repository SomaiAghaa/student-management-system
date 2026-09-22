# Student Management System

A Python console application developed to manage student records efficiently. The system utilizes JSON for persistent data storage and implements strict input validation and error handling to ensure data integrity.

## Key Features

- **CRUD Operations**: Add, View, Search, Update, and Delete student records.
- **Persistent Storage**: Reads and writes structured data to `students.json`.
- **Robust Error Handling**: Handles non-numeric inputs, missing files, corrupted JSON data, and duplicate records without application termination.
- **Transaction Logging**: Automatically tracks and appends user operations to `logs.txt`.

## Tech Stack & Concepts

- **Language**: Python 3
- **File Handling**: Context managers (`with open`), file modes (`r`, `w`, `a`)
- **Data Serialization**: Built-in `json` module (`json.load`, `json.dump`)
- **Exception Handling**: `try`, `except`, `finally` constructs

## Getting Started

1. Clone the repository:
   ```bash
   git clone [https://github.com/your-username/student-management-system.git](https://github.com/your-username/student-management-system.git)
