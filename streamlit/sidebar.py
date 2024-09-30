import streamlit as st 
from streamlit_option_menu import option_menu


def sidebar():
    st.set_page_config(layout="wide")

    # Detect theme and dynamically apply styles
    is_dark_mode = st.get_option("theme.base") == "dark"
    text_color = "white" if is_dark_mode else "black"
    
    with st.sidebar:
        select = option_menu(
            menu_title="",  # Judul menu
            options=["Curriculum Vitae", "Portofolio", "Dashboard", "Addition"],  # Opsi menu
            icons=["file-earmark-text", "journal", "bar-chart-line", "diagram-3"],  # Ikon untuk setiap opsi
            default_index=0,  # Indeks default yang dipilih
            styles={
                "container": {"padding": "5px", "background-color": "#f0f2f6"},  # Warna background sidebar
                "icon": {"color": "blue", "font-size": "20px"},  # Warna dan ukuran ikon
                "nav-link": { 
                    "font-size": "16px", 
                    "text-align": "left", 
                    "margin": "0px", 
                    "--hover-color": "#eeee",
                    "color": text_color  # Dynamic text color based on theme
                },  
                "nav-link-selected": {"background-color": "#88cdf6", "color": "white"},  # Warna saat opsi dipilih
            }
        )
    
    return select
