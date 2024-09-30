import random

print("Let´s play Rock, Paper, Scissors, Lizzard, Spock. Best of 7 wins:")
print("Draw: \n1-Rock 🪨 \n2-Paper 📃 \n3-Scissors ✂️ \n4-Lizzard 🦎 \n5-Spock 🖖🏼 ")
print("This new Version of the classic game adds two more elements to make it a little more complex and less likely to end in a tie")
print("""In this game the rules are very simple:
    Scissors ✂️ cut Paper 📃
    Paper 📃 covers Rock 🪨
    Rock 🪨 crushes Lizzard 🦎
    Lizzard 🦎 poisons Spock 🖖🏼
    Spock 🖖🏼 smashes Scissors ✂️
    Scissors ✂️ decapitate Lizzard 🦎
    Lizzard 🦎 eats Paper 📃
    Paper 📃 disproove Spock 🖖🏼
    Spock 🖖🏼 vaporizes Rock 🪨
    And as it always has Rock 🪨 crushes Scissors ✂️
    """)
while True:
    cpu_score = 0
    user_score = 0

    while cpu_score < 5 and user_score < 5:
        cpu = random.randint(1, 5)

        if cpu == 1:
            cpu = "Rock 🪨"
        elif cpu == 2:
            cpu = "Paper 📃"
        elif cpu == 3:
            cpu = "Scissors ✂️"
        elif cpu == 4:
            cpu = "Lizzard 🦎"
        elif cpu == 5:
            cpu = "Spock 🖖🏼"

        try:
            user = int(input("Choose a number to draw Rock, Paper, Scissors, Lizzard or Spock: "))
            if user == 1:
                user = "Rock 🪨"
                print("You chose Rock 🪨")
            elif user == 2:
                user = "Paper 📃"
                print("You chose Paper 📃")
            elif user == 3:
                user = "Scissors ✂️"
                print("You chose Scissors ✂️")
            elif user == 4:
                user = "Lizzard 🦎"
                print("You chose Lizzard 🦎")
            elif user == 5:
                user = "Spock 🖖🏼"
                print("You chose Spock 🖖🏼")
            else:
                raise ValueError
        except ValueError:
            print(("ERROR YOU HAVE TO CHOOSE A NUMBER BETWEEN 1 & 5"))

        if cpu == user:
            print(f"Computer drew: {cpu}")
            print("Its a tie.")
            print(f"Score:\nYOU: {user_score}\nCOMPUTER: {cpu_score}")

        elif cpu == "Scissors ✂️" and user == "Paper 📃":
            cpu_score += 1
            print(f"Computer drew: {cpu}")
            print("You lose")
            print(f"Score:\nYOU: {user_score}\nCOMPUTER: {cpu_score}")

        elif user == "Scissors ✂️" and cpu == "Paper 📃":
            user_score += 1
            print(f"Computer drew: {cpu}")
            print("You win")
            print(f"Score:\nYOU: {user_score}\nCOMPUTER: {cpu_score}")

        elif cpu == "Paper 📃" and user == "Rock 🪨":
            cpu_score += 1
            print(f"Computer drew: {cpu}")
            print("You lose")
            print(f"Score:\nYOU: {user_score}\nCOMPUTER: {cpu_score}")

        elif user == "Paper 📃" and cpu == "Rock 🪨":
            user_score += 1
            print(f"Computer drew: {cpu}")
            print("You win")
            print(f"Score:\nYOU: {user_score}\nCOMPUTER: {cpu_score}")

        elif cpu == "Rock 🪨" and user == "Lizzard 🦎":
            cpu_score += 1
            print(f"Computer drew: {cpu}")
            print("You lose")
            print(f"Score:\nYOU: {user_score}\nCOMPUTER: {cpu_score}")

        elif user == "Rock 🪨" and cpu == "Lizzard 🦎":
            user_score += 1
            print(f"Computer drew: {cpu}")
            print("You win")
            print(f"Score:\nYOU: {user_score}\nCOMPUTER: {cpu_score}")

        elif cpu == "Lizzard 🦎" and user == "Spock 🖖🏼":
            cpu_score += 1
            print(f"Computer drew: {cpu}")
            print("You lose")
            print(f"Score:\nYOU: {user_score}\nCOMPUTER: {cpu_score}")

        elif user == "Lizzard 🦎" and cpu == "Spock 🖖🏼":
            user_score += 1
            print(f"Computer drew: {cpu}")
            print("You win")
            print(f"Score:\nYOU: {user_score}\nCOMPUTER: {cpu_score}")

        elif cpu == "Spock 🖖🏼" and user == "Scissors ✂️":
            cpu_score += 1
            print(f"Computer drew: {cpu}")
            print("You lose")
            print(f"Score:\nYOU: {user_score}\nCOMPUTER: {cpu_score}")

        elif user == "Spock 🖖🏼" and cpu == "Scissors ✂️":
            user_score += 1
            print(f"Computer drew: {cpu}")
            print("You win")
            print(f"Score:\nYOU: {user_score}\nCOMPUTER: {cpu_score}")

        elif cpu == "Scissors ✂️" and user == "Lizzard 🦎":
            cpu_score += 1
            print(f"Computer drew: {cpu}")
            print("You lose")
            print(f"Score:\nYOU: {user_score}\nCOMPUTER: {cpu_score}")

        elif user == "Scissors ✂️" and cpu == "Lizzard 🦎":
            user_score += 1
            print(f"Computer drew: {cpu}")
            print("You win")
            print(f"Score:\nYOU: {user_score}\nCOMPUTER: {cpu_score}")

        elif cpu == "Lizzard 🦎" and user == "Paper 📃":
            cpu_score += 1
            print(f"Computer drew: {cpu}")
            print("You lose")
            print(f"Score:\nYOU: {user_score}\nCOMPUTER: {cpu_score}")

        elif user == "Lizzard 🦎" and cpu == "Paper 📃":
            user_score += 1
            print(f"Computer drew: {cpu}")
            print("You win")
            print(f"Score:\nYOU: {user_score}\nCOMPUTER: {cpu_score}")

        elif cpu == "Paper 📃" and user == "Spock 🖖🏼":
            cpu_score += 1
            print(f"Computer drew: {cpu}")
            print("You lose")
            print(f"Score:\nYOU: {user_score}\nCOMPUTER: {cpu_score}")

        elif user == "Paper 📃" and cpu == "Spock 🖖🏼":
            user_score += 1
            print(f"Computer drew: {cpu}")
            print("You win")
            print(f"Score:\nYOU: {user_score}\nCOMPUTER: {cpu_score}")

        elif cpu == "Spock 🖖🏼" and user == "Rock 🪨":
            cpu_score += 1
            print(f"Computer drew: {cpu}")
            print("You lose")
            print(f"Score:\nYOU: {user_score}\nCOMPUTER: {cpu_score}")

        elif user == "Spock 🖖🏼" and cpu == "Rock 🪨":
            user_score += 1
            print(f"Computer drew: {cpu}")
            print("You win")
            print(f"Score:\nYOU: {user_score}\nCOMPUTER: {cpu_score}")

        elif cpu == "Rock 🪨" and user == "Scissors ✂️":
            cpu_score += 1
            print(f"Computer drew: {cpu}")
            print("You lose")
            print(f"Score:\nYOU: {user_score}\nCOMPUTER: {cpu_score}")

        elif user == "Rock 🪨" and cpu == "Scissors ✂️":
            user_score += 1
            print(f"Computer drew: {cpu}")
            print("You win")
            print(f"Score:\nYOU: {user_score}\nCOMPUTER: {cpu_score}")

        if user_score == 5:
            print("You win the game")
        elif cpu_score == 5:
            print("Computer wins the game")

    answer = input("Do you wish to play again? (y/n): ")

    if answer.lower() != "y":
        print("Thank you for playing. Cya next time")
        input("Press Enter or close the window to finish the program")
        break