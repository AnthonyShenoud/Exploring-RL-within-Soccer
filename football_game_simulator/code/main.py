#!/usr/bin/python
# -*- coding: utf-8 -*-

# MIT LICENSE @copyright 2023 Mycode Development

"""
An 11 versus 11 football game simulator project, developed by Mycode Development.
This is the main executed file.
"""

import display_console as display_console
import stats as stats
import constant as constant
from create_teams import * 

import random
#from colorama import Fore
import time


def main(action_joueur, half_time_ballon, timeDisplay):
    global gameTime, timePerAction, halfTime
    result = 0 
    temps = 0 #minutes since the start of the match
    temps_log = halfTime
    
    #print(Fore.LIGHTRED_EX + textLanguage[11][0] + list_player[action_joueur].Return_nom() + Fore.RESET)
    #print()
    
    while temps <= gameTime:
        
        action_joueur = list_player[int(action_joueur)].random_action(temps, list_player)
        temps += timePerAction
        
        if int(temps) == temps_log: #half time
            
            action_joueur = half_time_ballon #ball to the team that did not have the commitment
            #print(Fore.LIGHTRED_EX + textLanguage[12][0])
            #print(Fore.LIGHTRED_EX +textLanguage[13][0] +  list_player[action_joueur].Return_nom() + Fore.RESET)
            temps_log = -15
        
        #time.sleep(timeDisplay)
    
    #print(Fore.LIGHTBLUE_EX + Fore.LIGHTRED_EX +textLanguage[14][0] + Fore.RESET)
    
    stat1, stat2 = stats.get_stats(list_player)
    #time.sleep(timeDisplay)
    #stats.display_stats(stat1 , stat2, team1, team2, textLanguage[15])

    if stat1['Goals'] > stat2['Goals']:
        result = 1
    elif stat1['Goals'] < stat2['Goals']:
        result = 2
    else:
        result = 0
    stats.reset_stats(list_player)
    return result


#display_console.Clear()

#get data
gameTime = constant.GAME_TIME
timePerAction = constant.TIME_PER_ACTION
halfTime = constant.HALF_TIME

team1, team2 = constant.NAME_TEAM

timeDisplay = constant.TIME_DISPLAY

textLanguage = constant.TEXT_LANGUAGE[constant.LANGUAGE]

#create teams / inteligent composition

data = get_json_player()
dispo1, dispo2, adversary_team, id_dispo1, id_dispo2 = create_team_composition(data)

list_player = create_player(data, adversary_team, [id_dispo1, id_dispo2], textLanguage)

#display composition
#display_console.write_dispo(team1, dispo1, Fore.LIGHTYELLOW_EX, textLanguage[15][0])
#display_console.write_dispo(team2, dispo2, Fore.LIGHTGREEN_EX, textLanguage[15][0])


team1_total = 0
team2_total = 0
draws = 0 

#start of the game 
for i in range(10000):
    #prize draw
    draw_result = random.randint(0, 1)

    if draw_result == 1:
        half_time_ball = 21
        player_action = 10
    else:
        player_action = 21
        half_time_ball = 10

    result = main(player_action, half_time_ball, timeDisplay) #main function
    if result == 1:
        team1_total +=1
    elif result == 2:
        team2_total +=1
    else:
        draws +=1

print(team1_total)
print(team2_total)
print(draws)


