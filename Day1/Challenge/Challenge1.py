number = int(input("Entrer un nombre : "))
length = int(input("Entre une taille specifie : "))
multiples = []
for i in range(1,length):
    mul = number * i
    multiples.append(mul)
print(f"number : {number} - length : {length} -> {multiples}")    


    