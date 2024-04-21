# Player Position Prediction

## Overview
This project aims to predict the ideal playing position for soccer players based on their attributes. Leveraging machine learning techniques, it provides insights into optimizing player placement for peak performance.

## Project Structure
The repository is organized as follows:
- **1 - Data Preprocessing.ipynb**: Notebook for data preprocessing tasks.
- **2 - EDA & Metrics.ipynb**: Notebook for exploratory data analysis and metric evaluation.
- **3 - Model Building.ipynb**: Notebook for building and evaluating machine learning models.
- **Player Position Prediction Model.sav**: Saved Random Forest model used for prediction.
- **Positional Attribute Means.csv**: CSV file containing positional attribute means.
- **Positional Attributes P80.csv**: CSV file containing positional attribute 80th percentile values.
- **app.py**: Web application for deployment.
- **app2.py**: Web application for testing purposes.
- **input_attributes_template.csv**: Template CSV file for inputting player attributes.
- **key_attr_players.csv**: CSV file containing key attribute values for players.
- **players.csv**: CSV file containing player attributes data.
- **predict_position.py**: Python script for predicting player positions.
- **requirements.txt**: Text file listing project dependencies.


## Requirements

- Python 3
- Libraries listed in `requirements.txt`

## Instructions

1. Clone the repository:

```bash
git clone https://github.com/your-username/player-position-prediction.git
cd player-position-prediction
```
2. Install the required libraries
   ```bash
   pip install -r requirements.txt
   ```
3. Run the web application
   ```bash
   streamlit run app.py
   ```
## Usage
1. Input player attributes into the provided CSV template (`input_attributes_template.csv`).
2. Upload the filled CSV file to the web application.
3. Obtain predictions for the players' ideal positions based on their attributes.

## Future Scope
- Integrate real-time player monitoring with bio sensors.
- Collaborate with soccer academies for in-depth player analysis.
- Expand analysis to include head-to-head player comparisons.

