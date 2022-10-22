import streamlit as st
import pandas as pd
import numpy as np

st.title('Will it Burn?')

DATE_COLUMN = 'firediscoverydatetime'

def load_data(nrows, filename):
    data = pd.read_csv(filename, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    print(data.columns)
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data

st.write('This web app shows the forecasts of fires in the state of California. The forecast is made using a Random Forest model using historical fire data from WFIGS and meteorolgoical data from ERA5.')

# Load 10,000 rows of data into the dataframe.
data = load_data(10000, 'dash.csv')

# Some number in the range 0-23
hour_to_filter = st.slider('Day', 1, 31, 1, step=1)
filtered_data = data[data[DATE_COLUMN].dt.day == hour_to_filter]

st.subheader('Fire predictions on Day %s' % hour_to_filter)
st.map(filtered_data)

# Load 10,000 rows of data into the dataframe.
data_all = load_data(10000, 'dash_all.csv')

st.subheader('All Fire Predictions')
st.map(data_all)


if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(data)


st.text('Developed by Simon Lechner, Ayush Prasad, Laurens Veltman')