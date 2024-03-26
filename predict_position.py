import joblib
import pandas as pd
import numpy as np
import plotly.graph_objects as go

def predict(input_data):
    clf = joblib.load("Player Position Prediction Model.sav")
    op = clf.predict(input_data)[0]
    pos_map = {"GK":"Goalkeeper", "DF":"Defender", "MF":"Midfielder", "FW":"Attacker (or) Forward"}
    return pos_map[op]

def plot_comparison_radar(position, data):
    means = pd.read_csv("Positional Attribute Means.csv",index_col="GroupedPosition")
    if position == "Goalkeeper":
        attr = ['Diving', 'Handling','Kicking','Positioning', 'Reflexes', 'Physicality']
        avg = np.array(means.loc["GK"][['GKDiving', 'GKHandling','GKKicking', 
                                        'GKPositioning', 'GKReflexes','PhysicalityTotal']])
    elif position == "Defender":
        attr = ['Pace', 'Shooting', 'Passing', 'Dribbling','Defending', 'Physicality']
        avg = np.array(means.loc["DF"][['PaceTotal', 'ShootingTotal', 'PassingTotal', 'DribblingTotal',
                                        'DefendingTotal', 'PhysicalityTotal']])
    elif position == "Midfielder":
        attr = ['Pace', 'Shooting', 'Passing', 'Dribbling','Defending', 'Physicality']
        avg = np.array(means.loc["MF"][['PaceTotal', 'ShootingTotal', 'PassingTotal', 'DribblingTotal',
                                        'DefendingTotal', 'PhysicalityTotal']])
    elif position == "Attacker (or) Forward":
        attr = ['Pace', 'Shooting', 'Passing', 'Dribbling','Defending', 'Physicality']
        avg = np.array(means.loc["FW"][['PaceTotal', 'ShootingTotal', 'PassingTotal', 'DribblingTotal',
                                        'DefendingTotal', 'PhysicalityTotal']])
    else:
        avg = None
    
    fig = go.Figure()
    
    fig.add_trace(go.Scatterpolar(
        r = list(avg),
        theta = list(attr),
        fill = 'toself',
        fillcolor = "red",
        name = "Positional Average"
    ))
    
    fig.add_trace(go.Scatterpolar(
        r = list(data),
        theta = list(attr),
        fill = 'toself',
        name = "Your Player"
    ))
    
    fig.update_layout(
        polar = dict(radialaxis = dict(visible=True,range = [0,100])),
        showlegend = True
    )
    
    return(fig)

def plot_comparison_radar_dataframe(player_data):
    p80 = pd.read_csv("Positional Attributes P80.csv", index_col="GroupedPosition")
    
    radar_plots = []
    
    for index, row in player_data.iterrows():
        player_name = row['Name']
        position = row['Predicted Position']
        
        if position == "Goalkeeper":
            attr = ['Diving', 'Handling', 'Kicking', 'Positioning', 'Reflexes', 'Physicality']
            player_stats = list(row[['GK Diving', 'GK Handling', 'GK Kicking', 'GK Positioning', 
                                     'GK Reflexes', 'Total Physicality']])
            pct80 = p80.loc["GK"][['GKDiving', 'GKHandling', 'GKKicking', 
                                             'GKPositioning', 'GKReflexes', 'PhysicalityTotal']]
        elif position == "Defender":
            attr = ['Pace', 'Shooting', 'Passing', 'Dribbling', 'Defending', 'Physicality']
            player_stats = list(row[['Total Pace', 'Total Shooting', 'Total Passing', 'Total Dribbling', 
                                     'Total Defending', 'Total Physicality']])
            pct80 = p80.loc["DF"][['PaceTotal', 'ShootingTotal', 'PassingTotal', 'DribblingTotal',
                                             'DefendingTotal', 'PhysicalityTotal']]
        elif position == "Midfielder":
            attr = ['Pace', 'Shooting', 'Passing', 'Dribbling', 'Defending', 'Physicality']
            player_stats = list(row[['Total Pace', 'Total Shooting', 'Total Passing', 'Total Dribbling', 
                                     'Total Defending', 'Total Physicality']])
            pct80 = p80.loc["MF"][['PaceTotal', 'ShootingTotal', 'PassingTotal', 'DribblingTotal',
                                             'DefendingTotal', 'PhysicalityTotal']]
        elif position == "Attacker (or) Forward":
            attr = ['Pace', 'Shooting', 'Passing', 'Dribbling', 'Defending', 'Physicality']
            player_stats = list(row[['Total Pace', 'Total Shooting', 'Total Passing', 'Total Dribbling', 
                                     'Total Defending', 'Total Physicality']])
            pct80 = p80.loc["FW"][['PaceTotal', 'ShootingTotal', 'PassingTotal', 'DribblingTotal',
                                             'DefendingTotal', 'PhysicalityTotal']]
        else:
            pct80 = None
        
        fig = go.Figure()
        
        fig.add_trace(go.Scatterpolar(
            r=list(pct80) + [pct80[0]],
            theta=attr + [attr[0]],
            fill='none',
            fillcolor="orange",
            mode='lines',
            line_color='orange',
            name="80th Percentile"
        ))
        
        fig.add_trace(go.Scatterpolar(
            r=player_stats + [player_stats[0]],
            theta=attr + [attr[0]],
            fill='none',
            fillcolor="blue",
            mode='lines',
            line_color='blue',
            name=player_name
        ))
        
        fig.update_layout(
            polar=dict(
                radialaxis=dict(visible=True, range=[0, 100]),
            ),
            showlegend=True,
            title=dict(
                text=player_name + " - " + position,
                x=0.5,
                font=dict(size=16)
            ),
            font=dict(
                family="Courier New, monospace",
                size=12,
                color="red"
            ),
            plot_bgcolor='white'  # Changed plot background color to white
        )
        
        radar_plots.append(fig)
    
    return radar_plots