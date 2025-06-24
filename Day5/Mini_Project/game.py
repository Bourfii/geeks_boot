import random
class Game:
    def get_user_item(self):
        while True:
            Tab_choix = ["rock" , "paper" , "scissors"]
            user_choice =  input("Choose one of this : rock , paper , scissors : ")
            if user_choice in Tab_choix:
               return user_choice
            else:
                print("Invalid choise! Please try again")
    def get_computer_item(self):
        computer_choice = random.choice(["rock","paper","scissors"])
        return computer_choice
    def get_game_result(self, user_item, computer_item):
        self.user_choice = user_item
        self.computer_choice = computer_item
        if user_item == computer_item:
            return f"Draw"
        elif (user_item == "rock" and computer_item == "scissors") or (user_item == "paper" and computer_item == "rock") or (user_item == "scissors" and computer_item == "paper"):
            print("The user won")
            return f"Win"
        else:
            print("The user lost")
            return f"Loss"
    def play(self):
        user_item = self.get_user_item()
        computer_item = self.get_computer_item()
        result = self.get_game_result(user_item,computer_item)
        print(f"You selected {user_item}. The computer selected {computer_item}")
        if result == "Win":
            print("You Win")
        elif result == "Lost":
            print("You loss")
        elif result == "Draw":
            print("Tie")
        return result  

if __name__=="__main__":
   game = Game()
   game.play()  
        
