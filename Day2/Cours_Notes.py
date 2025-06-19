Personne = {
   'name' : 'Ali',
   'age' : 25,
   'email' : 'alisalmi@gaml.com'
}
#print(Personne['name'])

a_dict = {'color': 'blue', 'fruit': 'apple', 'pet': 'dog'}

print(a_dict.items())
for key, value in a_dict.items():
    print(key, '->', value ) 

names = []
sizes = []
prices = []
shirts = [
  {
    'name': 'Awesome T-shirt 3000',
    'size': 'S',
    'price': 20
  },
  {
    'name': 'Awesome T-shirt 3000',
    'size': 'M',
    'price': 25
  },
  {
    'name': 'Awesome T-shirt 3000',
    'size': 'L',
    'price': 30
  },
]  
for shirt in shirts:
    for key, value in shirt.items():
        if key == 'name':
           names.append(value)
        elif key == 'size':
           sizes.append(value)
        elif key == 'price':
           prices.append(value)       
        #print(f"{key} : {value}")
print("\n")        
    
    #sizes.append(key['size'])
    #prices.append(key['price']) 
print("Names : ",names)    
print("Sizes : ",sizes)    
print("Prices : ",prices)  
  