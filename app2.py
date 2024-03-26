import streamlit as st
import numpy as np
import pandas as pd
from io import StringIO
import predict_position as pp

st.title("From Benchwarmer to Ballhawk - Optimal Player Position Predictor")

import streamlit as st

st.markdown("""
### 🚀 Welcome to Football Player Position Predictor! ⚽️

Ready to unravel the mystery of where your favorite players shine on the field? 🤔
Just enter their stats and let our magical model do the rest! 🌟
Whether they're a Speedy Striker 🏃‍♂️, a Powerful Defender 🛡️, or a Masterful Midfielder ⚙️, we've got you covered!
Let's kick off and discover the best spot for your player to rule the game! 🌟

**Note:** 📝 All player stats should be scaled to **100** for best prediction accuracy!
""")
st.divider()

st.markdown("From below, choose the approach you would like to use to predict position(s)")
option = st.radio("Choose the suitable method", ["Enter Manually","Upload csv"])

if option == "Enter Manually":
    name = st.text_input("Name",placeholder="Enter Player Name")
    st.header("Total Player Performace Metrics")
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        attacking_work_rate = st.select_slider("Attacking Work Rate",
                                               options=["Low", "Medium", "High"])
        total_dribbling = st.text_input("Dribbling Total")
    with col2:
        defensive_work_rate = st.select_slider("Defensive Work Rate",
                                               options=["Low", "Medium", "High"])
        total_defending = st.text_input("Defending Total")
    with col3:
        total_pace = st.text_input("Pace Total")
        total_physicality = st.text_input("Physicality Total")
    with col4:
        total_shooting = st.text_input("Shooting Total")
        total_passing = st.text_input("Passing Total")

    st.header("In-depth Player Attributes")
    col1, col2, col3, col4, col5, col6 = st.columns(6)
    with col1:
        crossing = st.text_input("Crossing")
        curve = st.text_input("Curve")
        agility = st.text_input("Agility")
        strength = st.text_input("Strength")
        penalties = st.text_input("Penalties")
        goalkeeper_handling = st.text_input("GK Handling")

    with col2:
        finishing = st.text_input("Finishing")
        fk_accuracy = st.text_input("Freekick Accuracy")
        reactions = st.text_input("Reactions")
        long_shots = st.text_input("Long Shot")
        composure = st.text_input("Composure")
        goalkeeper_kicking = st.text_input("GK Kicking")

    with col3:
        heading_accuracy = st.text_input("Heading Accuracy")
        long_passing = st.text_input("Long Passing")
        balance = st.text_input("Balance")
        aggression = st.text_input("Aggression")
        marking = st.text_input("Marking")
        goalkeeper_positioning = st.text_input("GK Positioning")

    with col4:
        short_passing = st.text_input("Short Passing")
        ball_control = st.text_input("Ball Control")
        shot_power = st.text_input("Shot Power")
        interceptions = st.text_input("Interceptions")
        standing_tackle = st.text_input("Standing Tackle")
        goalkeeper_reflexes = st.text_input("GK Reflexes")

    with col5:
        volleys = st.text_input("Volleys")
        accelaration = st.text_input("Accelaration")
        jumping = st.text_input("Jumping")
        positioning = st.text_input("Positioning")
        sliding_tackle = st.text_input("Sliding Tackle")

    with col6:
        dribbling = st.text_input("Dribbling")
        sprint_speed = st.text_input("Sprint Speed")
        stamina = st.text_input("Stamina")
        vision = st.text_input("Vision")
        goalkeeper_diving = st.text_input("GK Diving")

    st.text("")
    if(st.button("Where can I play this player?")):
        wr_map = {"Low":0,"Medium":1,"High":2}
        awr = wr_map[attacking_work_rate]
        dwr = wr_map[defensive_work_rate]

        input_data = [awr, dwr, total_pace, total_shooting, total_passing, total_dribbling, total_defending,
                      total_physicality, crossing, finishing, heading_accuracy, short_passing, volleys, dribbling,
                      curve, fk_accuracy, long_passing, ball_control, accelaration, sprint_speed, agility,
                      reactions, balance, shot_power, jumping, stamina, strength, long_shots, aggression, 
                      interceptions, positioning, vision, penalties, composure, marking, standing_tackle, 
                      sliding_tackle, goalkeeper_diving, goalkeeper_handling, goalkeeper_kicking, 
                      goalkeeper_positioning, goalkeeper_reflexes]
        input_array = np.array([input_data])
        input_array = input_array.astype(int)

        st.divider()
        pos = pp.predict(input_array)
        st.markdown("This player can display their best potential as a **"+pos+"** on the field")
        st.subheader("Comparison of attributes with Positional Average")
        if pos == "Goalkeeper":
            radar_slice = [goalkeeper_diving, goalkeeper_handling, goalkeeper_kicking, 
                      goalkeeper_positioning, goalkeeper_reflexes, total_physicality]
        else:
            radar_slice = [total_pace, total_shooting, total_passing, total_dribbling, total_defending,
                      total_physicality]
        fig = pp.plot_comparison_radar(pos,radar_slice)
        st.plotly_chart(fig,use_container_width=True)
        
if option == "Upload csv":
    with open("input_attributes_template.csv","rb") as file:
        btn = st.download_button(
            label = "Download Template",
            data = file,
            file_name = "input_attributes_template.csv",
            mime = "text/csv")
    st.markdown("Download the Template using the button above and fill in the values accordingly and Upload it as csv below!")
    uploaded_file = st.file_uploader("Choose a File")
    if uploaded_file is not None:
        input_df = pd.read_csv(uploaded_file)
        st.write(input_df)
        wr_map = {"Low":0,"Medium":1,"High":2}
        input_df["Attacking Work Rate"] = input_df["Attacking Work Rate"].map(wr_map)
        input_df["Defensive Work Rate"] = input_df["Defensive Work Rate"].map(wr_map)
        
        output = {"Name":list(),"Predicted Position":list()}
        for i in range(len(input_df)):
            output["Name"].append(input_df.iloc[i,0])
            ip = input_df.iloc[i,1:]
            output["Predicted Position"].append(pp.predict([ip]))
        output_df = pd.DataFrame(output)
        st.table(output_df)
        merged_df = pd.merge(input_df,output_df,on=["Name"])
        plots = pp.plot_comparison_radar_dataframe(merged_df)
        for i in plots:
            st.plotly_chart(i,use_container_width=False)