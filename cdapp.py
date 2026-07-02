import streamlit as st
import numpy as np
from PIL import Image
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image

st.set_page_config(page_title="Cat vs Dog Prediction", page_icon="🐾", layout="centered")

st.title("🐱🐶 Cat vs Dog Image Prediction")
st.write("Upload an image and the CNN model will predict whether it is a cat or dog.")

@st.cache_resource
def load_cnn_model():
    return load_model("cat_dog_cnn.h5")

model = load_cnn_model()

uploaded_file = st.file_uploader(
    "Upload Cat or Dog Image",
    type=["jpg", "jpeg", "png", "webp"]
)

if uploaded_file is not None:
    img = Image.open(uploaded_file).convert("RGB")
    st.image(img, caption="Uploaded Image", use_container_width=True)

    img_resized = img.resize((128, 128))
    img_array = image.img_to_array(img_resized)
    img_array = img_array / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    prediction = model.predict(img_array)[0][0]

    if prediction > 0.5:
        result = "Dog 🐶"
        confidence = prediction * 100
    else:
        result = "Cat 🐱"
        confidence = (1 - prediction) * 100

    st.success(f"Prediction: {result}")
    st.info(f"Confidence: {confidence:.2f}%")
    st.write(f"Prediction Score: `{prediction:.4f}`")