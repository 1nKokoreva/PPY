import csv


class Student:
    def __init__(self, email, name, surname, points, grade='', status=''):
        self.email = email
        self.name = name
        self.surname = surname
        self.points = float(points)
        self.grade = grade
        self.status = status

    def __str__(self):
        return f"{self.email}, {self.name}, {self.surname}, {self.points}, {self.grade}, {self.status}"

    def set_grade(self, grade):
        self.grade = grade

    def set_status(self, status):
        self.status = status


class MySortedList(list):
    def insert_sorted(self, student):
        for i, element in enumerate(self):
            if element.points < student.points:
                self.insert(i, student)
                return
        self.append(student)


students = MySortedList()
filepath = "example.txt"


def load_students_data(filepath):
    with open(filepath) as file_object:
        for line in file_object:
            row = line.strip().split(',')
            email = row[0]
            grade = row[4] if len(row) > 4 else ''
            status = row[5] if len(row) > 5 else ''
            student = Student(email, row[1], row[2], row[3], grade, status)
            students.insert_sorted(student)


load_students_data(filepath)
# for student in students:
#     print(student)
# print([student.email for student in students])


def save_students_data(filepath):
    with open(filepath, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        for student in students:
            writer.writerow(
                [student.email, student.name, student.surname, student.points, student.grade, student.status])


"""
Umożliwi automatyczne wystawianie oceny wszystkim studentom, którzy jeszcze nie mają wystawionej oceny (status
różny od GRADED oraz MAILED), zgodnie z punktacją zaproponowaną w regulaminie zaliczenia przedmiotu
50 i mniej 2
51-60 pkt 3
61-70 pkt 3.5
71-80 pkt 4
81-90 pkt 4.5
91-100 pkt 5
"""


def wstawienie_ocen():
    for student in students:
        if student.status not in ['GRADED', 'MAILED']:
            punkty = student.points
            if punkty <= 50:
                student.set_grade('2')
            elif punkty <= 60:
                student.set_grade('3')
            elif punkty <= 70:
                student.set_grade('3.5')
            elif punkty <= 80:
                student.set_grade('4')
            elif punkty <= 90:
                student.set_grade('4.5')
            else:
                student.set_grade('5')
            student.set_status('GRADED')


"""
Umożliwi usuwanie oraz dodawanie studentów ręcznie (sprawdzanie czy email jest już zajęty)
"""


def manage_students_data(action='add', email='', name='', surname='', points=0):
    if action == 'add':
        for student in students:
            if student.email == email:
                print('Student with this email already exists.')
                return
        student = Student(email, name, surname, points)
        students.insert_sorted(student)
        save_students_data('students.csv')
    elif action == 'remove':
        for i, student in enumerate(students):
            if student.email == email:
                del students[i]
                save_students_data('students.csv')
                return
        print('Student not found.')
