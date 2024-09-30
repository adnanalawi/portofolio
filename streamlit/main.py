from cv import cv
from portfolio import portfolio
from dashboard import dashboard
from addition import addition
from sidebar import sidebar    
from logit import prediksi

# Panggil sidebar menu dari file terpisah
selected_option = sidebar()

# Logika untuk setiap pilihan menu
if selected_option == "Curriculum Vitae":
    cv()
elif selected_option == "Portofolio":
    portfolio()
elif selected_option == "Addition":
    prediksi()
else:
    dashboard()
    
