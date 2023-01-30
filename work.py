class LivingThings:
    def __init__(self):
        print( "is a living thing")

class Plants(LivingThings):
    def __init__(self, pname):
        self.plname=pname
        print(self.plname,"is a living thing")
        super().__init__()

class Trees(Plants,LivingThings):
    def __init__(self, t_name):
        self.tname=t_name
        print(self.tname," is type of plants")
        super().__init__()

class Shrubs(Plants,LivingThings):
    def __init__(self, s_name):
        print("shrubs is a type of plants")
        super().__init__()

class Animals(LivingThings):
    def __init__(self, an_name):
        print("animal is a living thing")
        super().__init__()

class Marine(Plants, Animals, LivingThings):
    def __init__(self, m_name):
        print("marine lives in water")
        super().__init__()

class NonMarine(Plants, Animals, LivingThings):
    def __init__(self, n_name):
        print("non marine lives out of water")
        super().__init__()

class Winged(Animals, LivingThings):
    def __init__(self, w_name):
        print("winged animals  can fly")
        super().__init__()

class NonWinged(Animals, LivingThings):
    def __init__(self, nw_name):
        print("non winged cannot fly")
        super().__init__()


class HumanBeings(LivingThings):
    def __init__(self):
        print("human is a  living things")
        super().__init__()


class Men(HumanBeings, LivingThings):
    def __init__(self, men_name, men_age, men_place, marital_status, job_status, men_wage):
        self.men_name = men_name
        self.men_age = men_age
        self.men_wage = men_wage
        self.men_place = men_place
        self.marital_status = marital_status
        self.job_status = job_status
        super().__init__()

    def get_name(self):
        return self.men_name

    def get_age(self):
        return self.men_age

    def is_employee(self):
        if self.job_status == "employed":
            return "employed"
        else:
            return "unemployed"

    def is_married(self):
        if self.marital_status == "married":
            return "married"
        else:
            return "unmarried"
class Women(HumanBeings, LivingThings):
    def __init__(self, wo_name):
        print("women is a human_being")
        super().__init__()
class Child(HumanBeings,LivingThings):
    def __init__(self, c_name):
        print("child is a human_being")
        super().__init__()



men1 = Men("alex", 22, "banglore", "unmarried", "unemployed",7000)
men2 = Men("asif", 28, "calicut", "married", "employed",70000)
print(men1.get_name(), men1.get_age(), men1.is_employee(), men1.is_married())
print(men2.get_name(), men2.get_age(), men2.is_employee(), men2.is_married())
