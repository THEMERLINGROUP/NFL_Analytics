from itertools import groupby, accumulate
import gc
Team_Rankings = [{'Passing Yards':274.7, 'Rank':6}, {'Rushing Yards':90.2, 'Rank':28}, {'Points For':21.2, 'Rank':18},
{'Points Against':25.4, 'Rank':24}]
Team = groupby(Team_Rankings, key=lambda x:x['Rank'])
for key, value in Team:
    print(key, list(value))
Team_Leaders = [{'Passing Leader':'Derek Carr', 'Yards':'4618', 'TD':21, 'QBR':55.1}, {'Rushing Leader':'Josh Jacobs', 'Yards':740, 'Carries':191, 'TD':8}, {'Receiving Leader':'Hunter Renfrow', 'Yards':1025, 'Receptions':99, 'TD':7},
{'Tackle Leader':'Denzel Perryman', 'Tackles':145}, {'Sacks Leader':'Yannick Ngakoue', 'Sacks':10}, {'INT Leader':'Brandon Facyson', 'INTs':1}]
print(Team_Leaders)
Last_Five_Games = [{'Result':'Loss', 'Score':'Washington 17 - Raiderss 15'}, {'Result':'Loss', 'Score':'Chiefs 48 - Raiders 9'}, {'Result':'Win', 'Score':'Raiders 16 - Browns 14'},
{'Result':'Win', 'Score':'Broncos 17 - Raiders 13'}, {'Result':'Win', 'Score':'Raiders 23 - Colts 20'}]
group_sports_obj=groupby(Last_Five_Games, key=lambda x:x['Score'])
for key, value in group_sports_obj:
    print(key, list(value))
Derek_Carr_Total_YARDS = [4618, 4103, 4054, 4049, 3496, 3987, 3270]
Carr_acc = accumulate(Derek_Carr_Total_YARDS)
print(list(Carr_acc))
in_playoffs = False #WIN and IN vs Chargers on SNF
Raiders_V_Chargers_With_Herbert = [{'Score':'Chargers 28 - Raiders 14'}, {'Score':'Chargers 30 - Raiders 27'},
{'Score':'Raiders 31 - Chargers 26'}]
Carr_vs_Herbert = [{'Name':'Derek Carr', 'Yards':4618, 'TD':21, 'INT':14, 'Completion Percentage':69.2, 'Passer Rating':94.3}, {'Name':'Justin Herbert', 'Yards':4631, 'TD':35, 'INT':14, 'Completion Percentage':67.3, 'Passer Rating':99.5}]
group_QBs = groupby(Carr_vs_Herbert, key=lambda x:x['TD'])
for key, value in group_QBs:
    print(key, list(value))
td_int_ratio = lambda td,int:td/int
print(td_int_ratio(21,14))
beat_chargers_on_SNF = True
if(beat_chargers_on_SNF == True):
    print("Raiders are in the Playoffs")
else:
    print("Chargers are in the playoffs")
del in_playoffs
gc.enable()
playoff_team = True
