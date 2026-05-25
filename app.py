import streamlit as st
import engine 
from datetime import datetime

st.set_page_config(page_title="Weather Quant 2026", layout="wide")
st.title("🌡️ Global Weather-Energy Quant Machine")
st.write(f"Current Analysis Date: **{datetime.now().strftime('%B %d, %Y')}**")

# Sidebar selection
region = st.sidebar.selectbox("Select Energy Hub", ["Houston (Texas)", "Chicago (Illinois)", "London (UK)"])

ticker_map = {
    "Houston (Texas)": "NRG",
    "Chicago (Illinois)": "EXC",
    "London (UK)": "NG.L"
}

selected_ticker = ticker_map[region]

if st.button("Run Live Analysis"):
    with st.spinner(f"Connecting to satellites for {region}..."):
        data, corr_score = engine.get_quant_data(selected_ticker, region)
        
        col1, col2 = st.columns([1, 3])
        
        with col1:
            st.metric("Correlation Score", f"{corr_score:.4f}")
            st.info(f"Analyzing {len(data)} days of market & weather alignment.")
            
        with col2:
            st.subheader(f"Max Temp vs. {selected_ticker} Returns")
            st.scatter_chart(data, x="Temp_Max", y="Daily_Return")
            
        st.write("### Data Integrity Check (Last 5 Trading Days)")
        st.dataframe(data.tail())