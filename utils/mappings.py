import pandas as pd
import streamlit as st


@st.cache_data
def load_country_mapping():
    country = pd.read_csv(
        "data/raw/CL_FI_COUNTRY_GROUPS.csv",
        encoding="latin1"
    )

    return dict(
        zip(
            country["UN_Code"],
            country["Name_En"]
        )
    )


@st.cache_data
def load_species_mapping():
    species = pd.read_csv(
        "data/raw/CL_FI_SPECIES_GROUPS.csv",
        encoding="latin1"
    )

    return dict(
        zip(
            species["3A_Code"],
            species["Name_En"]
        )
    )
