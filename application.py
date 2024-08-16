import streamlit as st
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np

# Load your trained model
model = load_model('model_vgg16_01.h5')


# Define the predict_image function
def predict_image(model, img_path, class_names=['Fake', 'Real']):
    img = image.load_img(img_path, target_size=(224, 224))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array /= 255.0

    prediction = model.predict(img_array)
    probability = prediction[0][0]
    predicted_class = class_names[int(np.round(probability))]
    confidence = abs(probability - 0.5) * 2 * 100  # Confidence calculation

    return predicted_class, confidence

# Streamlit UI
st.title('Real vs Fake Face Classification')
st.markdown('<p style="font-size:16px;">Upload an image to classify it as real or fake.</p>', unsafe_allow_html=True)

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    st.image(uploaded_file, caption='Uploaded Image.', width=250)

    with open("temp.jpg", "wb") as f:
        f.write(uploaded_file.getbuffer())

    predicted_class, confidence = predict_image(model, "temp.jpg")

    st.markdown(f'<p style="font-size:16px;">Predicted Class: <strong>{predicted_class}</strong></p>',
                unsafe_allow_html=True)
    st.markdown(
        f'<p style="font-size:16px;">Confidence: <strong>{confidence:.2f}%</strong></p>',
        unsafe_allow_html=True)
