my_name = "Assia"
your_name = input("Entrer votre nom : ")
if your_name.strip().lower() == my_name.lower():
    print("Wow! We have the same name! Are we long-lost twins?")
else:
    print(f"Oh no, you're {your_name}? I was hoping for another {my_name}!")