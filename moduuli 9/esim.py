class Student:

    count = 0
    def __init__(self, name, age=0): # age oletusarvo 15, jollei määritelty kutsussa
        self.name = name
        self.age  = age
        self.credits = 0
        Student.count += 1
        print(f"Uusi opiskelija luotu. Opiskelijoita on nyt yhteensä {Student.count}.")

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


student1 = Student("Mikko Mallikas", 38)
student1.say_hello()
student1.change_name("Kalle")
student1.say_hello()

student2 = Student("Iines Ankka", 60)
student2.say_hello()

student1.add_credits(6)
student2.add_credits(3)
student1.add_credits(15)

student1.say_hello()
student2.say_hello()

print("*========*")
# Luodaan 10 uutta opiskelijaa lisää ja tallenetaan viittaukset listaan
students = []
for i in range(10):
    new_student = Student("Opiskelija " + str(i))
    new_student.add_credits(30)
    students.append(new_student)
students.append(student1)
students.append(student2)
# käydään kaikki listalla olevat opiskelijat läpi
for student in students:
    student.say_hello()