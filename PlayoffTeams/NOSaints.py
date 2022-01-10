from itertools import groupby
Taysom_vs_Jameis = [{'Name':'Taysom Hill', 'Yards':871, 'TD':3, 'INT':5, 'Completion Percentage':56.8, 'Games':7}, {'Name':'Jameis Winston', 'Yards':1170, 'TD':14, 'INT':3, 'Games':7}]
group_QBs = groupby(Taysom_vs_Jameis, key=lambda x:x['Completion Percentage'])
for key, value in group_QBs:
    print(key, list(value))
NO_Vs_Opponents = [{'First Downs':285, 'First Downs Opponent':291}, {'Total Offensive Yards':4808, 'Opponents Offensive Yards':5153}, {'Sacks':43, 'Opponents Sacks':36}, {'TDs':40, 'Opponents TDs':33}]
print(NO_Vs_Opponents)
Turnover_Ratio = +4
in_playoffs = False