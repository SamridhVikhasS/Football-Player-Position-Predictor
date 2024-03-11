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