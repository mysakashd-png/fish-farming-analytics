def total_production(df):
    return df["VALUE"].sum()


def total_countries(df):
    return df["COUNTRY.UN_CODE"].nunique()


def total_species(df):
    return df["SPECIES.ALPHA_3_CODE"].nunique()


def yearly_production(df):
    return (
        df.groupby("PERIOD")["VALUE"]
        .sum()
        .reset_index()
    )
