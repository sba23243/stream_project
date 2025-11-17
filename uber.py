import streamlit as st
import pandas as pd
import numpy as np

st.title("Uber Pickups in NYC")

DATA_URL = ('https://s3-us-west-2.amazonaws.com/'
         'streamlit-demo-data/uber-raw-data-sep14.csv.gz')

DATE_COLUMN = "date/time"

def load_data(nrows):
    uber_df = pd.read_csv(DATA_URL, nrows=nrows)
    lowercase = lambda x:str(x).lower()
    uber_df.rename(lowercase, axis="columns", inplace=True)
    uber_df[DATE_COLUMN] = pd.to_datetime(uber_df[DATE_COLUMN])
    return uber_df


    data_load_state = st.text("Loading Data...")
    uber_df = load_data(10000)
    data_load_state = st.text("Loading Data......Done!")