class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecture(self, lecturer, course, grade_l):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached:
            if course in lecturer.rate_l:
                if type(grade_l) == int and 0 <= grade_l <= 10:
                    lecturer.rate_l[course] += [grade_l]
                else:
                    lecturer.rate_l[course] = [grade_l]
            else:
                return 'Ошибка'
            
    def __str__(self):
        sum_grade = sum(self.grades.values())
        len_grade = len(self.grades)
        average_grade = sum_grade / len_grade 
        return (f"Имя: {self.name}\n"
                f"Фамилия: {self.surname}\n"
                f"Cредняя оценка за домашние задания: {average_grade}\n"
                f"Курсы вы процессе обучения: {(', '.join(self.courses_in_progress))}\n"
                f"Завершенные курсы: {(', '.join(self.finished_courses))}")
    
    def __lt__(self, other):
        if not isinstance(other, Student): 
            return
        if (sum(other.grades.values()) / len(other.grades)) < (sum(self.grades.values()) / len(self.grades)):
            other.status = 'Средняя оценка ниже'
            self.status = 'Средняя оценка выше'
        else:
            other.status = 'Средняя оценка выше'
            self.status = 'Средняя оценка ниже'
        
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.rate_l = {}

    def __str__(self):    
        sum_rate = sum(self.rate_l.values())
        len_rate = len(self.rate_l)
        average_rate_l = sum_rate / len_rate
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {average_rate_l}"

    def __lt__(self, other):
        if not isinstance(other, Lecturer): 
            return
        sum_other = sum(other.rate_l.values())
        len_other = len(other.rate_l)
        sum_self = sum(self.rate_l.values())
        len_self = len(self.rate_l)
        if (sum_other / len_other) < (sum_self / len_self):
            return f"Средняя оценка ниже"             
        else:
            return f"Средняя оценка выше"      

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
        return f"Имя: {self.name}\nФамилия: {self.surname}"
    
f_lecturer = Lecturer('Job', 'St')
s_lecturer = Lecturer('Lola', 'Gr')

f_reviewer = Reviewer('Julia', 'An')
s_reviewer = Reviewer('Daria', 'Nn')

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

students = [f_student, s_student]
all_grades_in_course = []


print(f_lecturer)
# print(f_reviewer)

# best_student = Student('Ruoy', 'Eman', 'your_gender')
# best_student.courses_in_progress += ['Python']
 
# cool_mentor = Mentor('Some', 'Buddy')
# cool_mentor.courses_attached += ['Python']
 
# cool_mentor.rate_hw(best_student, 'Python', 10)
# cool_mentor.rate_hw(best_student, 'Python', 10)
# cool_mentor.rate_hw(best_student, 'Python', 10)
 
# print(first_student.grades)