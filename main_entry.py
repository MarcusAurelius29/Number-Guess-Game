import random

print("Hello, Welcome to a new game!")

def generate1():
    n = random.randint(0 , 20)
    return n

def generate2():
    n = random.randint(0 , 50)
    return n

def generate3():
    n = random.randint(0 , 100)
    return n

print("Please select a difficulty")
print(" Easy || Medium || Hard")
ans = input()

if(ans == 'Easy'):
   x = generate1()

elif (ans == 'Medium'):
   x = generate2()

else:
   x = generate3()
      
      
guess = 0


def func_play_game(x , guess):
    
    
    print("Please enter your guess..")
    num = (int(input()))
    if(num == x):
      print("You won! Lesssgooo")
      print(" Would you like to play another game? (Y/N)")
      ans = input()
      if(ans == 'Y'):
         print("Please select a difficulty")
         print(" Easy || Medium || Hard")
         ans = input()

         if(ans == 'Easy'):
          x = generate1()

         elif (ans == 'Medium'):
          x = generate2()

         else:
          x = generate3()

         func_play_game(x, 0)
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