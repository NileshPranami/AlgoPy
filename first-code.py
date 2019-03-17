class Employee:

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first+'.'+last+'@gmail.com'

    def name(self):
        return '{} {}'.format(self.first, self.last)


emp1 = Employee('Nilesh','Pranami',200)
emp2 = Employee('ram', 'kumar', 322)

print(Employee.name(emp1))
print(emp1.email)
print(emp2.email)
