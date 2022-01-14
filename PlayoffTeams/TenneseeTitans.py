from itertools import groupby
#First dictionary are Derrick Henry Alone vs all of the other RBs
before_and_after_DerrickHenry_injury = [{'Pre-Injury':'6-2', 'RushingTDs':10, 'Rushing Yards':937}, {'Post-Injury':'6-2','RushingTDs':6, 'Rushing Yards':1028}]
Derrick_Henry_vs_team = groupby(before_and_after_DerrickHenry_injury, key=lambda x:x['RushingTDs'])
for key, value in Derrick_Henry_vs_team:
    print(key, list(value))
Titans_Vs_Opponents = [{'First Downs':339, 'First Downs Opponent':313}, {'Total Offensive Yards':5417, 'Opponents Offensive Yards':5254}, {'Sacks':41, 'Opponents Sacks':46}, {'TDs':45, 'Opponents TDs':35}]
print(Titans_Vs_Opponents)
Turnover_Ratio = -3
made_playoffs = True
won_division = True
clinched_number_one_seed = True
