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

dev1 = Developer('Nilesh','Pranami',200,'Python')
dev2 = Developer('ram', 'kumar', 322,'Java')

print(dev2.email)

print(dev2.lang)
