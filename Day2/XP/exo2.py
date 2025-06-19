family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}
totale_cost = 0
for name in family:
    age = family[name]
    if age<3:
       price = 0
    elif age>=3 and age <=12:
       price = 10
    else:
       price = 15
    totale_cost += price        
print(totale_cost) 
