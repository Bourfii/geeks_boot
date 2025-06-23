class Pets():
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            animal.walk()   
class Cat:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def make_sound(self):
        print(f"{self.name} everyday says Meow!")
    def walk(self):
        print(f"{self.name} is walking")

class Siamese(Cat):    
    def __init__(self,name,age,body_color):
        super().__init__(name,age)
        self.body_color = body_color

    def play(self):
        print(f"{self.name} is playing")
    #override     
    def make_sound(self):
        print(f"{self.name} says Meow!")
class Chartreux(Cat):
    def __init__(self,name,age,eyes_color):
        super().__init__(name,age)
        self.eyes_color = eyes_color 
    def make_sound(self):
        print(f"{self.name} and is {self.age} years old says MEOOOOOOOOW!")    
class Bengal(Cat):
    def make_sound(self):
        print(f"{self.name} love saying Grrr every day , He is {self.age} year.old") 
       
Bengal_obj = Bengal("Bengal",2)
Chartreux_obj = Chartreux("chartreux",1,"brown")
Siamese_obj = Siamese("Siamese",4,"Orange")        
all_cats = [Bengal_obj, Chartreux_obj, Siamese_obj]
for cat in all_cats:
    cat.make_sound()
sara_pets = Pets(all_cats)
sara_pets.walk()


    