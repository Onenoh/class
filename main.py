class Student:
    # [assignment] Skeleton class. Add your code here
    def __init__(self, name, age, tracks, score):
        self.name = name
        self.age = age
        self.tracks = tracks
        self.score = score

       
student = Student("Anthonia", "27", "General, Full Time", "99.07")
print(student.name)
print(student.age)
print(student.tracks)
print(student.score)

@classmethod
def change_name(cls):
    return cls('peter')
print(change_name)

def change_age(cls):
    return cls('27')
print(change_age)

def add_tracks(cls):
    return cls('FE','BE')
print(add_tracks)

def get_score(cls):
    return cls('get_score')
print(get_score)

#Bob = Student(name="Bob", age=26, tracks=["FE","BE"],score=20.90)

#Expected methods
#Bob.change_name("Peter")
#Bob.change_age(34)
#Bob.add_track("UI/UX")
#Bob.get_score()
