from module import *
from moduleElement import *

class Student(object):

    def __init__(self, name):
        ######## CODE MISSING HERE
        self.name = name
        self.modules = []
        self.grades = {}

    def add_module(self,module):
        ######## CODE MISSING HERE
        self.modules.append(title)
        self.grades[title] = title.get_grade()


    def get_list_modules(self):
        ######## CODE MISSING HERE
        print("Modules of student Tran Phan:")
        for module in self.modules:
            print(module)

    def get_grades(self):
        ######## CODE MISSING HERE
        print("Grades of student Tran Phan:")
        for grade in self.grades:
            print("%s: %s" % (grade, self.grades[grade]))

### test cases ###

me = Student("FirstName LastName")
me.add_module(info1)
me.get_list_modules()
# expected output:
# Modules of Student FirstName LastName:
#	Info 1

me.get_grades()
# expected output:
# Grades of Student FirstName LastName:
#	Info 1: 6