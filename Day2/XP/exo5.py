import random
def Random(number):   
    random_nomber = random.randint(1,100)
    if random_nomber == number:
        print("Success! The random number is the same origin number.")
    else:
        print(f"Fial! Your number : {number} , Random number : {random_nomber}")         
Random(1)  
Random(8)  
Random(2)  
Random(37)  
Random(56)        
