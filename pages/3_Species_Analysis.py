import streamlit as st
import pandas as pd
import plotly.express as px

st.title("🐟 Species Analysis")

df = pd.read_csv(
    "data/raw/Aquaculture_Quantity.csv"
)

from utils.mappings import load_species_mapping

species_map = load_species_mapping()

species_list = sorted(
    df["SPECIES.ALPHA_3_CODE"].unique()
)

selected_species = st.selectbox(
    "Select Species",
    species_list,
    format_func=lambda x:
        species_map.get(x, x)
)

selected_species = st.selectbox(
    "Select Species",
    species_list
)

species_df = df[
    df["SPECIES.ALPHA_3_CODE"]
    == selected_species
]

trend = (
    species_df.groupby("PERIOD")["VALUE"]
    .sum()
    .reset_index()
)

fig = px.line(
    trend,
    x="PERIOD",
    y="VALUE",
    title=f"{selected_species} Production Trend"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

country_data = (
    species_df.groupby(
        "COUNTRY.UN_CODE"
    )["VALUE"]
    .sum()
    .reset_index()
    .sort_values(
        "VALUE",
        ascending=False
    )
    .head(10)
)

fig2 = px.bar(
    country_data,
    x="COUNTRY.UN_CODE",
    y="VALUE",
    title="Top Producing Countries"
)

st.plotly_chart(
    fig2,
    use_container_width=True
)
