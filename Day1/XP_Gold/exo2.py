print("Question 1:")
numbers = range(1,21)
for i in numbers:
    print(i)
print("Question 2:")
numbers = list(range(1,21))
for i in range(len(numbers)):
    if i % 2 == 0:
        print(numbers[i])

