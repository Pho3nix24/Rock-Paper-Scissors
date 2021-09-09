import random

options = ["rock", "paper", "scissors"]
play_again = "yes"

while play_again == "yes":
    history = {1: []}
    user_points = 0
    cpu_points = 0
    no_of_rounds = int(input("Enter the number of Rounds : "))
    for i in range(0, no_of_rounds):
        user_input = input("Player choice (rock, paper, scissors): ")
        cpu_input = random.choice(options)
        print("CPU choice : {}".format(cpu_input))
        if user_input == "rock" and cpu_input == "scissors" or user_input == "scissors" and cpu_input == "paper" or user_input == "paper" and cpu_input == "rock":
            round_winner = "Player"
            user_points = user_points + 1
        elif user_input == "scissors" and cpu_input == "rock" or user_input == "paper" and cpu_input == "scissors" or user_input == "rock" and cpu_input == "paper":
            round_winner = "CPU"
            cpu_points = cpu_points + 1
        else:
            round_winner = "Tie"
        history[i + 1] = [user_input, cpu_input, round_winner]
    print("Player Score : ", user_points)
    print("CPU Score    : ", cpu_points)
    if user_points > cpu_points:
        print("Winner of the series is Player")
    elif user_points < cpu_points:
        print("Winner of the series is CPU")
    else:
        print("The Series is Tied")
    round_history = int(input("Enter the round whose information is needed (0 to exit): "))
    while round_history != 0:
        print("Player Choice : {}\nCPU Choice    : {}\nRound Winner  : {}".format(history[round_history][0],
                                                                                  history[round_history][1],
                                                                                  history[round_history][2]))
        round_history = int(input("Enter the round whose information is needed (0 to exit): "))
    play_again = input("Do you wish to play again? (yes/no) : ")
