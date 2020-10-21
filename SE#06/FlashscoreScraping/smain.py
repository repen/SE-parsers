from statistics import Statistics

# Statistics startup
stat = Statistics()

# get all matches where the Atletico MG win in 2018
# result = stat.get_win_matches('brazil', 'serie-a', 'Atletico-MG', 2018)
result = stat.get_teams('brazil', 'serie-a', 2018)
result = stat.get_statistic_by_team('brazil', 'serie-a', 'Atletico-MG', 'dangerous_attacks', 2018)
result = stat.get_statistic_by_team('brazil', 'serie-a', 'Atletico-MG', 'goal_attempts', 2018)

# import pdb;pdb.set_trace()

print(result)

# # get all matches where the Atletico MG lost between 2014 and 2016
# statistics.get_lose_matches('brazil', 'serie-a', 'Atletico-MG', 2016, 2014)

# # get all matches where the Atletico MG draw in 2015
# statistics.get_draw_matches('brazil', 'serie-a', 'Atletico-MG', 2015)

# # get all possession ball of Bayern Munich in 2019
# statistics.get_statistic_by_team('germany', 'bundesliga', 'Bayern Munich', statistic, 2017)

# # get all the names of teams that participated in the Premier League in 2019
# statistics.get_teams('england', 'premier-league', 2013)