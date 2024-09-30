import streamlit as st
import pickle
import pandas as pd


def prediksi():
    with open('pipeline.pkl', 'rb') as file:
        pipeline = pickle.load(file)

 
    st.title("Logistic Regression Prediction")
    
    # Membuat input_number kosong
    age = st.number_input("Masukkan umur:", min_value=0, max_value=80, value=None)
    balance = st.number_input("Jumlah Saldo Rekening:", min_value=0, max_value=100000, value=None)

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