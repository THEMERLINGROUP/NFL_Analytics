from itertools import groupby
Kyler_Murray = [{'Yards':3547, 'Passer Rating':100.9},{'Touchdowns':23, 'Interceptions':10}, {'Completion Percentage':69, 'Expected Completion Percentage':64.8}]
td_int_ratio = lambda touchdowns, interceptions: touchdowns/interceptions
print(td_int_ratio(23,10))
clinched_playoffs = True
won_division = False #TBD in WEEK18
Team_Leaders = [{'Passing Leader':'Kyler Murray', 'Yards':'3547'}, {'Rushing Leader':'James Conner', 'Yards':700}, {'Receiving Leader':'Christian Kirk', 'Yards':939},
{'Tackle Leader':'Jalen Thompson', 'Tackles':75}, {'Sacks Leader':'Markus Golen', 'Sacks':11}, {'INT Leader':'Byron Murphy', 'INTs':4}]
Turnover_Ratio = +11
Cardinals_Vs_Opponents = [{'First Downs':347, 'First Downs Opponent':317}, {'Total Offensive Yards':6047, 'Opponents Offensive Yards':5166}, {'Sacks':40, 'Opponents Sacks':34}, {'TDs':49, 'Opponents TDs':37}]
print(Cardinals_Vs_Opponents)
#It is a small sample size but a neccessary metric
before_and_after_DHOP_injury = [{'Pre-Injury':'10-2', 'TDs':20, 'INT':7}, {'Post-Injury':'1-2', 'TDs':3, 'INT':3}]
group_Before_After_Injury = groupby(before_and_after_DHOP_injury, key=lambda x:x['INT'])
for key, value in group_Before_After_Injury:
    print(key, list(value))
