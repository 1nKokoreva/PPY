"""
 Wczyta z pliku dane dotyczące studentów email, imię, nazwisko
oraz liczbę uzyskanych punktów z przedmiotu Podstawy Programowania Python.
Dodatkowo w pliku mogą znajdować się w tej samej linii dane dotyczące oceny końcowej
oraz statusu (‘’, GRADED, MAILED). Zakładamy, że plik istnieje może być pusty lub zawiera podstawowe informacje: email, imię, nazwisko, punkty.
Do przechowywania danych w programie użyj słownika oraz zagnieżdżania
"""
import csv
import smtplib
from email.mime.text import MIMEText

from Tools.demo.mcast import sender

student = {}
filepath = "students.txt"
def load_students_data(filepath):
    with open(filepath) as file_object:
        for line in file_object:
            row = line.strip().split(',') #dziala na copji
            email = row[0]
            if email not in student:
                student[email] = {}
                student[email]['imie'] = row[1]
                student[email]['nazwisko'] = row[2]
                student[email]['punkty'] = float(row[3])
                student[email]['grade'] = ''
                student[email]['status'] = ''
                if len(row) > 4:
                    student[email]['grade'] = row[4]
                    student[email]['status'] = row[5]

load_students_data(filepath)
for value in student.values():
    print(value)
print(student.keys())

def save_students_data(filepath):
    with open(filepath, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        for email, data in student.items():
            writer.writerow([email, data['imie'], data['nazwisko'], data['punkty'], data['grade'], data['status']])

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
    for email, data in student.items():
        if data['status'] not in ['GRADED', 'MAILED']:
            punkty = data['punkty']
            if punkty <= 50:
                data['grade'] = '2'
            elif punkty <= 60:
                data['grade'] = '3'
            elif punkty <= 70:
                data['grade'] = '3.5'
            elif punkty <= 80:
                data['grade'] = '4'
            elif punkty <= 90:
                data['grade'] = '4.5'
            else:
                data['grade'] = '5'
            data['status'] = 'GRADED'

"""
Umożliwi usuwanie oraz dodawanie studentów ręcznie (sprawdzanie czy email jest już zajęty)
"""
def manage_students_data(action = 'add', email='', name='', surname='', points=0):
    if action == 'add':
        if email in student:
            print('Student with this email already exists.')
        else:
            student[email] = {}
            student[email]['name'] = name
            student[email]['surname'] = surname
            student[email]['points'] = float(points)
            student[email]['grade'] = ''
            student[email]['status'] = ''
            save_students_data('students.csv')
    elif action == 'remove':
        if email in student:
            del student[email]
            save_students_data('students.csv')
        else:
            print('Student with this email does not exist.')

#Umożliwi wysyłanie emaila z informacją o wystawionej ocenie wszystkim studentom ze statusem innym niż MAILED

def send_email(email, grade):
    for e in student and student[email]['status'] != 'MAILED':
        data = student[email]
        data['grade'] = grade
        data['status'] = 'MAILED'
        save_students_data('students.csv')
        msg = MIMEText('Dear {0} {1}, your grade for the Python Programming Basics course is {2}.'.format(data['name'],
                 data['surname'], grade))
        msg['Subject'] = 'Python Programming Basics - Grade'
        msg['From'] = 'example@example.com'
        msg['To']  = ', '.join(email)
        smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        smtp_server.login("natkokr@gmail.com", "ldzvulscsaoclyku")
        smtp_server.sendmail("natkokr@gmail.com", msg.as_string())
        smtp_server.quit()

# def send_email(subject, body, sender, recipients, password):
#     msg = MIMEText(body)
#     msg['Subject'] = subject
#     msg['From'] = sender
#     msg['To'] = ', '.join(recipients)
#     smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
#     smtp_server.login(sender, password)
#     smtp_server.sendmail(sender, recipients, msg.as_string())
#     smtp_server.quit()
#
#
# subject = "Email wysłany z Python'a"
# body = "To jest wiadomość wysłana za pomocą SMTP" \
#        "Pozdrawiam" \
#        "Nadzeya K. *-* hehehehehehhe"
# sender = "natkokr@gmail.com"
# #recipients = ["nadya.kokoreva.2016@mail.ru"]
# password = "ldzvulscsaoclyku"
# send_email(subject, body, sender, "kokoreva.dasha.dk@gmail.com", password)
