month = int(input("Entrer un nombre entre 1 et 12 : "))
if month<=3 and month>=5:
   print("it's Spring")
elif month<=6 and month>=8:
   print("It's Summer")
elif month<=9 and month>=11:
   print("It's Autumn")
elif month<=12  and month>=2:
   print("It's Winter")
else:
   print("Le mois invalide!essayer d'entrer une autre nombre entre 1 et 12")

             