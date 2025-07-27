import streamlit as st
import numpy as np
import joblib

# Cargar modelo y scaler
model = joblib.load("glass_model.pkl")

# Si usaste scaler, descomenta esto:
# scaler = joblib.load("scaler.pkl")

# Título
st.title("Glass Type Prediction App")
st.markdown("Enter the chemical composition of the glass sample to predict its type.")

# Entrada de características
RI = st.number_input("Refractive Index (RI)", 1.4, 1.6, step=0.001, format="%.4f")
Na = st.number_input("Sodium (Na)", 0.0, 20.0, step=0.1)
Mg = st.number_input("Magnesium (Mg)", 0.0, 5.0, step=0.1)
Al = st.number_input("Aluminum (Al)", 0.0, 5.0, step=0.1)
Si = st.number_input("Silicon (Si)", 60.0, 75.0, step=0.1)
K  = st.number_input("Potassium (K)", 0.0, 10.0, step=0.1)
Ca = st.number_input("Calcium (Ca)", 0.0, 20.0, step=0.1)
Ba = st.number_input("Barium (Ba)", 0.0, 5.0, step=0.1)
Fe = st.number_input("Iron (Fe)", 0.0, 2.0, step=0.01)

# Botón de predicción
if st.button("Predict Glass Type"):
    input_data = np.array([[RI, Na, Mg, Al, Si, K, Ca, Ba, Fe]])
    
    # Si usaste scaler, descomenta esto:
    # input_data = scaler.transform(input_data)

    prediction = model.predict(input_data)[0]

    # Etiquetas según dataset
    class_map = {
        1: "Building Windows (Float processed)",
        2: "Building Windows (Non Float)",
        3: "Vehicle Windows",
        5: "Containers",
        6: "Tableware",
        7: "Headlamps"
    }

    label = class_map.get(prediction, "Unknown Type")
    
    st.subheader(f"🧪 Predicted Glass Type: {label} (class {prediction})")
