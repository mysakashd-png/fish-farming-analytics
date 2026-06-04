# app.py

import streamlit as st

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="Fish Farming Analytics Dashboard",
    page_icon="🐟",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -----------------------------
# Custom CSS
# -----------------------------
st.markdown("""
<style>
.main-header {
    font-size: 42px;
    font-weight: bold;
    color: #1E88E5;
}
.sub-header {
    font-size: 20px;
    color: #555;
}
</style>
""", unsafe_allow_html=True)

# -----------------------------
# Dashboard Header
# -----------------------------
st.markdown(
    '<p class="main-header">🐟 Fish Farming Analytics Dashboard</p>',
    unsafe_allow_html=True
)

st.markdown(
    '<p class="sub-header">FAO Global Aquaculture Production Analysis (1950–2023)</p>',
    unsafe_allow_html=True
)

# -----------------------------
# Sidebar
# -----------------------------
st.sidebar.title("Navigation")
st.sidebar.success(
    "Select a page from the sidebar."
)

# -----------------------------
# Home Page Content
# -----------------------------
col1, col2 = st.columns([2, 1])

with col1:
    st.markdown("## Welcome")
    
    st.write("""
    This dashboard helps analyze global aquaculture production
    using FAO datasets.

    ### Available Modules

    ✅ Global Overview

    ✅ Country Analysis

    ✅ Species Analysis

    ✅ Profitability Analysis

    ✅ Growth Opportunities

    ✅ Karnataka Fish Farming Advisor (Coming Soon)
    """)

with col2:
    st.image(
        "assets/fao_map.jpg",
        use_container_width=True
    )

# -----------------------------
# Project Goals
# -----------------------------
st.markdown("---")

st.markdown("## 🎯 Project Goals")

st.write("""
- Analyze global fish production trends
- Compare countries and species
- Identify profitable fish species
- Discover growth opportunities
- Support fish farming decisions in Karnataka
""")

# -----------------------------
# Footer
# -----------------------------
st.markdown("---")
st.caption("Built with Streamlit, Pandas, Plotly and FAO Aquaculture Dataset")
