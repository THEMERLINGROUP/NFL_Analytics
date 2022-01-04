from itertools import product, groupby
Aaron_Rodgers = [{'Year':2021,'Touchdowns':35, 'Interceptions':4},
{'Year':2020, 'Touchdowns':48, 'Interceptions':5},
{'Year':2019, 'Touchdowns':26, 'Interceptions':4}]
Next_Gen_Rodgers = [{'Passer Rating':105.7, 'Completion Percentage':67.1}, {'Yards':3977}]
#One game left in 2021 season
Year = ['2021', '2020', '2019']
Wins= ['13', '13', '13']
prod = product(Year, Wins)
print(list(prod))
Packers_Vs_Opponents = [{'First Downs':353, 'First Downs Opponent':318}, {'Total Offensive Yards':5837, 'Opponents Offensive Yards':5175}, {'Sacks':38, 'Opponents Sacks':29}, {'TDs':50, 'Opponents TDs':41}]
Fastest_Ball_Carriers= [{'player':'Jonathan Taylor', 'Speed':22.13}, {'player':'Marquez Valdes-Scantling', 'Speed':22.09},
{'player':'Patrick Surtain', 'Speed':22.07}, {'player':'Jonathan Taylor', 'speed':22.05}, {'player':'Jonathan Taylor', 'speed':21.83}]
group_speed = groupby(Fastest_Ball_Carriers, key=lambda x:x['Speed'])
for key, value in group_speed:
    print(key, list(value))
Turnover_Ratio = +16
won_division = True
Number_One_Overall_Seed = True
in_playoffs = True