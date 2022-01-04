from itertools import product, groupby, accumulate
Division_Title_Streak = True
if(Division_Title_Streak == True):
    print("Chiefs have won the division in six straight seasons")
Years = [2016, 2017, 2018, 2019, 2020, 2021]
Division = ['Chiefs Won Division']
prod = product(Years, Division)
print(list(prod))
Mahomes_this_year_vs_MVP_Season = [{'Year':2021,'Completion Percentage':66.6, 'Yards':'4569', 'TD':35, 'INT':13, 'Passer Rating':98.8},
 {'Year':2018, 'Completion Percentage':66, 'Yards':5097, 'TD':50, 'INT':12, 'Passer Rating':113.8}]
groupMahomes = groupby(Mahomes_this_year_vs_MVP_Season, key=lambda x:x['TD'])
for key, value in groupMahomes:
    print(key, list(value))
Total_Mahomes_Yards = [4569, 4740, 4031, 5097, 284]
the_acc = accumulate(Total_Mahomes_Yards)
print(list(the_acc))
Total_Mahomes_TDs = [35,38,26,50,0]
TD_acc = accumulate(Total_Mahomes_TDs)
print(list(TD_acc))
Total_Mahomes_INT = [13, 6, 5, 12, 1]
INT_acc = accumulate(Total_Mahomes_INT)
print(list(INT_acc))
Team_Leaders = [{'Passing Leader':'Patrick Mahomes', 'Yards':'4569'}, {'Rushing Leader':'Darrel Williams', 'Yards':514}, {'Receiving Leader':'Tyreek Hill', 'Yards':1237},
{'Tackle Leader':'Nick Bolton', 'Tackles':106}, {'Sacks Leader':'Chris Jones', 'Sacks':9}, {'INT Leader':'Tyrann Mathieu', 'INTs':3}]
print(Team_Leaders)
in_playoffs = True
number_one_seed = False #NEEDS A win in WEEK 18 and a Titans Loss

