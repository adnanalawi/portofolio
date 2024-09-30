import streamlit as st
import pickle
import pandas as pd

def prediksi():
    with open('streamlit/pipeline.pkl', 'rb') as file:
        pipeline = pickle.load(file)

    st.markdown("""
    <style> .main > div {
        padding-left: 12rem;
        padding-right: 12rem;
        }
        </style> """, unsafe_allow_html=True)
    
    st.title("Logistic Regression Prediction")
    st.markdown("")

    st.markdown('''
                <div> 
                <div style='text-align: justify;'>
                <p style="font-family: monospace; font-size: 14px; ">
                <style>
                [data-testid="stMarkdownContainer"] ul{
                padding-left:15px;
                }
                </style>
                
                Model prediksi menggunakan algoritma Logistic Regression yang dilatih dengan menggunakan dataset
                [Bank Marketing](https://archive.ics.uci.edu/dataset/222/bank+marketing), bertujuan untuk memprediksi 
                apakah seorang klien akan berlangganan deposito bank berjangka berdasarkan beberapa informasi pribadi dan finansial.
                
                </p>
                </div>
                ''', unsafe_allow_html=True
        
        )
    
    # Membuat input_number kosong
    age = st.number_input("Masukkan umur:", min_value=0, max_value=80, value=None)
    balance = st.number_input("Jumlah Saldo Rekening (dollar):", min_value=0, max_value=100000, value=None)

    # Menambahkan elemen kosong pada selectbox
    job = st.selectbox("Pekerjaan (job):", 
                       ['', 'management', 'technician', 'entrepreneur', 'retired', 'admin.', 
                        'services', 'blue-collar', 'self-employed', 'unemployed', 'housemaid', 'student'])

    marital = st.selectbox("Status pernikahan (marital):", ['', 'single', 'married', 'divorced'])
    education = st.selectbox("Pendidikan (education):", ['', 'tertiary', 'secondary', 'primary'])
    housing = st.selectbox("Punya kredit rumah (housing):", ['', 'yes', 'no'])
    loan = st.selectbox("Punya pinjaman pribadi (loan):", ['', 'yes', 'no'])
    

    # Simpan input pengguna dalam format DataFrame
    input_data = pd.DataFrame({
        'age': [age],
        'balance': [balance],
        'job': [job],
        'marital': [marital],
        'education': [education],
        'housing': [housing],
        'loan': [loan] })
    
    
    # Buat tombol untuk memulai prediksi
    if st.button("Prediksi"):
        # Lakukan prediksi menggunakan pipeline yang telah dimuat
        prediction = pipeline.predict(input_data)

        # Tampilkan hasil prediksi
        if prediction[0] == 1:
            st.success("Hasil prediksi: Pelanggan akan berlangganan deposito.")
        else:
            st.error("Hasil prediksi: Pelanggan tidak akan berlangganan deposito.")
