class PersonalBMI:

    def __init__(self, age, weight):
        self.age = age
        self.weight = weight
        self.bmi = 0

    def calculate_bmi(self):
        if self.age >= 18:
            self.bmi = (self.age * self.weight)
        return self.bmi
    
    def calculations(self):
        if self.bmi < 45:
            print("Young People")
        else: 
            print("Old People")

