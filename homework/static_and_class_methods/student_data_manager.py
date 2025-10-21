
class StudentDataManager:
    students = []

    def add_student(self, name: str) -> None:
        name = str(name)

        # Проверка наличия одинаковых студентов
        for std in StudentDataManager.students:
            if std[0] == name:
                print(f'Cтудент с именем {name} уже занесен в программу. Выберите другое имя.')
                return

        StudentDataManager.students.append([name, []])
        print(f'Студент {name} успешно занесен в программу.')

    def add_grades(self, student_name: str, student_grades: str) -> str:
        student_name = str(student_name).strip()
        if StudentDataManager.students == []:
            print('Студент не найден или еще небыл добавлен в программу.')
            return
            
        # Обработка и проверка оценок
        student_grades = str(student_grades).strip().split()
        sg_len_before = len(student_grades)
        student_grades = [int(sg) for sg in student_grades if StudentDataManager.is_valid_grade(int(sg))]
        sg_len_after = len(student_grades)
        
        for std in StudentDataManager.students:
            if std[0] == student_name:
                std[1].extend(student_grades)
                print(f'{sg_len_after} из {sg_len_before} оценок было добавленно. Некорректные оценки были проигнорированны. ')
                return
        
        print(f'Неправильный ввод или студент {student_name} не найден.')
        return

    def student_average_grade(self, student_name: str) -> int:
        if StudentDataManager.students == []:
            print('Студент не найден или еще небыл добавлен в программу.')
            return
        for std in StudentDataManager.students:
            if std[0] == student_name:
                if std[1] == []:
                    print(f'У студента {student_name} нет оценок. Добавьте оценки и повторите команду.')
                    return
                sum = 0
                for i in std[1]:
                    sum += i
                try:
                    return round(sum / len(std[1]))
                except ZeroDivisionError:
                    print(f'Студент {student_name} не имеет оценок.')

    @staticmethod
    def is_valid_grade(grade: int) -> bool:
        if isinstance(grade, int) and 0 < grade <= 5:
            return True
        else:
            return False

    @classmethod
    def all_students_average_grade(cls) -> int: 
        if StudentDataManager.students == []:
            print('Студенты еще не добавлены в программу.')
            return
        sum = 0
        cnt = 0
        std_len_valid = 0
        for std in StudentDataManager.students:
            if not std[1] == []:
                std_len_valid += 1
                for i in std[1]:
                    cnt += 1
                    sum += i
        try:
            result = round(sum / cnt)
            print(f'{std_len_valid} из {len(StudentDataManager.students)} студентов участвовало в расчете. Студенты без оценок проигнорированы.')
            print(f'Средняя оценка всех студентов: {result}')
            return result
            
        except ZeroDivisionError:
            print('В программе еще нет студентов с оценками.')
        


if __name__ == '__main__':
    print('Добро пожаловать в программу "Менеджмент оценок студентов".')
    obj_std = StudentDataManager()
        
    while True:
        print()
        print('Список доступных команд: ')
        print('1. Добавить нового студента.')
        print('2. Добавить оценки студенту.')
        print('3. Вывести среднюю оценку студента.')
        print('4. Вывести среднюю оценку всех добавленных студентов.')
        print('5. Закрыть программу.')
        user_input = input('Введите команду: ')
        print()
        if user_input == '1':
            user_input = input('Введите имя студента: ')
            obj_std.add_student(user_input)
            continue
        elif user_input == '2':
            user_input = input('Введите имя студента для добавления оценок: ')
            student_grades = input('Оценка должна быть числом от 1 до 5 включительно.\nВведите через пробел список оценок: ')
            obj_std.add_grades(user_input, student_grades)
            continue
        elif user_input == '3':
            user_input = input('Введите имя студента для расчета оценок: ')
            obj_std.student_average_grade(user_input)
            continue
        elif user_input == '4':
            StudentDataManager.all_students_average_grade()
            continue
        elif user_input == '5':
            print('До встречи!')
            exit()
        else:
            print('Ошибка ввода')
            continue
