class Farm:
    def __init__(self,farm_name):
        self.farm_name = farm_name
        self.animal = {}
    def add_animal(self,animal_type,count=1):
        if animal_type in self.animal:
            self.animal[animal_type] += count
        else:
            self.animal[animal_type] = count
    def get_info(self):
        String = f"farm's name : {self.farm_name}\n"
        for animal, count in self.animal.items():
            String += f"{animal} : {count}\n"
            String += "E-I-E-I-0!\n"
        return String
    def get_animal_types(self):
        return sorted(self.animal.keys())

    # BONUS 2: retourne une description courte
    def get_short_info(self):
        animal_list = self.get_animal_types()
        formatted_animals = []
        for animal in animal_list:
            if self.animal[animal] > 1:
                formatted_animals.append(animal + 's')
            else:
                formatted_animals.append(animal)
        if len(formatted_animals) > 1:
            short_description = ", ".join(formatted_animals[:-1])
            short_description += f" and {formatted_animals[-1]}"
        else:
            short_description = formatted_animals[0]
        return f"{self.farm_name}'s farm has {short_description}."
macdonald = Farm("McDonald")
macdonald.add_animal('cow', 5)
macdonald.add_animal('sheep')
macdonald.add_animal('zepra')
macdonald.add_animal('goat', 12)
print(macdonald.get_info())  
print()
print(macdonald.get_animal_types())  
print(macdonald.get_short_info())   
 