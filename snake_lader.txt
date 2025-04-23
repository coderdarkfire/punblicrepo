# gird is going user define
# invalid dice roll

# cut position older player gets reset


# logic for the game


import random
# import pandas as pd


def roll_dice():
    return random.randint(1,6)



def movePlayer(player,rolled_dice):
    pass

def get_postion(postion,gird):
    main_potion = 1
    for i in range(gird):
        y = 0
        if i%2==0:
            for j in range(gird):
                # print('(',j,i,')',main_potion)
                if main_potion == postion:
                    y = j
                    return (y,i)
                main_potion+=1
        else:
            for j in range((gird-1),-1,-1):
                # print('(',j,i,')',main_potion)
                if main_potion == postion:
                    y = j
                    return (y,i)
                main_potion+=1
    return (y,i)

       
           
           

       
       


playing = True

gird = int(input("pls enter your gird size: "))
position  = 0
players = ["player1","player2","player3"]
players_history = {player:[] for player in players}
players_postions = {player:[] for player in players}
players_postions_cordinate = {player:[] for player in players}

borad_size = gird**2

# print("board sizee",borad_size)
# print(get_postion(9,gird))  

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
            players_postions_cordinate[player].append((get_postion(rolled_dice,gird)))

        else:
            position = rolled_dice + players_postions[player][length-1]
            if position <= borad_size :
                players_postions[player].append(position)
                players_postions_cordinate[player].append((get_postion(position,gird)))

        if player == "player1":
            len_2 = len(players_postions['player2'])
            len_3 = len(players_postions['player3'])

           
            if (len_2 > 0 and players_postions['player2'][(len_2-1)] == position):
                players_postions['player2'].append(0)
                # players_postions_cordinate['player2'].append(get_postion(0,gird))
                players_postions_cordinate['player2'].append((0,0))
            elif (len_3 > 0 and players_postions['player3'][(len_3-1)] == position):
                players_postions['player3'].append(0)
                # players_postions_cordinate['player3'].append(get_postion(0,gird))
                players_postions_cordinate['player3'].append((0,gird))
               
        elif player == 'player2':
            len_1 = len(players_postions['player1'])
            len_3 = len(players_postions['player3'])
            # print("len(len_1)",len(len_1))
            # print("len(len_3)",len(len_3))
            if (len_1 > 0 and players_postions['player1'][(len_1-1)] == position):
                players_postions['player1'].append(0)
                # players_postions_cordinate['player1'].append(get_postion(0,gird))
                players_postions_cordinate['player1'].append((0,0))
            elif (len_3 > 0 and players_postions['player3'][(len_3-1)] == position):
                players_postions['player3'].append(0)
                players_postions_cordinate['player3'].append((0,0))
                # players_postions_cordinate['player3'].append(get_postion(0,gird))
        else:
            len_2 = len(players_postions['player2'])
            len_1 = len(players_postions['player1'])
            if (len_2 > 0 and players_postions['player2'][(len_2-1)] == position):
                players_postions['player2'].append(0)
                # players_postions_cordinate['player2'].append(get_postion(0,gird))
                players_postions_cordinate['player2'].append((0,0))
            elif (len_1 > 0 and players_postions['player1'][(len_1-1)] == position):
                players_postions['player1'].append(0)
                # players_postions_cordinate['player1'].append(get_postion(0,gird))
                players_postions_cordinate['player1'].append((0,0))

        # print("Players history",players_history)
        # print("Players postions",players_postions)
        if position==borad_size:
            print("---------------WINNER---------")
            print(f"{player} is a winner")
            print('\n'*2)
            for player in players:
                print(player)
                print("Players history--->>>",players_history[player])
                print("Players postions --->>>",players_postions[player])
                print("Players postions coordinates--->>>",players_postions_cordinate[player])
            # print("Players history--->>>",players_history)
            # print("Players postions --->>>",players_postions)
            # print("Players postions coordinates--->>>",players_postions_cordinate)
            print('\n'*2)
            playing = False
            break

           




