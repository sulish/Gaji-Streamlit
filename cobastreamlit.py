import streamlit as st
import joblib
import numpy as np

#memuat model regresi linier yang sudh di simpan
lin_reg_loaded=joblib.load('lin_reg_model.joblib')

#judul aplikasi
st.title("Prediksi Gaji Berdasarkan Lama Bekerja")

#input tahun pengalaman kerja
years_experience = st.number_input("Masukkan jumlah tahun bekerja: ", min_value = 0.0,step = 0.1)

#prediksi gaji

if st.button("Prediksi gaji"):
    gaji = lin_reg_loaded.predict([[years_experience]])
    st.write(f"Gaji seorang setelah bekerja selama {years_experience} tahun adalah ${gaji[0]:,.2f}")