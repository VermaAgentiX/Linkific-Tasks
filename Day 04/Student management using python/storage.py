import json
from pathlib import Path

FILE = Path(__file__).with_name("students.json")


def load_students():
    """Load records from JSON, or return an empty list if the file is missing."""
    if not FILE.exists():
        return []

    try:
        with FILE.open("r", encoding="utf-8") as f:
            data = json.load(f)
    except json.JSONDecodeError as exc:
        raise ValueError(
            f"{FILE.name} contains invalid JSON. Fix it before continuing."
        ) from exc

    if not isinstance(data, list):
        raise ValueError(f"{FILE.name} must contain a JSON list.")

    for item in data:
        if not isinstance(item, dict):
            raise ValueError("Every student record must be a JSON object.")
        if not {"sid", "name", "age", "course"}.issubset(item):
            raise ValueError("A student record is missing required fields.")

    return data


def save_students(students):
    """Save student records to JSON."""
    with FILE.open("w", encoding="utf-8") as f:
        json.dump(students, f, indent=4, ensure_ascii=False)
        f.write("\n")
