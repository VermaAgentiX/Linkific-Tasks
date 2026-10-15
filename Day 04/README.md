# Student Management using Python

A command-line student management application built with Python and JSON file storage. Records persist after the application closes.

## Features
- Add students with unique IDs
- View all student records
- Search by student ID
- Update a student's name, age, or course
- Delete a student with confirmation
- Persist records in `students.json`
- Validate required fields and age
- Handle missing or invalid JSON files

## Technology
Python 3, OOP, functions, modules, lists, dictionaries, JSON, file handling, and exception handling.

## Project structure
```text
student-management-cli/
├── main.py
├── student.py
├── storage.py
├── students.json
├── tests/
│   └── test_student.py
├── README.md
└── .gitignore
```

## Run
1. Install Python 3.
2. Open this folder in VS Code.
3. Run `python main.py` in the terminal.

No third-party packages are required.

## Menu
1. Add student
2. View all students
3. Search student
4. Update student
5. Delete student
6. Exit

## Data format
Records are stored as a JSON list in `students.json`.

## Run tests
```bash
python -m unittest discover -s tests -v
```

## Upload to GitHub
```bash
git status
git add main.py student.py storage.py students.json tests README.md .gitignore
git commit -m "Add student management CLI"
git push
```
If Git says this folder is not a repository, open your existing repository folder in VS Code first or connect this folder to your GitHub repository.

## Learning outcomes
Practised classes, constructors, functions, loops, modules, JSON serialization, file operations, input validation, and exception handling.

> Use fictional sample records only in a public repository. Do not commit real student personal information.
