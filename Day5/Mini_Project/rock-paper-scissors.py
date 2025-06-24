from game import Game

def get_user_menu_choice():
    print("=========Menu:=========")
    print("1.Play a new game")
    print("2.Show scores")
    print("3.Quit")
    choice = input("choose 1 , 2 or 3 :").strip()
    print(f"DEBUG: choice entered: {choice}")
    if choice in ['1' , '2' , '3']:
        return choice
    else:
        print("Invalid choice!")
        return None
def print_results(results):
    print("The result of this game is : ")
    print(f"Winners : {results.get('Win' , 0)}")
    print(f"Losers : {results.get('Loss' , 0)}")
    print(f"Equal : {results.get('Draw' , 0)}")  
    print("Thank you for playing!")
def main():
    results = {"Win" : 0,"Loss" : 0,"Draw" : 0}
    while True:
        choice = get_user_menu_choice()
        if choice == '1':
            game = Game()
            result = game.play()
            results[result] += 1
        elif choice == '2':
            print_results(results)
        elif choice == '3':
            print_results(results)
            break
        else:
            continue
if __name__=="__main__":
    main()        