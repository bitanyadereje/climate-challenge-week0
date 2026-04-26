import pandas as pd
import numpy as np
import plotly.express as px
import streamlit as st

@st.cache_data
def get_climate_data(countries, years, variable):
    """
    Simulates fetching NASA POWER data. 
    In Task 3, you will replace the dummy data with your real merged CSV.
    """
    dates = pd.date_range(start="2015-01-01", end="2026-03-31", freq="D")
    
    data_frames = []
    for country in countries:
        values = np.random.normal(loc=25, scale=5, size=len(dates))
        
        temp_df = pd.DataFrame({
            "date": dates,
            "country": country,
            variable: values
        })
        data_frames.append(temp_df)
    
    df = pd.concat(data_frames)
    
    mask = (df['date'].dt.year >= years[0]) & (df['date'].dt.year <= years[1])
    return df[mask]

def plot_regional_trends(df, variable):
    """Generates an interactive Plotly chart."""
    fig = px.line(
        df, 
        x="date", 
        y=variable, 
        color="country",
        title=f"Regional {variable} Analysis (2015-2026)",
        labels={variable: f"{variable} Value", "date": "Timeline"},
        template="plotly_white"
    )
    fig.update_layout(hovermode="x unified")
    return fig