# laajennetaan esimerkkiä
# Opiskelija kuuluu tietylle kursille
# Kurssit kuuluu tietylle koululle

'''

1. tehdään 3 opiskelijaa
2. luodaan kolme kurssia, kursseihin 1 ja 2 lisätään opiskelijoita
3. viimeisenä 2 koulua, Metropolia ja Laurea, molemmat saa yhden kurssin

'''
# kurssi toimii omana luokkanaan
# kurssilla on: nimi, lista opiskelijoista
class Course:

    def __init__(self, name, teacher):
        self.name = name
        self.students = []
        self.teacher = teacher

    def check_coursename(self):
        print(f"Kurssin nimi on: {self.name}")

    def get_course_info(self):
        return f"Kurssin nimi on: {self.name}\nOpettaja: {self.teacher.name}"
    def check_students_on_course(self):
        for student in self.students:
            print(student.name)

    def add_student(self, student):
        self.students.append(student)

    def remove_student(self, student):
        self.students.remove(student)

    def add_credits_to_all(self, credit_units):
        for student in self.students:
            # kutsutaan Student-olion metodeja
            student.add_credits(credit_units)
            student.say_hello()

class Student:

    count = 0

    def __init__(self, name, age=18): # age oletusarvo 15, jollei määritelty kutsussa
        self.name = name
        self.age = age
        self.credits = 0
        Student.count += 1
        # print(f"Uusi opiskelija luotu. Opiskelijoita on nyt yhteensä {Student.count}.")

    def say_hello(self):
        print(f"Morjes! Olen {self.name}, {self.age} vuotta. "
              f"Minulla on {self.credits} opintopistettä.")

    def change_name(self, new_name):
        self.name = new_name

    def add_credits(self, credits):
        # estä opintopisteiden menemine negatiiviseksi
        if self.credits + credits < 0:
            self.credits = 0
        else:
            self.credits = self.credits + credits


class Teacher:
    def __init__(self, name, id_number):
        self.name = name
        self.id_number = id_number

    def say_hello(self):
        print(f"Morjes! Olen opettaja {self.name}")

# luodaan koulut
class School:

    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.courses = []

    def add_course(self, course):
        self.courses.append(course)

    def remove_course(self, course):
        self.courses.remove(course)

    def fire_alarm(self):
        print(f"Koululla: {self.name}, lokaatiossa: {self.location} on palohälytys.")
        for course in self.courses:
            print(f"Kurssit käynnissä: {course.name}")
            print("Opiskelijat kurssilla:")
            course.check_students_on_course()


print("Hei, tervetuloa kouluun!")

# luodaan kolme opiskelijaa ja annetaan opintopisteet
student1 = Student("Mikko Mallikas", 38)
student1.add_credits(6)
student1.say_hello()

student2 = Student("Iines Ankka", 23)
student2.add_credits(3)
student2.say_hello()

student3 = Student("Risto Reipas", 30)
student3.add_credits(15)
student3.say_hello()

print(f"Uusi opiskelijoita on nyt {Student.count}.")
print("*========*")

# luodaan opettaja koska se vaaditaan kurssin luomiseksi

teacher1 = Teacher("Kaisa Katti", 5354)
# luodaan kaksi kurssia, tsekataan kurssin nimi (metodi)
course1 = Course("Ohjelmisto 1", teacher1)
course1.check_coursename()

# lisätään oppilaat kursseille
# Mikko ja Iines ovat Ohjelmisto 1 kurssilla
# Iines ja Risto ovat ohjelmisto 2 kurssilla

course1.students.append(student1)
course1.students.append(student2)
course1.check_students_on_course()
print("*========*")
# parempi tap aon käyttää metodeja tähän toimintoon
# Student-olio (tai oikeastaan viittaus siihen) annetaan metodikutsun parametrina
course2 = Course("Ohjelmisto 2", teacher1)
course2.check_coursename()

course2.add_student(student2)
course2.add_student(student3)
course2.check_students_on_course()
print("*========*")

# oppilaat ovat kurssilla 2 tosi ahkeria ja saavat lisää opintopisteitä
course2.add_credits_to_all(5)
print("*========*")

# laajennetaan esimerkkiä niin että luodaan kaksi koulua

school1 = School("Metropolia", "Karamalmi")
school2 = School("Laurea", "Leppävaara")

school1.add_course(course1)
school2.add_course(course2)

school1.fire_alarm()

# haetaan kurssin info

print(course1.get_course_info())