class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f'{self.name}, {self.age}'

class Patient(Person):
    def __init__(self, name, age, disease):
        super().__init__(name, age)
        self.disease = disease

    def __add__(self, other):
        PatientGroup([self, other])

    def __str__(self):
        tmp = super().__str__()
        return f'Пациент {tmp}. Заболевание: {self.disease}.'

class PatientGroup:
    def __init__(self, patients):
        self.patients = patients

    def __str__(self):
        return f'Группа пациентов: {''.join(p.name for p in self.patients)}'

class Doctor(Person):
    def __init__(self, name, age, specialization):
        super().__init__(name, age)
        self.specialization = specialization
        self.procedure_count = 0

    def perform_procedure(self, patient):
        raise NotImplementedError('Метод не был переопределен.')

    def __gt__(self, other):
        return self.procedure_count > other.procedure_count

    def __str__(self):
        tmp = super().__str__()
        return f'Врач: {tmp}. Специализация: {self.specialization}. Кол-во пр-дур: {self.procedure_count}'

class Procedure:
    def __init__(self, name, doctor, patient):
        self.name = name
        self.doctor = doctor
        self.patient = patient

    def __str__(self):
        return f'Процедура: {self.name}, Доктор: {self.doctor.name}, Пациент: {self.patient.name}.'

class Therapist(Doctor):
    def __init__(self, name, doctor):
        super().__init__(name, doctor,'Терапевт')

    def perform_procedure(self, patient):
        print(f'{self.specialization} {self.name} проводит {patient.name}.')
        self.procedure_count += 1
        return Procedure('Терапия', self, patient)

    def __str__(self):
        return f''

tr1 = Therapist('Какойтов И. А.', 45,)
tr2 = Therapist('Петров B. И.', 25,)

pt1 = Patient('Алексеев Т. В.', 11, 'Аритмия')
pt2 = Patient('Александров Б. Ю', 45, 'Ступор мозговины')

pr1 = tr1.perform_procedure(pt1)
pr2 = tr2.perform_procedure(pt1)
pr3 = tr2.perform_procedure(pr2)

group = pt1 + pt2
print(group)

print(tr1 > tr2)

