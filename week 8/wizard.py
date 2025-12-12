class Wizard:
    def __init__(self, name):
        if not name:
            raise ValueError("no name")
        self.name = name
    ...


        

class Student(Wizard):
    def __init__(self, name, house):
        super().__init__(name)
        self.house = house



class Professor(Wizard):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject

student = Student("harry", "gry")
professor = Professor("severus", "defence")
wizard = Wizard("name")