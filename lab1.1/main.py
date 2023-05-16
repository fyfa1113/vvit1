groupmates = [
    {
        "name": "Александр",
        "surname": "Александров",
        "exams": ["Информатика", "ЭЭиС", "Web"],
        "marks": [4, 3, 5]
    },
    {
        "name": "Александр1",
        "surname": "Александров",
        "exams": ["История", "АиГ", "КТП"],
        "marks": [4, 4, 4]
    },
    {
        "name": "Александр2",
        "surname": "Александров",
        "exams": ["Философия", "ИС", "КТП"],
        "marks": [5, 5, 5]
    }
]


def print_students(students):
    mark = int(input("Введите оценку: "))
    if mark > 0:
        print(u"Имя".ljust(15), u"Фамилия".ljust(10), u"Экзамены".ljust(35), u"Оценки".ljust(15))
        for student in students:
            if sum(student["marks"]) / len(student["marks"]) > mark:
                print(student["name"].ljust(15), student["surname"].ljust(10), str(student["exams"]).ljust(35),
                      str(student["marks"]).ljust(15))


print_students(groupmates)
