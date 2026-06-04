import streamlit as st
import pandas as pd
import plotly.express as px

st.title("🏳️ Country Analysis")

df = pd.read_csv("data/raw/Aquaculture_Quantity.csv")

country_list = sorted(
    df["COUNTRY.UN_CODE"].unique()
)

selected_country = st.selectbox(
    "Select Country Code",
    country_list
)

country_df = df[
    df["COUNTRY.UN_CODE"] == selected_country
]

trend = (
    country_df.groupby("PERIOD")["VALUE"]
    .sum()
    .reset_index()
)

fig = px.line(
    trend,
    x="PERIOD",
    y="VALUE",
    title=f"Country {selected_country} Production"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

species_data = (
    country_df.groupby(
        "SPECIES.ALPHA_3_CODE"
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
    species_data,
    x="SPECIES.ALPHA_3_CODE",
    y="VALUE",
    title="Top Species"
)

st.plotly_chart(
    fig2,
    use_container_width=True
)
