import streamlit as st
import pandas as pd

st.set_page_config(page_title="N-Number History", page_icon="✈️")

st.title("✈️ US Aircraft Historical Search")
st.write("Enter an N-Number to see current and previous registrations.")

@st.cache_data
def load_data():
    # In a production app, you would point this to a URL or a SQL database
    try:
        df = pd.read_csv('aircraft_data.csv', low_memory=False)
        return df
    except FileNotFoundError:
        return None

data = load_data()

if data is None:
    st.warning("Data file not found. Please upload 'aircraft_data.csv' to your GitHub repo.")
else:
    search = st.text_input("Tail Number (e.g., 737PW)").upper().strip()
    if search:
        results = data[data['N-NUMBER'] == search]
        if not results.empty:
            st.dataframe(results)
        else:
            st.error("No historical records found.")
