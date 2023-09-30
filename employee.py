"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name, monthly=0, hourly=0, hours_worked=0):
        self.name = name
        self.monthly = monthly
        self.hourly = hourly
        self.hours_worked = hours_worked

    def get_pay(self):
        if self.monthly:
            return self.monthly
        else:
            return self.hourly * self.hours_worked

    def __str__(self):
        if self.monthly:
            return f"{self.name} works on a monthly salary of {self.monthly}. Their total pay is {self.get_pay()}."
        else:
            return f"{self.name} works on a contract of {self.hours_worked} hours at {self.hourly}/hour. Their total pay is {self.get_pay()}."
    
class Comission(Employee):
    def __init__(self, name, monthly=0, hourly=0, hours_worked=0, bonus=0, contract=0, contract_pay=0):
        super().__init__(name, monthly, hourly, hours_worked)
        self.bonus = bonus
        self.contract = contract
        self.contract_pay = contract_pay

    def get_pay(self):
        if self.bonus:
            return super().get_pay() + self.bonus
        else:
            return super().get_pay() + (self.contract * self.contract_pay)
        
    def __str__(self):
        if self.monthly:
            if self.bonus:
                return f"{self.name} works on a monthly salary of {self.monthly} and receives a bonus comission of {self.bonus}. Their total pay is {self.get_pay()}."
            if self.contract:
                return f"{self.name} works on a monthly salary of {self.monthly} and receives a comission for {self.contract} contract(s) at {self.contract_pay}/contract. Their total pay is {self.get_pay()}."
        else:
            if self.bonus:
                return f"{self.name} works on a contract of {self.hours_worked} hours at {self.hourly}/hour and receives a bonus comission of {self.bonus}. Their total pay is {self.get_pay()}."
            if self.contract:
                return f"{self.name} works on a contract of {self.hours_worked} hours at {self.hourly}/hour and receives a comission for {self.contract} contract(s) at {self.contract_pay}/contract. Their total pay is {self.get_pay()}."


# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie', monthly=4000)

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie', hourly=25, hours_worked=100)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Comission('Renee', monthly=3000, contract=4, contract_pay=200)

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Comission('Jan', hourly=25, hours_worked=150, contract=3, contract_pay=220)

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Comission('Robbie', monthly=2000, bonus=1500)

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Comission('Ariel', hourly=30, hours_worked=120, bonus=600)

print(str(ariel))