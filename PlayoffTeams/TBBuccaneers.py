from itertools import groupby
losses= [('Rams','34-24'), ('Saints', '36-27'), ('Washington', '29-19'), ('Saints', '9-0')]
Ls_sorted= sorted(losses, key=lambda x:x[1])
print(Ls_sorted)
def function_tom_brady(stats):
    for x in stats:
        print(x)
statistics = ["Yards:4990", "TD:40", "INT:12", "Passer Rating:100.5"]
function_tom_brady(statistics)
def antoniobrown(y):
    return y+y
yards = (121,17,63,124,93,101,26)
result = map(antoniobrown, yards)
print(list(result))
tom_brady_bucs_vs_pats_TDs = [{'Year':2021, 'TDs':40, 'INT':12}, {'Year':2020, 'TDs':40, 'INT':12},
{'Year':2019, 'TDs':24, 'INT':8}, {'Year':2018, 'TDs':29, 'INT':11}]
group_TDs = groupby(tom_brady_bucs_vs_pats_TDs, key=lambda x:x['TDs'])
for key, value in group_TDs:
    print(key, list(value))
TURNOVER_RATIO_TB12_2021 = lambda touchdowns, interceptions: touchdowns/interceptions
print(TURNOVER_RATIO_TB12_2021(40, 12))
Team_Leaders = [{'Passing Leader':'Tom Brady', 'Yards':'4990'}, {'Rushing Leader':'Leonard Fournette', 'Yards':812}, {'Receiving Leader':'Chris Godwin', 'Yards':1103},
{'Tackle Leader':'Devin White', 'Tackles':84}, {'Sacks Leader':'Shaquil Barrett', 'Sacks':10}, {'INT Leader':'Mike Edwards', 'INTs':3}]
Turnover_Ratio = +8
Bucs_Vs_Opponents = [{'First Downs':383, 'First Downs Opponent':326}, {'Total Offensive Yards':6492, 'Opponents Offensive Yards':5318}, {'Sacks':45, 'Opponents Sacks':22}, {'TDs':58, 'Opponents TDs':37}]
print(Bucs_Vs_Opponents)
won_division = True
in_Playoffs = True
