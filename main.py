# Programmers: Antonio Dueno
# Course: CS151, Zelalem Yalew
# Due Date: 10/23/2024
# Programming Assignment: 2
# Problem Statement:You are creating a three player game of the Game of Sticks where players alternate turns
#                   taking 1-3 sticks. The player to take the last stick loses.
# Data In: Player input for if player 2 is participating, number of sticks to take from, number of sticks taken by
#           player 1 and player 2, Player input for if player wishes to play game again.
# Data Out: Program explanation, number of sticks remaining in a game, player 1 losses, player 2 losses, and player 3 losses.
# Credits: Class discussion of while loops and SENTINEL.

import random

#Variable values being set before loop
times_played = 0
player_number = 0
player_1_losses = 0
player_2_losses = 0
player_3_losses = 0
game_running = 0
SENTINEL = 0

#program explanation
print('Hello! Welcome to the Game of Sticks! In this game, you will enter how many sticks you wish \nto play with,'
          'then you will take turns with the computer player to remove 1 to 3 sticks. \nWhoever removes the last stick loses!')

#main loop
while SENTINEL != 1:
    if times_played > 0:
        total_sticks = 0
        game_running = 0
        replay_game = str(input('Would you like to play again? \nInput "y" for yes and "n" for no:' ))
        while replay_game != 'y' and replay_game != 'n':
            replay_game = str(input('Would you like to play again? \n') )
        if replay_game.lower() == 'n':
           SENTINEL = 1

    #prompt asking how many players will play
    player_number = input("How many players will play? Input '1' for you and the computer, and input '2' for you, a friend, and the computer!:")
    while not player_number.isdigit() and player_number < 1 or player_number > 2:
        player_number = (input('Please enter a valid number:'))




    #prompt asking how many sticks will be used
    total_sticks = input('How many sticks will play? Please input a number between 10 and 100:' )

    while total_sticks.isdigit():
        total_sticks = input('Please enter a valid number:')
        if total_sticks.isdigit():
            total_sticks = int(total_sticks)
            if 10 > total_sticks or total_sticks > 100:
                total_sticks = input('Please enter a valid number:')


    #loop for while game is running
    while game_running == 0:

        #player 1's turn
        player_1_sticks = input("Player 1's turn! How many sticks will you remove? Please input a number between 1 and 3:" )
        while player_1_sticks != 1 or 2 or 3 and not player_1_sticks.isalpha():
            player_1_sticks = input("Please input a valid number between 1 and 3:" )
            if player_1_sticks.isdigit():
                player_1_sticks = int(player_1_sticks)
            total_sticks = total_sticks - player_1_sticks

        #player 1 loses
        if total_sticks <= 0:
            print("Player 1 drew the last stick! You lose, Player 1!")
            player_1_losses += 1
            times_played += 1
            game_running = 1

        #Player 2's turn, if there is a player 2 participating
        if player_number == 2:
            player_2_sticks = input("Player 2's turn! How many sticks will you remove? Please input a number between 1 and 3:" )
            while player_2_sticks != 1 or 2 or 3 and player_2_sticks.isalpha():
                player_2_sticks = input("Please input a valid number between 1 and 3:" )
                if player_2_sticks.isdigit():
                    player_2_sticks = int(player_2_sticks)
            total_sticks = total_sticks - player_2_sticks

            #Player 2 loses
            if total_sticks <= 0:
                print("Player 2 drew the last stick! You lose, Player 2!")
                player_2_losses += 1
                times_played += 1
                game_running = 1

        #Computer player's turn
        player_3_sticks = random.randint(1, 3)
        print("COM Player's turn! They removed" + str(player_3_sticks) + " stick(s)!")
        total_sticks = total_sticks - player_3_sticks
        if total_sticks <= 0:
            print("COM player drew the last stick! You lose, COM player!")
            player_3_losses += 1
            times_played += 1
            game_running = 1

print("Thank you for playing the Game of Sticks! Here are the final stats:"
      "\nGame was played" + str(times_played) + " time(s)!"
      "\nPlayer 1 lost:", player_1_losses, "time(s)!"
      "\nPlayer 2 lost:", player_2_losses, "time(s)!"
      "\nPlayer 3 lost:", player_3_losses, "time(s)!")

