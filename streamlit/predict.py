import streamlit as st 
import pickle
from streamlit_drawable_canvas import st_canvas 
from tensorflow.keras.models import load_model
from PIL import Image, ImageOps
import numpy as np
from scipy.ndimage import center_of_mass

# 1. Muat model MNIST yang sudah disimpan
model = load_model('mnist_model.keras')

# 2. Muat metadata (opsional, jika digunakan)
with open('model_metadata.pkl', 'rb') as f:
    metadata = pickle.load(f)

# Fungsi untuk menempatkan digit di tengah
def center_image(image):
    cy, cx = center_of_mass(image)  # Cari pusat massa dari digit
    shift_x = np.round(image.shape[1] / 2.0 - cx).astype(int)
    shift_y = np.round(image.shape[0] / 2.0 - cy).astype(int)
    return np.roll(np.roll(image, shift_y, axis=0), shift_x, axis=1)

# Fungsi untuk memprediksi digit dari gambar
def predict_digit(image):
    image = ImageOps.grayscale(image)  # Ubah gambar ke grayscale
    image = image.resize((28, 28))     # Resize gambar menjadi 28x28
    image = np.array(image)            # Konversi ke array numpy
    image = image / 255.0              # Normalisasi nilai piksel
    image = (image > 0.5).astype(np.float32)  # Terapkan thresholding
    image = center_image(image)        # Pusatkan digit
    image = image.reshape(1, 28, 28, 1)   # Sesuaikan dengan input model
    prediction = model.predict(image)  # Prediksi label digit
    return np.argmax(prediction, axis=1)[0]



# Membuat kanvas menggambar
st.write("Draw a digit below:")
canvas_result = st_canvas(
    stroke_width=10, 
    stroke_color="black", 
    background_color="white",
    height=300, 
    width=300, 
    drawing_mode="freedraw", 
    key="canvas"
)

# Jika gambar telah dibuat di kanvas
if canvas_result.image_data is not None:
    # Konversi gambar dari kanvas ke format PIL
    img = Image.fromarray(np.uint8(canvas_result.image_data))

    # Tampilkan gambar yang digambar oleh pengguna
    st.image(img, caption="Your drawn digit", width=150)

    # Prediksi digit dari gambar
    if st.button("Predict"):
        label = predict_digit(img)
        st.write(f"Predicted Digit: {label}")
