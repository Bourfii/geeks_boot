class Zoo:
    def __init__(self,zoo_name):
        self.zoo_name = zoo_name
        self.animals = []
    def add_animal(self,new_animal):    
        if new_animal not in self.animals:
            self.animals.append(new_animal)
    def get_animals(self):
        for animal in self.animals:            
            print(animal)
    def sell_animal(self,animal_sold):
        if animal_sold in self.animals:
            self.animals.remove(animal_sold)
    def sort_animals(self):
        self.animals.sort()
        groups = {}
        for animal in self.animals: 
            letter = animal[0].upper()
            if letter not in groups:
                groups[letter] = [animal]
            else:
                groups[letter].append(animal)    
        return groups
    def get_groups(self):
        groups = self.sort_animals()
        for letter, animal in groups.items():
            print(f"{letter} : {animal}")

z = Zoo("Shark Zoo")    
z.add_animal("elephant")
z.add_animal("Bear")
z.add_animal("Giraffe")
z.add_animal("lion")
z.add_animal("zebra")
z.get_animals()   
print("_______________________________________________\n")
z.sell_animal("zebra")
print(z.sort_animals())
print("_______________________________________________\n")
z.get_groups()

