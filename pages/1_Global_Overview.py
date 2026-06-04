import streamlit as st
import pandas as pd
import plotly.express as px

st.title("🌍 Global Aquaculture Overview")

df = pd.read_csv("data/raw/Aquaculture_Quantity.csv")

# KPIs
total_production = df["VALUE"].sum()
countries = df["COUNTRY.UN_CODE"].nunique()
species = df["SPECIES.ALPHA_3_CODE"].nunique()

latest_year = df["PERIOD"].max()
previous_year = latest_year - 1

latest_value = (
    df[df["PERIOD"] == latest_year]["VALUE"]
    .sum()
)

previous_value = (
    df[df["PERIOD"] == previous_year]["VALUE"]
    .sum()
)

growth = (
    (latest_value - previous_value)
    / previous_value
) * 100

c1, c2, c3, c4 = st.columns(4)

latest_production = (
    df[df["PERIOD"] == latest_year]["VALUE"]
    .sum()
)

c1.metric(
    "2023 Production",
    f"{latest_production/1_000_000:.1f} M tonnes"
)
c2.metric("Countries", countries)
c3.metric("Species", species)
c4.metric("Annual Growth %",f"{growth:.2f}%")

st.divider()

# Production Trend
trend = (
    df.groupby("PERIOD")["VALUE"]
    .sum()
    .reset_index()
)

fig = px.line(
    trend,
    x="PERIOD",
    y="VALUE",
    title="Global Production Trend"
)

st.plotly_chart(fig, use_container_width=True)

st.success(
    f"Global aquaculture production reached "
    f"{latest_value/1_000_000:.1f} million tonnes in {latest_year}, "
    f"growing {growth:.2f}% compared to {previous_year}."
)

from utils.mappings import (
    load_country_mapping,
    load_species_mapping
)

country_map = load_country_mapping()
species_map = load_species_mapping()


top_countries = (
    df[df["PERIOD"] == latest_year]
    .groupby("COUNTRY.UN_CODE")["VALUE"]
    .sum()
    .reset_index()
    .sort_values("VALUE", ascending=False)
    .head(10)
)

top_countries["Country"] = (
    top_countries["COUNTRY.UN_CODE"]
    .map(country_map)
)

fig2 = px.bar(
    top_countries,
    x="Country",
    y="VALUE",
    title=f"Top 10 Aquaculture Countries ({latest_year})"
)

st.plotly_chart(fig2, use_container_width=True)


top_species = (
    df[df["PERIOD"] == latest_year]
    .groupby("SPECIES.ALPHA_3_CODE")["VALUE"]
    .sum()
    .reset_index()
    .sort_values("VALUE", ascending=False)
    .head(10)
)

top_species["Species"] = (
    top_species["SPECIES.ALPHA_3_CODE"]
    .map(species_map)
)

fig3 = px.bar(
    top_species,
    x="Species",
    y="VALUE",
    title=f"Top 10 Aquaculture Species ({latest_year})"
)

st.plotly_chart(fig3, use_container_width=True)

