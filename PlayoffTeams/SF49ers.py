from itertools import groupby
Trey_Lance_vs_Jimmy_G = [{'Name':'Trey Lance', 'Yards':'603', 'TD':5, 'INT':2, 'QBR':35.4}, {'Name':'Jimmy Garoppolo', 'Yards':3494, 'TD':19, 'INT':10, 'QBR':53.8}]
qbs_group = groupby(Trey_Lance_vs_Jimmy_G, key=lambda x:x['QBR'])
for key, value in qbs_group:
    print(key, list(value))
SF_Vs_Opponents = [{'First Downs':338, 'First Downs Opponent':299}, {'Total Offensive Yards':5938, 'Opponents Offensive Yards':5005}, {'Sacks':43, 'Opponents Sacks':30}, {'TDs':47, 'Opponents TDs':40}]
print(SF_Vs_Opponents)
Turnover_Ratio = -4
made_playoffs = False #WIN and in 
