names = ['Samus', 'Cortana', 'V', 'Link', 'Mario', 'Cortana', 'Samus']
user_name = input("Entrer votre nom : ")
if user_name in names:
        exist = names.index(user_name)
        print(f"le nom est existe dans la liste : {user_name}",exist)
        