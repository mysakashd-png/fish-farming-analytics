import streamlit as st
import pandas as pd
import plotly.express as px

st.title("🌍 Global Aquaculture Overview")

df = pd.read_csv("data/raw/Aquaculture_Quantity.csv")

# KPIs
total_production = df["VALUE"].sum()
countries = df["COUNTRY.UN_CODE"].nunique()
species = df["SPECIES.ALPHA_3_CODE"].nunique()

c1, c2, c3 = st.columns(3)

c1.metric("Total Production", f"{total_production:,.0f}")
c2.metric("Countries", countries)
c3.metric("Species", species)

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

st.dataframe(trend.tail())
