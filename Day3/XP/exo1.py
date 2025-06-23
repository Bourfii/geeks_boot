#step 1
class Cat:
    def __init__(self,name,age):
        self.name = name 
        self.age = age 
cat1 = Cat("Mimi",1)
cat2 = Cat("Minouch",4)
cat3 = Cat("Tom",7)
#step 2
def oldest_cat(cat_a,cat_b,cat_c):
    oldest = cat_a
    if cat_b.age > oldest.age:
        oldest = cat_b
    if cat_c.age > oldest.age:
        oldest = cat_c
    return oldest
#step 3    
old = oldest_cat(cat1,cat2,cat3)
print(f"The oldest cat is {old.name} and is {old.age} years old")
   