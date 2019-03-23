class Employee:
    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first+'.'+last+'@gmail.com'

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

class Developer(Employee):
    def __init__(self,first,last,pay,lang):
        super().__init__(first,last,pay)
        self.lang = lang

class Manager(Employee):
    def __init__(self, first, last, pay, employee = None):
        super().__init__(first, last, pay)
        if employee is None:
            self.employee = []
        else:
            self.employee = employee


    def addEmployee(self,emp):
        if emp not in self.employee:
            self.employee.append(emp)
    
    def removeEmployee(self, emp):
        if emp in self.employee:
            self.employee.remove(emp)

    def printEmployee(self):
        for emp in self.employee:
            print('--> ',emp.fullname())


dev1 = Developer('Nilesh','Pranami',200,'Python')
dev2 = Developer('ram', 'kumar', 322,'Java')
mng = Manager('Rahul', 'Pranami', 10000,[dev1])
print(mng.email)

mng.printEmployee()

mng.addEmployee(dev2)
mng.printEmployee()

mng.removeEmployee(dev2)
mng.printEmployee()
#print(dev2.lang)
