import streamlit as st
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image as tsimage
import numpy as np
from PIL import Image

def classificar(img):
    img = img.resize((200, 200))
    x = tsimage.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = x / 255.0  # Normalizar los píxeles
    predicciones = modelo.predict(x)
    if predicciones[0][0] == 1:
        return "Es un Perro"
    else:
        return "Es un Gato"
    
st.set_page_config(page_title='🐈Cat&Dog Classifier🐕')
st.title('🐈Cat&Dog Classifier🐕')

archivo = st.file_uploader("Elige una imagen...", type=["jpg", "jpeg", "png"])

if archivo is not None:
    # Mostrar la imagen
    image = Image.open(archivo)
    st.image(image, caption='Imagen subida', use_column_width=True)

    imagen_cargada = True
    if imagen_cargada:
        modelo = load_model('model_keras_catdog.h5')
        
        # if 'clasificar' not in st.session_state:
        #     st.session_state.clasificar = True

        # if st.session_state.clasificar:
        if st.button("Classificar", key="boton_clasificar"):
            prediction = classificar(image)
            st.write(f"Predicción: {prediction}")
            st.session_state.clasificar = False
