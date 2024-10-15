# Initial Design Document

1. import random module
2. output program explanation to user 
3. set times_played to 0
4. set player_number to 0
4. set player_1_wins to 0
5. set player_2_wins to 0
6. set player_3_wins to 0
3. while true:
   4. if times_played is greater than 0:
      5. ask user if they want to play again
      6. if user answers no
      7. output player_1_wins
      8. if player_number greater than 0
         9. output player_2_wins 
      10. output player_3_wins 
      7. exit program
   3. ask user to input how many players are playing
        4. while user input doesnt equal "1" or "2" or "one" or "two"
           5. ask user to input valid number of players
        6. assign user input for number of players to player_number
        7. ask user number to enter number of sticks
           8. while user input isnt greater than 10 or less than 100:
              9. ask user to input valid number
        10. assign user input for number of sticks to stick_total 
        11. output to player that game is starting.
            12. while true:
                13. player 1 is asked to input how many sticks they wish to remove.
                    14. while input is not equal to 1 or 2 or 3:
                        15. ask user to input valid number
                16. user input is subtracted from stick_total
                17. if stick total is less than or equal to 0
                    18. output player 1 wins
                    19. add 1 to player_1_wins
                    20. end loop
                17. if player number is equal to 2:
                    18. player 2 is asked to input how many sticks they wish to remove.
                        14. while input is not equal to 1 or 2 or 3:
                            15. ask user to input valid number
                    16. user input is subtracted from stick_number
                    17. if stick total is less than or equal to 0
                        18. output player 2 wins
                        19. add 1 to player_2_wins
                        20. end loop
                17. computer player subtracts number. number is decided via random number generator set to generate 
                    random number between 1 and 3. 
                18. computer player's number is subtracted from stick_total
                19. if stick total is less than or equal to 0
                    18. output player 3 wins
                    19. add 1 to player_3_wins
                    20. end loop
   