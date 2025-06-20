class Cat:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        print(f"Name's cat : {self.name} , Age's cat : {self.age}")
cat1 = Cat("Mimi",3)
cat2 = Cat("Grie",4)
cat3 = Cat("Sondoss",1)
def Oldest_Cat(cat1,cat2,cat3):
    if cat1.age > cat2.age and cat1.age > cat3.age:
        return cat1
    elif cat2.age > cat1.age and cat2.age > cat3.age:
        return cat2
    else:
        return cat3
oldest = Oldest_Cat(cat1,cat2,cat3)    
print(f"The oldest cat is  {oldest.name} and is {oldest.age} years old")  

    

    

