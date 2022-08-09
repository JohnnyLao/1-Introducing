class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def __str__(self):
        for grades in self.grades.values():
            result = f'Имя: {self.name} ' \
                     f'Фамилия: {self.surname} ' \
                     f'Средняя оценка за домашнее задание: {float(sum(grades) / len(grades))} ' \
                     f'Курсы в процессе: {" ".join(self.courses_in_progress)}'
            return result

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
        for grades in self.grades.values():
            result = f'Имя: {self.name} ' \
                     f'Фамилия: {self.surname} ' \
                     f'Средняя оценка за лекцию: {float(sum(grades) / len(grades))}'
            return result


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
        result = f'Имя: {self.name} ' \
                 f'Фамилия: {self.surname}'
        return result

def calc_avg_homework(student_list, course):
    for student in student_list:
        if course in student.courses_in_progress:
            for grades in student.grades.values():
                avg = float(sum(grades) / len(grades))
                print(avg)

    else:
        return "Ошибка"


def calc_avg_rate(lecturer_list, course):
    for lecturer in lecturer_list:
        if course in lecturer.courses_attached:
            for grades in lecturer.grades.values():
                avg = float(sum(grades) / len(grades))
                print(avg)
    else:
        return "Ошибка"


students = []
lecturers = []

# Блок для проверки

student1 = Student("Антон", "Ильич", "м")
student1.courses_in_progress += ["Python"]
student1.courses_in_progress += ["Git"]
student2 = Student("Егор", "Лошкарев", "м")
student2.courses_in_progress += ["Python"]
students.append(student1)
students.append(student2)

lecturer1 = Lecturer("Марина", "Калашникова")
lecturer1.courses_attached += ["Python"]
lecturer2 = Lecturer("Андрей", "Ильин")
lecturer2.courses_attached += ["Python"]
lecturers.append(lecturer1)
lecturers.append(lecturer2)

reviewer1 = Reviewer("Егор", "Морозов")
reviewer1.courses_attached += ["Python"]
reviewer2 = Reviewer("Владислав", "Котов")
reviewer2.courses_attached += ["Python"]

student1.rate_lecturer(lecturer1, "Python", 10)
student2.rate_lecturer(lecturer1, "Python", 8)

reviewer1.rate_hw(student1, "Python", 8)
reviewer2.rate_hw(student1, "Python", 9)


print(lecturer1)
print(reviewer1)
print(student1)

calc_avg_homework(students, "Python")
calc_avg_rate(lecturers, "Python")
