# gird is going user define 
# invalid dice roll

# cut position older player gets reset 


# logic for the game 


import random
# import pandas as pd


def roll_dice():
    return random.randint(1,6)


gird = int(input("pls enter your gird size: "))
position  = 0
players = ["player1","player2","player3"]
players_history = {player:[] for player in players}
players_postions = {player:[] for player in players}
borad_size = gird**2

print("board sizee",borad_size)
    

def movePlayer(player,rolled_dice):
    pass
        
        
playing = True

while playing:
    for player in players:
        # int(input(f"{player} press enter to roll a dice "))
        rolled_dice = roll_dice()
        # print(f"{player} has rolled {rolled_dice}")
        players_history[player].append(rolled_dice)
        length = len(players_postions[player])


        if length==0:
            position = rolled_dice
            players_postions[player].append(rolled_dice)
        else:
            position = rolled_dice + players_postions[player][length-1]
            if position <= borad_size :
                players_postions[player].append(position)

                if player == "player1":
                    len_2 = len(players_postions['player2'])
                    len_3 = len(players_postions['player3'])

                    # print("len(players_postions['player2'])" ,len_2 )
                    if (len_2 > 0 and players_postions['player2'][(len_2-1)] == position):
                        players_postions['player2'].append(0)
                    elif (len_3 > 0 and players_postions['player3'][(len_3-1)] == position):
                        players_postions['player3'].append(0)
                        
                elif player == 'player2':
                    len_1 = len(players_postions['player1'])
                    len_3 = len(players_postions['player3'])
                    # print("len(len_1)",len(len_1))
                    # print("len(len_3)",len(len_3))
                    if (len_1 > 0 and players_postions['player1'][(len_1-1)] == position):
                        players_postions['player1'].append(0)
                    elif (len_3 > 0 and players_postions['player3'][(len_3-1)] == position):
                        players_postions['player3'].append(0)
                else:
                    len_2 = len(players_postions['player2'])
                    len_1 = len(players_postions['player1'])
                    if (len_2 > 0 and players_postions['player2'][(len_2-1)] == position):
                        players_postions['player2'].append(0)
                    elif (len_1 > 0 and players_postions['player1'][(len_1-1)] == position):
                        players_postions['player1'].append(0)

        # print("Players history",players_history)
        # print("Players postions",players_postions)
        if position==borad_size:
            print("---------------WINNER---------")
            print(f"{player} is a winner")
            print("Players history--->>>",players_history)
            print("Players postions--->>>",players_postions)
            playing = False
            break
            

# df = pd.DataFrame()



    



