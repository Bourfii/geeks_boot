brand = { 
    'name' : 'Zara',
    'creation_date': 1975,
    'creator_name': 'Amancio Ortega Gaona',
    'type_of_clothes' : ['men' , 'women', 'children', 'home'],
    'international_competitors': ['Gap', 'H&M', 'Benetton'],
    'number_stores': 7000,
    'major_color': 
    {
        'France': 'blue', 
        'Spain': 'red', 
        'US': ['pink', 'green']
    }
}
#brand['number_stores'] = 2
brand.update(number_stores=2)
print("Description of Zara's cleint : ",brand['type_of_clothes'])
brand["country_creation"] = "Spain"
for key in brand:
    if "international_competitors" in brand:
        print("international_competitors exists!")
brand['international_competitors'].append("Desigual")  
# Deleting creation_date key.
del brand['creation_date'] 
print("The last item of  international_competitors : \n",brand['international_competitors'][-1])
print("The major colors in the US : ",brand['major_color']['US'])
print("The numbers of the keys in the dictionary : ",len(brand))    
for key in brand:
     print(key)       
#Bonus 
more_on_zara = {
    'creation_date' : 2000,
    'number_stores' : 3000
}
brand.update(more_on_zara)
print(brand)