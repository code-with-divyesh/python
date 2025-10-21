import random

num_to_guess=random.randint(1,100)
while True:
  try:
    guess=int(input("Guess Any No Between 1 to 100..."))
    if guess<num_to_guess:
      print("too low!")
    elif guess>num_to_guess:
      print("Too High!")
    else:
      print('Congratulations! You guessed the number.')
      break
  except ValueError:
      print('Please enter a valid number')