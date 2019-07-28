# Задание-1:
# Реализуйте описаную ниже задачу, используя парадигмы ООП:
# В школе есть Классы(5А, 7Б и т.д.), в которых учатся Ученики.
# У каждого ученика есть два Родителя(мама и папа).
# Также в школе преподают Учителя. Один учитель может преподавать 
# в неограниченном кол-ве классов свой определенный предмет. 
# Т.е. Учитель Иванов может преподавать математику у 5А и 6Б,
# но больше математику не может преподавать никто другой.


class ClassRoom:
    def __init__(self, class_room):
        self.class_room = {
            'class_num': int(class_room.split()[0]),
            'class_letter': class_room.split()[1]
        }

    def get_name(self):
        return str(self.class_room['class_num']) + ' ' + self.class_room['class_letter']


class Person:
    def __init__(self, name, surname, father_name, birth_date):
        self.name = name
        self.surname = surname
        self.father_name = father_name
        self.birth_date = birth_date

    def get_full_name(self):
        return self.surname + ' ' + self.name[:1] + '.' + self.father_name[:1] + '.'


class Student(Person):
    def __init__(self, name, surname, father_name, birth_date, class_room, father, mother):
        Person.__init__(self, name, surname, father_name, birth_date)
        self.class_room = class_room
        self.father = father
        self.mother = mother

    def get_class_room(self):
        return self.class_room

    def get_parents(self):
        return self.father.get_full_name(), self.mother.get_full_name()


class Teacher(Person):
    def __init__(self, name, surname, father_name, birth_date, classes, subject):
        Person.__init__(self, name, surname, father_name, birth_date)
        self.classes = classes
        self.subject = subject

    def get_subject(self):
        return self.subject

    def get_classes(self):
        return self.classes


class_rooms = ['5 А', '4 В', '8 Б']

parents = [Person("Иван", "Сидоров", "Игоревич", "11.08.1981"),
           Person("Татьяна", "Сидорова", "Максимовна", "15.08.1983"),
           Person("Игорь", "Иванов", "Александрович", "11.08.1981"),
           Person("Ирина", "Иванова", "Александровна", "11.08.1981"),
           Person("Николай", "Петров", "Александрович", "11.08.1981"),
           Person("Светлана", "Петрова", "Николаевна", "11.08.1981")]

students = [Student("Александр", "Иванов", "Игоревич", '10.11.1998', class_rooms[0], parents[2], parents[3]),
            Student("Петр", "Сидоров", 'Иванович', '10.01.1995', class_rooms[2], parents[0], parents[1]),
            Student("Иван", "Петров", 'Николаевич', '12.11.1999', class_rooms[1], parents[4], parents[5])]

teachers = [Teacher("Иван", "Сидоров", "Игоревич", "11.08.1981", [class_rooms[0], class_rooms[1]], 'Математика'),
            Teacher("Игорь", "Иванов", "Александрович", "15.08.1983", [class_rooms[2], class_rooms[1]], 'История'),
            Teacher("Николай", "Петров", "Александрович", "11.08.1981", [class_rooms[0], class_rooms[2]], 'Английский')]


# Выбранная и заполненная данными структура должна решать следующие задачи:
# 1. Получить полный список всех классов школы
# 2. Получить список всех учеников в указанном классе
#  (каждый ученик отображается в формате "Фамилия И.О.")
# 3. Получить список всех предметов указанного ученика
#  (Ученик --> Класс --> Учителя --> Предметы)
# 4. Узнать ФИО родителей указанного ученика
# 5. Получить список всех Учителей, преподающих в указанном классе

print('1. Список классов в школе: ')
for a in class_rooms:
    print(a)

for b in class_rooms:
    print("2. Ученики в классе {}:".format(b))
    print([x.get_full_name() for x in students if x.get_class_room() == b])

for c in students:
    print("3. Предметы ученика {}:".format(c.get_full_name()))
    print([y.subject for y in [z for z in teachers if c.get_class_room() in z.get_classes()]])

for d in students:
   print("4. Родители учеников {}:".format(d.get_full_name()))
   print(d.get_parents())

for f in class_rooms:
  print('5. Учителя, преподающие в {} классе:'.format(f))
  print([q.get_full_name() for q in teachers if f in q.get_classes()])

