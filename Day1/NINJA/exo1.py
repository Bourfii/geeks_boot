print(3 <= 3 < 9) # True
print(3 == 3 == 3)  # True
print(bool(0))  # False
print(bool(5 == "5"))  # True
print(bool(4 == 4) == bool("4"== "4"))  # True
print(bool(bool(None)))  # False

x = (1 == True)  # True
y = (1 == False)  # False
a = True + 4 # 5 
b = False + 10 # 10

print("x is", x) # x is True
print("y is", y) # y is False
print("a:", a)  # a: 5
print("b:", b) #b: 10