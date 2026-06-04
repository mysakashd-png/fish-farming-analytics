import streamlit as st
import pandas as pd
import plotly.express as px

from utils.mappings import (
    load_species_mapping,
    load_country_mapping
)

# -----------------------------
# Load Data
# -----------------------------
df = pd.read_csv(
    "data/raw/Aquaculture_Quantity.csv"
)

species_map = load_species_mapping()
country_map = load_country_mapping()

st.title("🐟 Species Analysis")

# -----------------------------
# Species Dropdown
# -----------------------------
species_list = sorted(
    df["SPECIES.ALPHA_3_CODE"]
    .dropna()
    .astype(str)
    .unique()
)

selected_species = st.selectbox(
    "Select Species",
    species_list,
    format_func=lambda x: str(
        species_map.get(x, x)
    )
)

# -----------------------------
# Filter Data
# -----------------------------
species_df = df[
    df["SPECIES.ALPHA_3_CODE"]
    .astype(str)
    == selected_species
]

# -----------------------------
# Production Trend
# -----------------------------
trend = (
    species_df.groupby("PERIOD")["VALUE"]
    .sum()
    .reset_index()
)

species_name = species_map.get(
    selected_species,
    selected_species
)

fig = px.line(
    trend,
    x="PERIOD",
    y="VALUE",
    title=f"{species_name} Production Trend"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# -----------------------------
# Top Producing Countries
# -----------------------------
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

country_data["Country"] = (
    country_data["COUNTRY.UN_CODE"]
    .map(country_map)
)

fig2 = px.bar(
    country_data,
    x="Country",
    y="VALUE",
    title=f"Top Countries Producing {species_name}"
)

st.plotly_chart(
    fig2,
    use_container_width=True
)
