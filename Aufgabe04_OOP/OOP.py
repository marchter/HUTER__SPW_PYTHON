class Person:
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

class Employee(Person):
    def __init__(self, name, gender, department):
        super().__init__(name, gender)
        self.department = department

class Manager(Person):
    def __init__(self, name, gender, department):
        super().__init__(name, gender)
        self.department = department

class Department:
    def __init__(self, name):
        self.name = name
        self.employees = []
        self.manager = None

class Firma:
    def __init__(self):
        self.departments = []
        self.employees = []
        self.managers = []

    def instanciate(self, name, gender, department=None):
        if department is None:
            p = Person(name, gender)
        else:
            p = Employee(name, gender, department)
            self.employees.append(p)
        return p

    def get_employee_count(self):
        return len(self.employees)

    def get_manager_count(self):
        return len(self.managers)

    def get_department_count(self):
        return len(self.departments)

    def get_biggest_department(self):
        biggest = None
        for d in self.departments:
            if biggest is None or len(d.employees) > len(biggest.employees):
                biggest = d
        return biggest

    def get_gender_percentage(self):
        male = len([p for p in self.employees if p.gender == 'male'])
        female = len([p for p in self.employees if p.gender == 'female'])
        return {'male': male, 'female': female}

firma = Firma()

# Instantiiere Personen
p1 = firma.instanciate('Max', 'male')
p2 = firma.instanciate('Julia', 'female')
p3 = firma.instanciate('John', 'male')

# Instantiiere Abteilungen
d1 = Department('Marketing')
d2 = Department('Entwicklung')

# Instantiiere Mitarbeiter
e1 = firma.instanciate('Jenny', 'female', d1)
e2 = firma.instanciate('Frank', 'male', d2)
e3 = firma.instanciate('Huter', 'male', d2)

# Instantiiere Abteilungsleiter
m1 = Manager('Hans', 'male', d1)

# Füge Abteilung zur Firma hinzu
firma.departments.append(d1)
firma.departments.append(d2)
firma.departments.append(d2)

# Füge Abteilungsleiter zur Firma hinzu
firma.managers.append(m1)

# Füge Mitarbeiter zu Abteilung hinzu
d1.employees.append(e1)
d2.employees.append(e2)
d2.employees.append(e3)


# Füge Abteilungsleiter zu Abteilung hinzu
d1.manager = m1


# Ausgabe
print('Anzahl der Mitarbeiter: ', firma.get_employee_count())
print('Anzahl der Abteilungsleiter: ', firma.get_manager_count())
print('Anzahl der Abteilungen: ', firma.get_department_count())

biggest_department = firma.get_biggest_department()
if biggest_department is not None:
    print('Größte Abteilung: ', biggest_department.name)

gender_percentage = firma.get_gender_percentage()
print('Männlich/Weiblich: ', gender_percentage['male'], '/', gender_percentage['female'])