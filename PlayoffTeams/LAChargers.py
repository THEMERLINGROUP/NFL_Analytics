from itertools import groupby, accumulate
Justin_Herbert = [{'Yards':4631, 'Rank':3}, {'TD':35, 'Rank':3}, {'INT':14, 'Rank':25}, {'QBR':66.3, 'Rank':3}]
Rankings = groupby(Justin_Herbert, key=lambda x:x['Rank'])
for key, value in Rankings:
    print(key, list(value))
Team_Leaders = [{'Passing Leader':'Justin Herbert', 'Yards':'4631', 'TD':35, 'QBR':66.9}, {'Rushing Leader':'Austin Ekeler', 'Yards':847, 'Carries':190, 'TD':11}, {'Receiving Leader':'Keenan Allen', 'Yards':1086, 'Receptions':100, 'TD':6},
{'Tackle Leader':'Kyzir White', 'Tackles':137}, {'Sacks Leader':'Joey Bosa', 'Sacks':9.5}, {'INT Leader':'Derwin James JR', 'INTs':2}]
print(Team_Leaders)
Team_Rankings = [{'Passing Yards':277.8, 'Rank':4}, {'Rushing Yards':109.3,'Rank':20}, {'Points For':27.6, 'Rank':26.5}]
Team = groupby(Team_Rankings, key=lambda x:x['Rank'])
for key, value in Team:
    print(key, list(value))
Last_Five_Games = [{'Result':'WIN', 'Score':'Chargers 41 - Bengals 22'}, {'Result':'WIN', 'Score':'Giants 37 - Chargers 21'}, {'Result':'LOSS', 'Score':'Chiefs 34 - Chargers 28'},
{'Result':'LOSS', 'Score':'Texans 41 - Chargers 29'}, {'Result':'Win', 'Score':'Chargers 34 - Broncos 28'}]
group_sports_obj=groupby(Last_Five_Games, key=lambda x:x['Score'])
for key, value in group_sports_obj:
    print(key, list(value))
Raiders_V_Chargers_With_Herbert = [{'Score':'Chargers 28 - Raiders 14'}, {'Score':'Chargers 30 - Raiders 27'},
{'Score':'Raiders 31 - Chargers 26'}]
Carr_vs_Herbert = [{'Name':'Derek Carr', 'Yards':4618, 'TD':21, 'INT':14, 'Completion Percentage':69.2, 'Passer Rating':94.3}, {'Name':'Justin Herbert', 'Yards':4631, 'TD':35, 'INT':14, 'Completion Percentage':67.3, 'Passer Rating':99.5}]
group_QBs = groupby(Carr_vs_Herbert, key=lambda x:x['TD'])
for key, value in group_QBs:
    print(key, list(value))
Herbert_TotalTDs = [35,31]
herb_acc = accumulate(Herbert_TotalTDs)
print(list(herb_acc))
Herbert_total_YDs = [4631, 4336]
yards_acc = accumulate(Herbert_total_YDs)
print(list(yards_acc))
td_int_ratio = lambda td,int:td/int
print(td_int_ratio(66,24))
in_playoffs = False #PLAY Raiders on SNF WIN and IN
beat_raiders_on_SNF = True
if(beat_raiders_on_SNF == True):
    print("Chargers are in the Playoffs")
else:
    print("Raiders are in the playoffs")