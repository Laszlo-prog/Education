class EmploYees:

    num_of_emps = 0
    raise_amt = 2.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

emp_1 = EmploYees('Laszlo', 'Balint', 35900)
emp_2 = EmploYees( 'Dave', 'Micheal', 7899)
print(EmploYees.raise_amt)
print("My income:", emp_1.raise_amt * 35900)
print("My Income:", emp_2.raise_amt * 7899)
print("My name is:", emp_1.last)
print("My name is:", emp_2.first)
