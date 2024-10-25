# Final Design Document

1. output program explanation to user 
2. set times_played to 0
3. set player_number to 0
4. set player_1_losses to 0
5. set player_2_losses to 0
6. set player_3_losses to 0
7. set game_running to 0
7. set SENTINEL to 0
8. while SENTINEL does not equal 1
   1. if times_played is greater than 0:
      1. ask user if they want to play again
      2. if user answers no
         1. output player_1_losses
         2. if player_number greater than 0
            1. output player_2_losses
         3. output player_3_losses
         4. exit program
   2. ask user to input how many players are playing
      1. while user input doesn't equal "1" or "2" or "one" or "two"
         1. ask user to input valid number of players
         2. assign user input for number of players to player_number
         3. ask user number to enter number of sticks
            1. while user input isn't greater than 10 or less than 100:
               1. ask user to input valid number
         4. assign user input for number of sticks to stick_total 
         5. output to player that game is starting.
            1. while game running is greater than 0:
               1. player 1 is asked to input how many sticks they wish to remove.
                  1. while input is not equal to 1 or 2 or 3:
                     1. ask user to input valid number
                  2. user input is subtracted from stick_total
                  3. if stick total is less than or equal to 0
                     1. output prompt saying player 1 wins
                     2. If player 1 loses, 
                        1. add 1 to player_1_losses
                     3. set game running to 1
                     4. break loop
                  4. if player number is equal to 2:
                     1. player 2 is asked to input how many sticks they wish to remove.
                        1. while input is not equal to 1 or 2 or 3:
                           1. ask user to input valid number
                     2. user input is subtracted from stick_number
                     3. if stick total is less than or equal to 0
                        1. output prompt saying player 2 wins
                        2. if player 2 lost:
                           1. add 1 to player_2_losses
                        3. set game running to 1
                        4. break loop
                  5. computer player subtracts number. number decided via random number generator set to generate number between 1 and 3. 
                  6. computer player's number is subtracted from stick_total
                  7. if stick total is less than or equal to 0
                     1. output prompt saying player 3 wins
                     2. if player 3 loses:
                        1. add 1 to player_3_losses
                     3. set game running to 1
                     
   