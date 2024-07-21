import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import altair as alt
import pandas as pd
import requests

#Endpoints
api_url = 'http://127.0.0.1:8000/api/person/'
jog_api_url = 'http://127.0.0.1:8000/api/jog/'
journalapi = 'http://127.0.0.1:8000/api/journal/'


#functions
def fetch_data(endpoint):
    response = requests.get(endpoint)
    data = response.json()
    return data


def send_data(place, distance, duration, difficulty):
    difficulty_value = "0" if difficulty == "Easy" else "1"
    data = {
        "place": place,
        "distance": distance,
        "duration": duration,
        "difficulty": difficulty_value,
    }
    response = requests.post(jog_api_url, json=data)
    return response

def log_journal(title, mood, entry):
    data = {
        "title": title,
        "mood": mood,
        "entry": entry
    }
    response = requests.post(journalapi, json=data)
    return response


st.title("Goal Tracker")
st.write('v0.0.1')

# Layout Customization
col1, col2 = st. columns(2)


with col1:
    st.header('Jogs')
    st.write('Log your jogs here.')

    place = st.text_input("Where did you run?")
    distance = st.slider("How far did you run? (km)", 0.01, 100.0, 0.01)
    duration = st.number_input("How long did you run?")
    difficulty = st.radio("Difficulty", ["Easy", "Hard"])

    if st.button("Log"):
        response = send_data(place, distance, distance, difficulty)
        if response.status_code == 201:
            st.success("good")

        else:
            st.error('error')
    
    data = fetch_data(jog_api_url)

    if data:
        df = pd.DataFrame(data)
        scatter_chart = alt.Chart(df).mark_circle().encode(
            x='distance',
            y='duration',
        )

    st.altair_chart(scatter_chart, use_container_width=True)

    st.dataframe(df)
with col2:
    st.header('Journal')
    st.write('Log your journal here')

    title = st.text_input('Entry Title')
    mood = st.text_input('How u feeling?')
    entry = st.text_area('Write about it.')

    if st.button("Log Journal"):
        response = log_journal(title, mood, entry)
        if response.status_code == 201:
            st.success("good")

        else:
            st.error('error')
    
    data = fetch_data(journalapi)
    df = pd.DataFrame(data)
    st.data_editor(df, num_rows="dynamic")
    if data:
        df = pd.DataFrame(data)
        scatter_chart = alt.Chart(df).mark_circle().encode(
            x='mood',
            y='date',
        )
    st.altair_chart(scatter_chart, use_container_width=True)
