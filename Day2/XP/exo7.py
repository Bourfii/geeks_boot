import random 
#step 1
def get_random_temp(season):
    if season == "Winter":
        return random.uniform(0,16)
    elif season == "Spring":
        return random.uniform(16,23)
    elif season == "Autumn":
        return random.uniform(24,32)
    elif season == "Summer":
        return random.uniform(32,40)
    #degree = random.randint(-10,40)
    #degree_float = random.uniform(-10,40)
    #return degree
    #etape 5

#step 2
#step 3
def main():
    month = int(input("Enter a month between 1 and 12 : "))
    if month in [12, 1, 2]:
        season = "Winter"
    elif month in [3, 4, 5]:
        season = "Spring"
    elif month in [6, 7, 8]:
        season = "Summer"
    elif month in [9, 10, 11]:
        season = "Autumn"
    else:
        print("Invalid month!")
        return
    Temperature = get_random_temp(season)
    print(f"The temerature Today is {Temperature} degree Celsius in {season}")
    if Temperature == 0:
        print("Brrr,that's freezing! Wear soe extra layers today")
    elif Temperature <=16:
        print("Quite chilly ! Don't forgot your coat")
    elif Temperature<= 23 :
        print("Nice weather")
    elif Temperature <= 32:
        print("A bit warm , stay hydrated.")
    elif Temperature <= 40:  
        print("It's really hot! Stay cool")            
    else:
        print("invalid Temperature")
main()        

    