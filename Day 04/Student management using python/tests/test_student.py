import unittest
from student import Student


class TestStudent(unittest.TestCase):
    def test_to_dict(self):
        stu = Student("S101", "Rahul", 22, "Python")
        self.assertEqual(stu.to_dict(), {
            "sid": "S101",
            "name": "Rahul",
            "age": 22,
            "course": "Python",
        })

    def test_from_dict(self):
        data = {
            "sid": "S102",
            "name": "Neha",
            "age": "21",
            "course": "AI",
        }
        stu = Student.from_dict(data)
        self.assertEqual(stu.age, 21)
        self.assertEqual(stu.name, "Neha")


if __name__ == "__main__":
    unittest.main()
