from itertools import groupby, accumulate
Fastest_Ball_Carriers= [{'player':'Jonathan Taylor', 'speed':22.13}, {'player':'Marquez Valdes-Scantling', 'speed':22.09},
{'player':'Patrick Surtain', 'speed':22.07}, {'player':'Jonathan Taylor', 'speed':22.05}, {'player':'Jonathan Taylor', 'speed':21.83}]
group_speed = groupby(Fastest_Ball_Carriers, key=lambda x:x['speed'])
for key, value in group_speed:
    print(key, list(value))
Jonathan_Taylor_Total_Yards = [1734, 1169]
acc = accumulate(Jonathan_Taylor_Total_Yards)
print(list(acc))
Jonathan_Taylor_Stats = [{'Attempts':317, 'Rank':1}, {'Yards':1734, 'Rank':1}, {'TD':18, 'Rank':1},
{'AVG':5.5, 'Rank':7}]
Taylor_Ranking = groupby(Jonathan_Taylor_Stats, key=lambda x:x['Rank'])
for key, value in Taylor_Ranking:
    print(key, list(value))
def Carson_Wentz(numbers):
    for x in numbers:
        print(x)
Wentz_Stats_Rankings = ["Yards: 3378(17th)", "TD:26(10th)", "INT:6(4th)", "QBR:58.4(8th)"]
Carson_Wentz(Wentz_Stats_Rankings)
Last_Five_Games = [{'Result':'Loss', 'Score':'Bucs 38 - Colts 31'}, {'Result':'Win', 'Score':'Colts 31 - Texans 0'}, {'Result':'Win', 'Score':'Colts 27 - Patriots 17'},
{'Result':'Win', 'Score':'Colts 22 - Arizona Cardinals 16'}, {'Result':'Loss', 'Score':'Raiders 23 - Colts 20'}]
group_sports_obj=groupby(Last_Five_Games, key=lambda x:x['Score'])
for key, value in group_sports_obj:
    print(key, list(value))
in_playoffs = False #WIN against Houston in Week 18 and IN