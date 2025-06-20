class Zoo:
    def __init__(self,zoo_name):
        self.zoo_name = zoo_name 
        self.animals = []
    def add_animal(self,new_animal):
        if new_animal not in self.animals:
            self.animals.append(new_animal)
    def get_animals(self):
        print(f"The all animals currently {self.animals} in the {self.zoo_name}")
    def sell_animal(self,animal_sold):
           for animal in self.animals:
                if animal_sold in self.animals:
                    print("The animal is exist.")
                    self.animals.remove(animal_sold)
    def sort_animals(self):
        self.animals.sort()
        self.groups = {}
        for animal in self.animals:
            first_letter = animal[0].upper()
            if first_letter in self.groups:
                self.groups[first_letter].append(animal)
            else:
                self.groups[first_letter] = [animal]
    def get_groups(self):
        for letter, animals_list in self.groups.items():
            print(f"{letter}: {animals_list}")                
# creation a zoo
ramat_gan_safari = Zoo("Ramat Gan Safari")
ramat_gan_safari.add_animal("Giraffe")
ramat_gan_safari.add_animal("Bear")
ramat_gan_safari.add_animal("Baboon")
ramat_gan_safari.get_animals()
ramat_gan_safari.sell_animal("Bear")
ramat_gan_safari.get_animals()
ramat_gan_safari.sort_animals()
ramat_gan_safari.get_groups()



