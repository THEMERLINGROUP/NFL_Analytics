from itertools import groupby, accumulate
OFTeam_Leaders = [{'Passing Leader':'Dak Prescott', 'Yards':4154},
{'Rushing Leader':'Ezekiel Elliot', 'Yards':915}, {'Receiving Leader':1057, 'Yards':1057}]
group_OF_Leaders = groupby(OFTeam_Leaders, key=lambda x:x['Yards'])
for key, value in group_OF_Leaders:
    print(key, list(value))
Total_Penalties = [8,8,4,7,8,12,11,5,8,6,14,5,7,6,3,10]
acc = accumulate(Total_Penalties)
print(list(acc))
Def_Leaders = [{'Tackle Leader':'Jayron Kearse', 'Tackles':67}, {'Sack Leader':'Micah Parsons', 'Sacks':13}, {'INT leader':'Trevon Diggs', 'INTs':13}]
print(Def_Leaders)
Cowboys_Vs_Opponents = [{'First Downs':368, 'First Downs Opponent':305}, {'Total Offensive Yards':6444, 'Opponents Offensive Yards':5652}, {'Sacks':38, 'Opponents Sacks':32}, {'TDs':57, 'Opponents TDs':36}]
print(Cowboys_Vs_Opponents)
Turnover_Ratio = +13
won_division = True
in_playoffs = True