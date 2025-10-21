import random
roll_count=0
while True:
  choice=input("Roll The dice?(y,n):").lower()
  if choice=='y':
    try:
            num_dice = int(input("How many dice do you want to roll? (1–6): "))
            if num_dice < 1 or num_dice > 6:
                print("⚠️ Please enter a number between 1 and 6.")
                continue

            # Roll the dice
            dice = []
            for i in range(num_dice):
                dice.append(random.randint(1, 6))

            roll_count += 1  
            print(f"You rolled: {dice}")
            print(f"Total rolls so far: {roll_count}\n")

    except ValueError:
            print("❌ Please enter a valid number.")
            continue

  elif choice=='n':
    print("Thanks for playing!")
    break
  else:
    print("Invalid value! Please enter 'y' or 'n'.")