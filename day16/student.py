class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        self.grades=[]
    def add_grades(self,grade):
        self.grades.append(grade)
    def get_average_grade(self):
        avg=sum(self.grades)/len(self.grades)
        return avg
name=input("Enter name:")
age=int(input("Enter age:"))
example=Student(name,age)
example.add_grades(100)
example.add_grades(80)
example.add_grades(95)
print(f"Average grade is {example.get_average_grade()}")