class Student:
    instance_list = []    
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.__class__.instance_list.append(self)

    def rate_lecture(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
                return 'Ошибка'
            
    def __str__(self):
        return (f"Имя: {self.name}\n"
                f"Фамилия: {self.surname}\n"
                f"Cредняя оценка за домашние задания: {average_grade(self)}\n"
                f"Курсы вы процессе обучения: {(', '.join(self.courses_in_progress))}\n"
                f"Завершенные курсы: {(', '.join(self.finished_courses))}")
    
    def __lt__(self, other):
        if not isinstance(other, Student) and not self.grades and not other.grades:
            return 'нечего сравнивать'
        return average_grade(self) < average_grade(other)

    def __le__(self, other):
        if not isinstance(other, Student) and not self.grades and not other.grades:
            return 'нечего сравнивать'
        return average_grade(self) <= average_grade(other)

    def __eq__(self, other):
        if not isinstance(other, Student) and not self.grades and not other.grades:
            return 'нечего сравнивать'
        return average_grade(self) == average_grade(other)
    
    def add_courses(self, course_name):
        self.finished_courses.append(course_name)            
        
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    instance_list = []
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
        self.__class__.instance_list.append(self)

    def __str__(self):    
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {average_grade(self)}"

    def __lt__(self, other):
        if not isinstance(other, Lecturer) and not self.grades and not other.grades:
            return 'нечего сравнивать'
        return average_grade(self) < average_grade(other)

    def __le__(self, other):
        if not isinstance(other, Lecturer) and not self.grades and not other.grades:
            return 'нечего сравнивать'
        return average_grade(self) <= average_grade(other)

    def __eq__(self, other):
        if not isinstance(other, Lecturer) and not self.grades and not other.grades:
            return 'нечего сравнивать'
        return average_grade(self) == average_grade(other)   

class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
    
    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}"
    
def average_grade(self):
    if self.grades:
        return sum([sum(i) for i in self.grades.values()]) / sum([len(i) for i in self.grades.values()])
    else:
        return 'Оценок нет!'

def average_grade_students(students_list, course):
    result = 0
    count = 0
    for s in students_list:
        if course in s.courses_in_progress and course in s.grades:
            result += sum(s.grades[course]) / len(s.grades[course])
            count += 1
    if count:
        return f'Средняя оценка студентов за курс: {course} - {result / count}'
    else:
        return 'нет данных для сравнения'

def average_grade_lecturers(lecturers_list, course):
    result = 0
    count = 0
    for s in lecturers_list:
        if course in s.courses_attached and course in s.grades:
            result += sum(s.grades[course]) / len(s.grades[course])
            count += 1
    if count:
        return f'Средняя оценка лекторов за курс: {course} - {result / count}'
    else:
        return 'нет данных для сравнения'            
    
f_lecturer = Lecturer('Job', 'St')
s_lecturer = Lecturer('Lola', 'Gr')
f_lecturer.courses_attached += ['Python']
f_lecturer.courses_attached += ['Git']
s_lecturer.courses_attached += ['Python']
s_lecturer.courses_attached += ['Git']

f_reviewer = Reviewer('Julia', 'An')
s_reviewer = Reviewer('Daria', 'Nn')
f_reviewer.courses_attached += ['Python']
f_reviewer.courses_attached += ['Git']
s_reviewer.courses_attached += ['Python']
s_reviewer.courses_attached += ['Git']

f_student = Student('One','Jan', 'male')
f_student.courses_in_progress += ['Python']
f_student.courses_in_progress += ['Git']
f_student.finished_courses += ['Введение в программирование']

s_student = Student('Two','Feb', 'female')
s_student.courses_in_progress += ['Python']
s_student.courses_in_progress += ['Git']
s_student.finished_courses += ['Введение в программирование']

f_student.rate_lecture(f_lecturer, 'Python', 10)
f_student.rate_lecture(s_lecturer, 'Python', 9)
f_student.rate_lecture(f_lecturer, 'Git', 9)
f_student.rate_lecture(s_lecturer, 'Git', 10)

s_student.rate_lecture(f_lecturer, 'Python', 8)
s_student.rate_lecture(s_lecturer, 'Python', 7)
s_student.rate_lecture(f_lecturer, 'Git', 6)
s_student.rate_lecture(s_lecturer, 'Git', 5)

f_reviewer.rate_hw(f_student, 'Python', 10)
s_reviewer.rate_hw(f_student, 'Git', 10)
f_reviewer.rate_hw(s_student, 'Python', 8)
s_reviewer.rate_hw(s_student, 'Git', 8)
f_reviewer.rate_hw(f_student, 'Python', 10)
s_reviewer.rate_hw(f_student, 'Git', 10)
f_reviewer.rate_hw(s_student, 'Python', 8)
s_reviewer.rate_hw(s_student, 'Git', 8)

print(f_student)
print(s_student)
print(f_lecturer)
print(s_lecturer)

print(average_grade_students(Student.instance_list, 'Python'))
print(average_grade_lecturers(Lecturer.instance_list, 'Git'))

print(f_student < s_student)
print(f_student > s_student)
print(f_student <= s_student)
print(f_lecturer < s_lecturer)
print(f_lecturer > s_lecturer)
print(f_lecturer >= s_lecturer)
print(f_student == s_student)
print(f_lecturer != s_lecturer)