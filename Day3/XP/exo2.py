#step 1
class Dog:
    def __init__(self,name,height):
        self.name = name
        self.height = height
    def bark(self):
        print(f"{self.name} is goes Woof!")
    def jump(self):
        x = self.height * 2
        print(f"{self.name} jumps {x} cm height")
    def affiche_details(self):
        print(f"The dog's name is : {self.name} and is {self.height}")    
#step 2
davids_dog = Dog("Zomba",11)
sarahs_dog = Dog("Ric",14)
#step 3
davids_dog.bark()
davids_dog.jump()

sarahs_dog.bark()
sarahs_dog.jump()

def compare(dog1,dog2):
    if dog1.height > dog2.height:
        print(f"{dog1.name} is taller than {dog2.name}")
    elif dog2.height > dog1.height:
        print(f"{dog2.name} is taller than {dog1.name}")
    else:
       print(f"{dog1.name} and {dog2.name} are the same height")
compare(davids_dog,sarahs_dog)              

