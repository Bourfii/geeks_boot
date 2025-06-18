String = input("Entrer un string : ")
newString = ""
for i in range(len(String)):
    if i==0 or String[i] != String[i-1]: 
       newString += String[i]
print(f"User's word : {String} -> {newString}")    

