import numpy as np
import pandas as pd
seasons = [str(season) for season in range(2010,2023)]
print(f'number of seasons = {len(seasons)}')
team_abbrs = ['crd', 'atl', 'rav','buf','car','chi','cle','dal','den','det']
print(f'number of teams = {len(team_abbrs)}')

import time
import random
nfl_df = pd.DataFrame()
for season in seasons:
    for team in team_abbrs:
        url = 'https://www.pro-football-reference.com/teams/' + team + '/' + season +'/gamelog/'
        print(url)
        off_df = pd.read_html(url, header=1, attrs ={'id':'gamelog' + season})[0]
        def_df = pd.read_html(url, header=1, attrs ={'id':'gamelog_opp' + season})[0]
        team_df = pd.concat([off_df, def_df],axis=1)
        team_df.insert(loc=0,column='Season',value=season)
        team_df.insert(loc=2, column='Team', value=team.upper())
        nfl_df = pd.concat([nfl_df, team_df],ignore_index=True)
        time.sleep(random.randint(4,5))
    print(nfl_df)
    nfl_df.to_csv('nfl_gamelogs_2010-2023.csv', index=False)
