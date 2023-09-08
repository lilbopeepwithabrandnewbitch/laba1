# Определение структуры student
class Student:
    def __init__(self, first_name, last_name, age, facult):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.facult = facult
# Функция для поиска студента по параметрам
def find_student(students, first_name, last_name):
    for student in students:
        if student.first_name == first_name and student.last_name == last_name:
            return student
    return None

# Пример списка студентов
students = [
    Student("Иван", "Иванов", 20, "факультет вычислительной техники"),
    Student("Петр", "Петров", 22, "Факультет экономики и управления"),
    Student("Мария", "Сидорова", 19, "Юридический факультет")
]

# Заданные параметры для поиска
search_first_name = input("Введите имя студента: ")
search_last_name = input("Введите фамилию студента: ")

# Вызываем функцию поиска
found_student = find_student(students, search_first_name, search_last_name)

if found_student:
    print(f"Студент найден: {found_student.first_name} {found_student.last_name}, возраст {found_student.age} лет, {found_student.facult}")
else:
    print("Студент с заданными параметрами не найден")
