from itertools import groupby, accumulate
Mac_Jones = [{'Yards':3540, 'Rank':13}, {'TD':21, 'Rank':13}, {'INT':12, 'Rank':20}, {'QBR':54.3, 'Rank':9}]
Rankings = groupby(Mac_Jones, key=lambda x:x['Rank'])
for key, value in Rankings:
    print(key, list(value))
Team_Rankings = [{'Passing Yards':225.8, 'Rank':15}, {'Rushing Yards':126.1, 'Rank':8}, {'Points For':27.4, 'Rank':8},
{'Points Against':16.9, 'Rank':1}]
obj_Team = groupby(Team_Rankings, key=lambda x:x['Rank'])
for key, value in obj_Team:
    print(key, list(value))
Team_Leaders = [{'Passing Leader':'Mac Jones', 'Yards':'3540', 'TD':21, 'QBR':54.3}, {'Rushing Leader':'Damien Harris', 'Yards':892, 'Carries':191, 'TD':14}, {'Receiving Leader':'Jakobi Meyers', 'Yards':796, 'Receptions':79, 'TD':2},
{'Tackle Leader':'Kyle Dugger', 'Tackles':92}, {'Sacks Leader':'Matthew Judon', 'Sacks':12.5}, {'INT Leader':'JC Jackson', 'INTs':8}]
print(Team_Leaders)
made_playoffs = True
won_division = False #WIN AND Buffalo Loss and they win the division