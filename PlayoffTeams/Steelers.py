from itertools import accumulate
#class for Big Ben this year 
class BigBen:
    def __init__(self):
        self.name=("Ben Roethlisberger")
        self.age = 39
        self.completionpercentage = 64.5
        self.yards = 3740
        self.touchdowns = 22
        self.interceptions = 10
        self.passerrating = 86.8
        self.qbr=35.8
        pass
b1=BigBen()
b2=BigBen()
b3=BigBen()
b4=BigBen()
b5=BigBen()
b6=BigBen()
b7=BigBen()
b8=BigBen()
print(b1.name)
print(b2.age)
print(b3.completionpercentage)
print(b4.yards)
print(b5.touchdowns)
print(b6.interceptions)
print(b7.passerrating)
print(b8.qbr)

Ben_Career = [{'Yards':64088, 'Completion Percentage':64.4, 'Passer Rating':93.5, 'Seasons':18}, {'Touchdowns':418, 'Interceptions':211}, {'Pro Bowls':6, 'Super Bowls':2, 'AFC North Championships':8, 'MVPs':0}]
td_int_ratio = lambda touchdowns, interceptions: touchdowns/interceptions
print(td_int_ratio(418,211))
Ben_QBR_avg = [58,70.5,47.1,69,67.4,68.3,71.9,58,69.4,72.8,60.5,67.2,69.6,28.8,52.5,35.8]
acc = accumulate(Ben_QBR_avg)
print(list(acc))
#966.8
AVG_QB= lambda total_QBR, seasons_played: total_QBR/seasons_played
print(AVG_QB(966.8,16))
Team_Leaders = [{'Passing Leader':'Ben Roethlisberger', 'Yards':'3740'}, {'Rushing Leader':'Najee Harris', 'Yards':1200}, {'Receiving Leader':'Diontae Johnson', 'Yards':1161},
{'Tackle Leader':'Minkah Fitzpatrick', 'Tackles':124}, {'Sacks Leader':'TJ Watt', 'Sacks':22.5}, {'INT Leader':'Ahkello Witherspoon', 'INTs':3}]
print(Team_Leaders)
made_playoffs = True