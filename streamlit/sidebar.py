import streamlit as st 
from streamlit_option_menu import option_menu


# Set layout
st.set_page_config(layout="wide")

# Detect theme and dynamically apply styles
is_dark_mode = st.get_option("theme.base") == "dark"

# Set background color based on the theme
background_color = "#333333" if is_dark_mode else "#f0f2f6"
text_color = "white" if is_dark_mode else "black"
hover_color = "#555555" if is_dark_mode else "#eeeeee"

# Sidebar menu
with st.sidebar:
    select = option_menu(
        menu_title="",  # Judul menu
        options=["Curriculum Vitae", "Portofolio", "Dashboard", "Addition"],  # Opsi menu
        icons=["file-earmark-text", "journal", "bar-chart-line", "diagram-3"],  # Ikon untuk setiap opsi
        default_index=0,  # Indeks default yang dipilih
        styles={
            "container": {"padding": "5px", "background-color": background_color},  # Background sesuai tema
            "icon": {"color": "blue", "font-size": "20px"},  # Warna dan ukuran ikon
            "nav-link": { 
                "font-size": "16px", 
                "text-align": "left", 
                "margin": "0px", 
                "--hover-color": hover_color,  # Hover color sesuai tema
                "color": text_color  # Warna teks sesuai tema
            },  
            "nav-link-selected": {"background-color": "#88cdf6", "color": "white"},  # Warna saat opsi dipilih
        }
    )

# Apply custom background color using markdown and CSS for the main page
page_style = f"""
<style>
    .stApp {{
        background-color: {background_color};
    }}
</style>
"""
st.markdown(page_style, unsafe_allow_html=True)
