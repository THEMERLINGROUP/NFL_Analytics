from itertools import groupby
nfl_passing_leaders = [{'Name':'Tom Brady', 'Touchdowns':40, 'Pass yards':4990}, {'Name':'Matthew Stafford', 'Touchdowns':38, 'Pass yards':4648},
{'Name':'Aaron Rodgers', 'Touchdowns':35, 'Pass yards':3977}, {'Name':'Patrick Mahomes', 'Touchdowns':35, 'Pass yards':4569}, {'Name':'Justin Herbert', 'Touchdowns':35, 'Pass yards':4631},
{'Name':'Joe Burrow', 'Touchdowns':34, 'Pass yards':4611}]
group_passing = groupby(nfl_passing_leaders, key=lambda x:x['Pass yards'])
for key, value in group_passing:
    print(key, list(value))
nfl_rushing_leaders = [{'Name':'Jonathan Taylor', 'TDs':18, 'Rush Yards':1734}, {'Name':'Joe Mixon', 'TDs':13, 'Rush Yards':1205},
{'Name':'Nick Chubb', 'TDs':8, 'Rush Yards':1143}, {'Name':'Dalvin Cook', 'TDs':6, 'Rush Yards':1080}, {'Name':'Najee Harris', 'TDs':6, 'Rush Yards':984},
{'Name':'Derrick Henry', 'TDs':10, 'Rush Yards':937}]
group_rushing = groupby(nfl_rushing_leaders, key=lambda x:x['TDs'])
for key, value in group_rushing:
    print(key, list(value))
#Begins with receptions
nfl_receiving_leaders = [{'Cooper Kupp':138, 'Yards':1829, 'TDs':15}, {'Justin Jefferson':103, 'Yards':1509, 'TDs':9},{'Mark Andrews':99, 'Yards':1276, 'TDs':9},
{'Davante Adams':117, 'Yards':1498, 'TDs':11}, {'JaMarr Chase':79, 'Yards':1429, 'TDs':13}, {'Deebo Samuel':79, 'Yards':1310, 'TDs':6}, {'Tyreek Hill':110, 'Yards':1237, 'TDs':9}, {'Travis Kelce':88, 'Yards':'1091', 'TDs':8}]
group_receivers = groupby(nfl_receiving_leaders, key=lambda x:x['Yards'])
for key, value in group_receivers:
    print(key, list(value))
sack_leaders = [{'Name':'Robert Quinn', 'Sacks':18}, {'Name':'TJ Watt', 'Sacks':17.5}, {'Name':'Myles Garrett', 'Sacks':15}, {'Name':'Nick Bosa', 'Sacks':15},
{'Name':'Trey Hendrickson', 'Sacks':14}, {'Name':'Micah Parsons', 'Sacks':13}, {'Name':'Matt Judon', 'Sacks':12.5}, {'Name':'Aaron Donald', 'Sacks':12.5}, {'Name':'Harold Landry', 'Sacks':12}]
group_sacks = groupby(sack_leaders, key=lambda x:x['Sacks'])
for key, value in group_sacks:
    print(key, list(value))
Interception_Leaders = [{'Name':'Trevon Diggs', 'INT':11, 'TD':2},
{'Name':'JC Jackson', 'INT':8, 'TD':1}, {'Name':'Amani Oruwariye', 'INT':6, 'TD':0},
{'Name':'Justin Simmons', 'INT':5, 'TD':0}, {'Name':'Rasul Douglas', 'INT':5, 'TD':2}]
group_picks= groupby(Interception_Leaders, key=lambda x:x['INT'])
for key, value in group_picks:
    print(key, list(value))
