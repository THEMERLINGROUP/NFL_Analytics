from itertools import groupby, accumulate
Josh_Allen = [{'Yards':4168, 'Rank':7}, {'TD':34, 'Rank':6}, {'INT':15, 'Rank':29}, {'QBR':61, 'Rank':6}]
Rankings = groupby(Josh_Allen, key=lambda x:x['Rank'])
for key, value in Rankings:
    print(key, list(value))
Team_Rankings = [{'Passing Yards':251.9, 'Rank':10}, {'Rushing Yards':127.4, 'Rank':6}, {'Points For':28.5, 'Rank':3},
{'Points Against':17.4, 'Rank':2}]
Team = groupby(Team_Rankings, key=lambda x:x['Rank'])
for key, value in Team:
    print(key, list(value))
Interception_Total = [12, 9, 10, 15]
acc = accumulate(Interception_Total)
print(list(acc))
TD_totals = [10,20,37,34]
td_acc_Josh_Allen = accumulate(TD_totals)
print(list(td_acc_Josh_Allen))
td_int_avg_Josh_Allen = lambda TD,INT: TD/INT
print(td_int_avg_Josh_Allen(101, 46))
Team_Leaders = [{'Passing Leader':'Josh Allen', 'Yards':'4168'}, {'Rushing Leader':'Devin Singletary', 'Yards':782}, {'Receiving Leader':'Stefon Diggs', 'Yards':1144},
{'Tackle Leader':'Tremaine Edmunds', 'Tackles':104}, {'Sacks Leader':'Mario Addison', 'Sacks':5}, {'INT Leader':'Micah Hyde', 'INTs':5}]
print(Team_Leaders)
made_playoffs = True
won_division = False #WIN AND THE DIVISION IS THERES