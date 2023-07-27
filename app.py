import streamlit as st
import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing.image import load_img, img_to_array
from tensorflow.keras.models import load_model

# Load the pre-trained model
model = load_model('model.h5')

# Function to preprocess the image
def preprocess_image(image_path):
    img = load_img(image_path, target_size=(64, 64))
    img = img_to_array(img)
    img = img / 255.0  # Normalize pixel values to [0, 1]
    return img

# Function to make prediction
def predict_mask(image):
    img = preprocess_image(image)
    img = np.expand_dims(img, axis=0)
    prediction = model.predict(img)
    accuracy = round(prediction[0][0] * 100, 2)
    if prediction[0][0] >= 0.5:
        return "The image below is with mask (Accuracy: {}%)".format(accuracy)
    else:
        return "The image below is without mask (Accuracy: {}%)".format(accuracy)

def main():
    st.title("Face Mask Detection")
    st.write("Upload an image to check if the person is wearing a mask.")
    st.markdown("---")

    # File uploader for user to upload an image
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        # Display the uploaded image
        image = load_img(uploaded_file)
        st.image(image, caption="Uploaded Image.", use_column_width=True)

        # Make prediction
        prediction = predict_mask(uploaded_file)

        # Display prediction with colorful text
        st.markdown("---")
        if "with mask" in prediction:
            st.markdown(f"<p style='color:green; font-size: 24px;'>{prediction}</p>", unsafe_allow_html=True)
        else:
            st.markdown(f"<p style='color:red; font-size: 24px;'>{prediction}</p>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()