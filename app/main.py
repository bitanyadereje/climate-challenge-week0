import streamlit as st
from utils import get_climate_data, plot_regional_trends

st.set_page_config(
    page_title="EthioClimate Analytics | COP32", 
    page_icon="🌍", 
    layout="wide"
)

st.sidebar.image("https://streamlit.io/images/brand/streamlit-mark-color.png", width=50)
st.sidebar.header("Decision Support Filters")

selected_countries = st.sidebar.multiselect(
    "Select Nations", 
    options=["Ethiopia", "Kenya", "Sudan", "Tanzania", "Nigeria"],
    default=["Ethiopia", "Kenya"]
)

selected_var = st.sidebar.selectbox(
    "Climate Metric", 
    options=["T2M", "PRECTOTCORR", "RH2M"],
    format_func=lambda x: {"T2M": "Temperature", "PRECTOTCORR": "Precipitation", "RH2M": "Humidity"}[x]
)

year_range = st.sidebar.slider(
    "Analysis Period", 
    min_value=2015, 
    max_value=2026, 
    value=(2015, 2026)
)

st.title("🌍 COP32 Climate Decision Support Portal")
st.markdown("""
    *Developed by **EthioClimate Analytics** for the Ethiopian Ministry of Planning and Development.*
    This portal provides evidence-backed insights to support Africa's climate policy narrative ahead of the 2027 summit.
""")

st.divider()

if not selected_countries:
    st.warning("⚠️ Please select at least one country in the sidebar to visualize the data.")
else:
    with st.spinner("Analyzing regional datasets..."):
        df = get_climate_data(selected_countries, year_range, selected_var)
        
        col1, col2, col3 = st.columns(3)
        col1.metric("Selected Countries", len(selected_countries))
        col2.metric("Start Year", year_range[0])
        col3.metric("End Year", year_range[1])
        
        fig = plot_regional_trends(df, selected_var)
        st.plotly_chart(fig, use_container_width=True)
        
        # Data Preview Table (Optional but professional)
        with st.expander("View Raw Data Table"):
            st.dataframe(df.head(100), use_container_width=True)

st.sidebar.info("Framework Layer: **EDA (What is changing?)**")