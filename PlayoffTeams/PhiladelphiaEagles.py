from itertools import groupby

from PlayoffTeams.GBPackers import Turnover_Ratio
made_playoffs = True
won_division = False
last_5_games = [{'Game':'Week 12', 'Outcome':'Loss', 'Score':'13-7'}, {'Game':'Week 13', 'Outcome':'Win', 'Score':'33-18'}, {'Game':'Week 15', 'Outcome':'Win', 'Score':'27-17'}, {'Game':'Week 16', 'Outcome':'Win', 'Score':'34-10'}, {'Game':'Week 17', 'Outcome':'Win', 'Score':'20-16'}]
group_last_5_games = groupby(last_5_games, key=lambda x:x['Score'])
for key, value in group_last_5_games:
    print(key, list(value))
Eagles_Vs_Opponents = [{'First Downs':330, 'First Downs Opponent':336}, {'Total Offensive Yards':5804, 'Opponents Offensive Yards':5115}, {'Sacks':28, 'Opponents Sacks':28}, {'TDs':47, 'Opponents TDs':40}]
Turnover_Ratio = +1
print(Eagles_Vs_Opponents)
