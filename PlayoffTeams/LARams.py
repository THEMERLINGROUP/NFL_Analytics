from itertools import groupby
def function_rams_with_OBJ(stats):
    for x in stats:
        print(x)
statistics = ["Yards:287", "TD:5", "Rec:25", "Avg:11.5"]
function_rams_with_OBJ(statistics)
before_and_after_OBJ_Arrival = [{'Pre-OBJ':'7-2', 'TDs':15, 'INT':9}, {'Post-OBJ':'5-2', 'TDs':23, 'INT':6}]
group_Before_After_Injury = groupby(before_and_after_OBJ_Arrival, key=lambda x:x['TDs'])
for key, value in group_Before_After_Injury:
    print(key, list(value))
Rams_Vs_Opponents = [{'First Downs':336, 'First Downs Opponent':324}, {'Total Offensive Yards':6060, 'Opponents Offensive Yards':5414}, {'Sacks':49, 'Opponents Sacks':37}, {'TDs':49, 'Opponents TDs':37}]
print(Rams_Vs_Opponents)
Turnover_Ratio = +2
made_playoffs = True
won_division = False #TBD in Week 18
