import streamlit as st
from itertools import combinations

def generate_teams(players, num_teams):
    teams = []
    for c in combinations(players, 11):
        for vc in combinations(c, 1):
            for cap in combinations(c, 1):
                if vc != cap:
                    team = list(c)
                    team.remove(vc[0])
                    team.remove(cap[0])
                    team.append(('VC', vc[0]))
                    team.append(('C', cap[0]))
                    teams.append(team)
        if len(teams) >= num_teams:
            break
    return teams[:num_teams]

st.title('Dream11 Team Generator')

# Input the list of players
players = st.text_input('Enter the list of players (separated by commas)')

# Input the number of teams to generate
num_teams = st.slider('Number of teams', 1, 1000, 10)

if st.button('Generate Teams'):
    players_list = players.split(',')
    teams = generate_teams(players_list, num_teams)

    # Display the teams in a table
    for i in range(num_teams):
        st.write(f'Team {i+1}')
        columns = st.columns(11)
        for j, player in enumerate(teams[i]):
            if isinstance(player, tuple):
                columns[j].write(f'{player[0]}: {player[1]}')
            else:
                columns[j].write(player)
                
    st.code("© Developed by Mr. Sangam Bhamare & SQUAD. All rights reserved.")
