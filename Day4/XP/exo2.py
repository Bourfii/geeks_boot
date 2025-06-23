class Dog:
    def __init__(self,name,age,weight):
        self.name =  name
        self.age = age
        self.weight = weight
    def  bark(self):
        return f"{self.name} is barking"
    def run_speed(self):
        return self.weight / (self.age * 10)
    def fight(self,other_dog):
        dog1 = self.run_speed() * self.weight
        dog2 = other_dog.run_speed() * other_dog.weight
        if dog1 > dog2:
            return f"{self.name} is won in the fight"
        elif dog1 < dog2:
            return f"{other_dog.name} is won in the fight"
        else:
            return "Equal" 
dog_1 = Dog("Rex",3,12)
dog_2 = Dog("Zak",4,15)
dog_3  = Dog("Boby",2,17)
print("Dog number 1 : \n") 
print(dog_1.bark())
print(dog_1.run_speed())
print(dog_1.fight(dog_3))
print("Dog number 2 : \n")
print(dog_2.bark())
print(dog_2.run_speed())
print(dog_2.fight(dog_1))
print("Dog number 3 : \n")
print(dog_3.bark())
print(dog_3.run_speed())
print(dog_3.fight(dog_2))

    