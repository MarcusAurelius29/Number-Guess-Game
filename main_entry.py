import random

print("Hello, Welcome to a new game!")

def generate():
    n = random.randint(0 , 20)
    return n

x = generate()
guess = 0


def func_play_game(x , guess):
    
    
    print("Please enter your guess..")
    num = (int(input()))
    if(num == x):
      print("You won! Lesssgooo")
      print(" Would you like to play another game? (Y/N)")
      ans = input()
      if(ans == 'Y'):
         new_x = generate()
         func_play_game(new_x, 0)
      else:
         exit()
            
    elif(num > x):
      print("LOWER YOUR GUESS")
      guess +=1
      print(f"Your total guesses are {guess}")
      func_play_game(x , guess)

    elif (num < x):
      print("RAISE YOUR GUESS")
      guess +=1
      print(f"Your total guesses are {guess}")
      func_play_game(x , guess)


func_play_game(x , guess)