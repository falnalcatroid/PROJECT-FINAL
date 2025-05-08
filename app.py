# app.py  ───────────────────────────────────────────
import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path


# ---------- 1. Load data ----------

df = pd.read_csv('vehicles_us.csv')

CURRENT_YEAR = 2025
df["vehicle_age"] = CURRENT_YEAR - df["model_year"]
df = df.dropna(subset=["vehicle_age"])   # drop ads with no model_year

# ---------- 2. Page header ----------
st.header("Used‑Car Listings Explorer 🚗")
st.write(
    """
    Explore ~50 k scraped vehicle ads.  
    Toggle below to switch between **vehicle‑age distribution**
    and **model‑year listing counts**.
    """
)

# ---------- 3. Checkbox controls which plot we show ----------
show_age_hist = st.checkbox(
    "Show Vehicle‑Age Histogram",
    value=True,
)

# ---------- 4. Plot #1  – histogram or bar chart ----------
if show_age_hist:
    fig = px.histogram(
        df,
        x="vehicle_age",
        nbins=40,
        title="Distribution of Vehicle Age",
        labels={"vehicle_age": "Age (years)"},
    )
else:
    year_counts = (
        df[df["model_year"].between(1980, CURRENT_YEAR)]
          .groupby("model_year")
          .size()
          .reset_index(name="count")
          .sort_values("model_year")
    )
    fig = px.scatter(
        year_counts,
        x="model_year",
        y="count",
        title="Number of Listings by Model Year (1980–2025)",
        labels={"model_year": "Model Year", "count": "Listings"},
    )

st.plotly_chart(fig, use_container_width=True)