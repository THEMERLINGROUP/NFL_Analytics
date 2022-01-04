from itertools import groupby, accumulate
before_and_after_JamarrChase = [{'Pre-Chase':'4-11-1', 'BurrowTDs':13, 'INT':5}, {'Post-Chase':'10-6', 'TDs':34, 'INT':14}]
group_Before_After = groupby(before_and_after_JamarrChase, key=lambda x:x['INT'])
for key, value in group_Before_After:
    print(key, list(value))
Burrow_yards = [4611, 2688]
acc = accumulate(Burrow_yards)
print(list(acc))
def function_burrow(stats):
    for x in stats:
        print(x)
careerstatistics = ["Yards:4990", "TD:40", "INT:12", "Passer Rating:100.5"]
function_burrow(careerstatistics)
Joe_Burrow = [{'Yards':4611, 'Rank':5}, {'TD':34, 'Rank':14}, {'QBR':53.9, 'Rank':11}]
burrow = groupby(Joe_Burrow, key=lambda x:x['Rank'])
for key, value in burrow:
    print(key, list(value))
Team_Leaders = [{'Passing Leader':'Joe Burrow', 'Yards':'4611'}, {'Rushing Leader':'Joe Mixon', 'Yards':1205}, {'Receiving Leader':'JaMarr Chase', 'Yards':1429},
{'Tackle Leader':'Logan Wilson', 'Tackles':100}, {'Sacks Leader':'Trey Hendrickson', 'Sacks':14}, {'INT Leader':'Logan Wilson', 'INTs':4}]
print(Team_Leaders)
won_divsion = True