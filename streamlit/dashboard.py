import streamlit as st 
import streamlit.components.v1 as components


def dashboard():
    st.title("DASHBOARD")
    
    st.markdown("""
    <style> .main > div {
        padding-left: 5rem;
        padding-right: 4rem;
        padding-up: 5rem;
        padding-bottom: 5rem;
        }
        </style> """, unsafe_allow_html=True)
    
    components.html("""
    <iframe src="https://public.tableau.com/views/E-commerceDataAnalysis_17248145029050/Dashboard1?:showAppBanner=false&:showVizHome=no&:embed=true&:origin=viz_share_link " 
    width="100%" height="800" frameborder="0" allowfullscreen></iframe>""", height=800)