import streamlit as st
import pandas as pd
import joblib
from datetime import datetime
from google.oauth2.service_account import Credentials
import gspread

st.set_page_config(layout="wide")

# Define the scope (permissions)
scope = [
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive'
]

# Path to your credentials JSON file
credentials = Credentials.from_service_account_file('jsonapi/rfid-415217-7bdeac6b4e7b.json', scopes=scope)

# Authorize the client
client = gspread.authorize(credentials)

# Open the spreadsheet
spreadsheet = client.open('RFID Logs')

# Select a specific worksheet
worksheet = spreadsheet.worksheet('Sheet1')

# Get all values from the worksheet
data = worksheet.get_all_values()

garage_id = []

for row in data:
    if not row:
        continue
    id = row[0]
    status = row[2]
    if len(row) < 3:
        continue
    if status == "Start":
        garage_id.append(id)
    elif status == "End":
        if id in garage_id:
            garage_id.remove(id)

# Load the saved model
loaded_model = joblib.load('model/random_forest_model.pkl')

def main():
    st.title('Garage Prediction')
    st.subheader('Garage ID prediction based on system time and live data')
    
    # Print the data from Google Sheets
    st.button("Garage Status")
    for row in garage_id:
        try:
            st.write(f"{row}, is in use !!!")
        except:
            st.write("Below Garage is empty now !!!")

    # Get the current system time
    current_time = datetime.now()

    # Prepare data for prediction
    prediction_data = pd.DataFrame({
        'Start_plugin': [current_time],
        'End_plugout': [current_time],
        'Hour': [current_time.hour],
        'DayOfWeek': [current_time.weekday()]  # Using weekday() to get day of the week
    })

    # Making predictions along with probabilities
    predicted_probs = loaded_model.predict_proba(prediction_data)[0]

    # Get the predicted labels
    predicted_labels = loaded_model.classes_

    # Counter to keep track of displayed predictions
    displayed_count = 0

    # Print predicted labels along with probabilities (show only top 5 non-zero probabilities)
    for label, prob in zip(predicted_labels, predicted_probs):
        if prob != 0 and displayed_count < 5 and label not in garage_id:
            st.write(f"Predicted Garage ID: {label}, Status: FREE now !!!")
            displayed_count += 1

if __name__ == '__main__':
    main()
