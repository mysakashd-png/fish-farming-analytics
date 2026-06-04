import pandas as pd
import streamlit as st


@st.cache_data
def load_quantity_data():
    return pd.read_csv(
        "data/raw/Aquaculture_Quantity.csv"
    )


@st.cache_data
def load_value_data():
    return pd.read_csv(
        "data/raw/Aquaculture_Value.csv"
    )
