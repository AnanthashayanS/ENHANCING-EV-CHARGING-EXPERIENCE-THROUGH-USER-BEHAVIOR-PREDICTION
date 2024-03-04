'''from google.oauth2.service_account import Credentials
import gspread

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

# Print the data
for row in data:
    print(row[0])

# Clear all values from the worksheet
worksheet.clear()

#print("All values cleared from the worksheet.")'''

'''	
import streamlit as st
import pandas as pd
import joblib
from datetime import datetime
from google.oauth2.service_account import Credentials
import gspread

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

# Load the saved model
loaded_model = joblib.load('model/random_forest_model.pkl')

def main():
    st.title('Garage Prediction App')
    st.write('This app predicts the Garage ID based on current system time.')
    
    # Print the data from Google Sheets
    st.write("Garage in use:")
    for row in data:
        st.write(row[0])

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
        if prob != 0 and displayed_count < 5:
            st.write(f"Predicted Garage ID: {label}, Probability: {prob}")
            displayed_count += 1

if __name__ == '__main__':
    main()
'''
'''
import streamlit as st
import pandas as pd
import joblib
from datetime import datetime
from google.oauth2.service_account import Credentials
import gspread

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

# Load the saved model
loaded_model = joblib.load('model/random_forest_model.pkl')

def main():
    st.title('Garage Prediction App')
    st.write('This app predicts the Garage ID based on current system time.')

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
        if prob != 0 and displayed_count < 5:
            st.write(f"Predicted Garage ID: {label}, Probability: {prob}")
            displayed_count += 1

    # Display data from Google Sheets
    st.title('Garage Status from Google Sheets')
    for row in data:
        st.write(f"Garage ID: {row[0]}, Status: {'In Use' if row[1] == '1' else 'Not In Use'}")

if __name__ == '__main__':
    main()
'''
'''import streamlit as st
import pandas as pd
import joblib
from datetime import datetime

# Load the saved model
loaded_model = joblib.load('model/random_forest_model.pkl')

def main():
    st.title('Garage Prediction App')
    st.write('This app predicts the Garage ID based on current system time.')

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
        if prob == 0 and displayed_count < 5:
            st.write(f"Predicted Garage ID: {label} is Free now")
            displayed_count += 1

if __name__ == '__main__':
    main()
'''	