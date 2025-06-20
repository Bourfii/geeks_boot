class Dog:
    def __init__(self,name,height):
        self.name = name
        self.height = height
    def bark(self):
        print(f"{self.name} goes woof!")
    def jump(self):
        x = self.height * 2
        print(f"{self.name} jumps {x} cm high!") 
#cree les object       
davids_dog = Dog("Maxe", 12) 
sarahs_dog = Dog("Lusie", 15)

print(f"Davids's dog name : {davids_dog.name} and is {davids_dog.height} cm height")
davids_dog.bark()
davids_dog.jump()

print(f"Sarah's dog name : {sarahs_dog.name} and is {sarahs_dog.height} cm height")
sarahs_dog.bark()
sarahs_dog.jump()

#compare Dog size
if davids_dog.height == sarahs_dog :
    print("The dogs are the same height ")
else:
    print("The dogs are not the same height")    


    