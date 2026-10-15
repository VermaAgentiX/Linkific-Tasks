class Student:
    """Represent one student record."""

    def __init__(self, sid, name, age, course):
        self.sid = sid
        self.name = name
        self.age = age
        self.course = course

    def to_dict(self):
        return {
            "sid": self.sid,
            "name": self.name,
            "age": self.age,
            "course": self.course,
        }

    @classmethod
    def from_dict(cls, data):
        return cls(data["sid"], data["name"], int(data["age"]), data["course"])
