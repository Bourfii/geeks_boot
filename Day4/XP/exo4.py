class Person:
    def __init__(self,first_name,age):
        self.first_name = first_name
        self.age = age
        self.last_name = ""  
    def is_18(self):
        return self.age >= 18
class Family:
    def __init__(self,last_name):
        self.last_name = last_name
        self.members = []  
    
    def born(self,first_name,age):
        new_person = Person(first_name, age)
        new_person.last_name = self.last_name 
        self.members.append(new_person) 
    
    def check_majority(self,first_name):
        for person in self.members:
            if person.first_name == first_name:
                if person.is_18():
                    print(f"You are over 18, your parents Jane and John accept that you will go out with your friends")
                else:
                    print("Sorry, you are not allowed to go out with your friends.")
                return
        print(f"No family member named {first_name} found.")
    
    def family_presentation(self):
        print(f"Family last name: {self.last_name}")
        print("Members of the familly:")
        for person in self.members:
            print(f"- {person.first_name}, {person.age} years old")
family = Family("Carle")
family.born("Jims", 20)
family.born("Sam", 16)
family.born("Charlot", 25)
family.check_majority("Jim") 
family.check_majority("Sam")    
family.check_majority("charlot")  
family.family_presentation()
