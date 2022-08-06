class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def __str__(self):
        print(f'Имя: {self.name}')
        print(f'Фамилия: {self.surname}')
        for grades in self.grades.values():
            avg_grade = sum(grades) / len(grades)
            print(f'Средняя оценка за домашнее задание: {float(avg_grade)}')
        print(f'Курсы в процессе обучения: {self.courses_in_progress}')

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer,
                      Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __str__(self):
        print(f'Имя: {self.name}')
        print(f'Фамилия: {self.surname}')
        for grades in self.grades.values():
            avg_grade = sum(grades) / len(grades)
            print(f'Средняя оценка за лекцию: {float(avg_grade)}')
            break


class Reviewer(Mentor):

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        print(f'Имя: {self.name}')
        print(f'Фамилия: {self.surname}')


# Блок для проверки
student1 = Student("Антон", "Ильич", "м")
student1.courses_in_progress += ["Python"]
student1.courses_in_progress += ["Git"]
student2 = Student("Егор", "Лошкарев", "м")
student2.courses_in_progress += ["Python"]

lecturer1 = Lecturer("Марина", "Калашникова")
lecturer1.courses_attached += ["Python"]
lecturer2 = Lecturer("Андрей", "Ильин")
lecturer2.courses_attached += ["Python"]

reviewer1 = Reviewer("Егор", "Морозов")
reviewer1.courses_attached += ["Python"]
reviewer2 = Reviewer("Владислав", "Котов")
reviewer2.courses_attached += ["Python"]

student1.rate_lecturer(lecturer1, "Python", 9)
student2.rate_lecturer(lecturer1, "Python", 8)

reviewer1.rate_hw(student1, "Python", 9)
reviewer2.rate_hw(student1, "Python", 8)

# print(lecturer1)
# print(reviewer1)
print(student1)
