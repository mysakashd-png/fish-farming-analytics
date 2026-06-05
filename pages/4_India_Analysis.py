import streamlit as st
import pandas as pd
import plotly.express as px

from utils.mappings import (
    load_country_mapping,
    load_species_mapping
)

st.title("🇮🇳 India Aquaculture Analysis")

# -----------------------------
# Load Data
# -----------------------------
df = pd.read_csv(
    "data/raw/Aquaculture_Quantity.csv"
)

country_map = load_country_mapping()
species_map = load_species_mapping()

# -----------------------------
# Find India Code
# -----------------------------
india_code = None

for code, name in country_map.items():
    if str(name).lower() == "india":
        india_code = code
        break

if india_code is None:
    st.error("India not found in country mapping.")
    st.stop()

# -----------------------------
# Filter India Data
# -----------------------------
india_df = df[
    df["COUNTRY.UN_CODE"] == india_code
]

# -----------------------------
# KPIs
# -----------------------------
latest_year = india_df["PERIOD"].max()
previous_year = latest_year - 1

latest_value = (
    india_df[india_df["PERIOD"] == latest_year]["VALUE"]
    .sum()
)

previous_value = (
    india_df[india_df["PERIOD"] == previous_year]["VALUE"]
    .sum()
)

growth = (
    (latest_value - previous_value)
    / previous_value
) * 100

global_latest = (
    df[df["PERIOD"] == latest_year]["VALUE"]
    .sum()
)

india_share = (
    latest_value / global_latest
) * 100

c1, c2, c3 = st.columns(3)

c1.metric(
    f"{latest_year} Production",
    f"{latest_value/1_000_000:.2f} M tonnes"
)

c2.metric(
    "Growth Rate",
    f"{growth:.2f}%"
)

c3.metric(
    "Global Share",
    f"{india_share:.2f}%"
)

st.divider()

# -----------------------------
# India Production Trend
# -----------------------------
trend = (
    india_df.groupby("PERIOD")["VALUE"]
    .sum()
    .reset_index()
)

fig = px.line(
    trend,
    x="PERIOD",
    y="VALUE",
    title="India Aquaculture Production Trend"
)

fig.update_layout(height=500)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.success(
    f"India produced {latest_value/1_000_000:.2f} million tonnes in {latest_year}, "
    f"representing {india_share:.2f}% of global aquaculture production."
)

# -----------------------------
# Top Species in India
# -----------------------------
st.subheader("🐟 Top Species in India")

top_species = (
    india_df[india_df["PERIOD"] == latest_year]
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

fig2 = px.bar(
    top_species.sort_values("VALUE"),
    x="VALUE",
    y="Species",
    orientation="h",
    title=f"Top Species Produced in India ({latest_year})"
)

fig2.update_layout(height=600)

st.plotly_chart(
    fig2,
    use_container_width=True
)

top_species_name = top_species.iloc[0]["Species"]
top_species_value = top_species.iloc[0]["VALUE"]

st.info(
    f"{top_species_name} is the leading aquaculture species in India "
    f"with approximately {top_species_value/1_000_000:.2f} million tonnes production."
)

# -----------------------------
# India's Rank Globally
# -----------------------------
st.subheader("🌍 India's Position Globally")

country_rank = (
    df[df["PERIOD"] == latest_year]
    .groupby("COUNTRY.UN_CODE")["VALUE"]
    .sum()
    .reset_index()
    .sort_values("VALUE", ascending=False)
)

country_rank["Country"] = (
    country_rank["COUNTRY.UN_CODE"]
    .map(country_map)
)

india_rank = (
    country_rank.reset_index()
    .query("Country == 'India'")
    .index[0] + 1
)

st.metric(
    "Global Rank",
    f"#{india_rank}"
)

st.dataframe(
    country_rank.head(10),
    use_container_width=True
)
