from exo2 import Dog
import random
class PetDog(Dog):
    def __init__(self,name,age,weight,trained=False):
        super().__init__(name,age,weight)
        self.trained = trained
    def train(self):
        def __init__(self,name,age,weight):
           super().__init__(name,age,weight)
           self.trained = False
    def train(self):
        print(self.bark())
        self.trained = True
    def play(self,*args):
        names = [self.name] + [dog.name for dog in args]
        all_dogs =" , ".join(names)
        print(f"{all_dogs} are playing together")
    def do_a_trick(self):
        if self.trained:
            tricks = [
                "does a barrel roll",
                "stands on his back legs",
                "shakes your hand",
                "plays dead"
            ]
            trick = random.choice(tricks)
            print(f"{self.name} {trick}")
        else:
            print(f"{self.name} is not trained yet!")       

dog1 = PetDog("Boby", 3, 12)
dog2 = PetDog("Rocy", 2, 10)
dog3 = PetDog("Zac", 4, 15)
dog1.train()
dog1.play(dog2,dog3)
dog1.do_a_trick()
