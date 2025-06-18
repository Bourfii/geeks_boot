numbers = []
for i in range(1,4):
    number = int(input(f"Entrer le {i} nombre : "))
    numbers.append(number)
max = max(numbers)
input(f"la plus grand nombre est :{max}")    