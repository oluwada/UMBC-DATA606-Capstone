import pickle
import pandas as pd
import streamlit as st

# Page config
st.set_page_config(page_title="Early Life Diet Predictor", page_icon="☀️💊🇩", layout="wide")

# Header
st.markdown("<h1 style='color:#758BF1;'>Early Life Diet Predictor (Mouse Model)</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='color:#FFFFFF;'>Use the sidebar to enter respiratory and exposure data</h3>", unsafe_allow_html=True)

# Load model
with open('best_model.pkl', 'rb') as f:
    loaded_model = pickle.load(f)

# ----------
# SIDEBAR
# ----------
st.sidebar.header("💨 Respiratory Metrics")

breathing_frequency = st.sidebar.number_input("Breathing Frequency", 1.0, 10.0, step=0.01)
tidal_volume = st.sidebar.number_input("Tidal Volume", 0.0, 1.0, step=0.0001)
inspiratory_time = st.sidebar.number_input("Inspiratory Time", 0.0, 0.7, step=0.001)
expiratory_time = st.sidebar.number_input("Expiratory Time", 0.0, 2.5, step=0.5)
penh = st.sidebar.number_input("Penh", 0.0, 3.0, step=0.01)

st.sidebar.header("🌪️ Environmental Exposure")
exposure = st.sidebar.selectbox("Exposure", ["Air", "Smog", "Unknown"])

predict = st.sidebar.button("Predict Early-life Diet")


#  CONTAINER
# -----------
result_box = st.container()

with result_box:
    st.markdown("### 🧪 Prediction Result")

    if predict:

        Exposure_Air = 1 if exposure == "Air" else 0
        Exposure_Smog = 1 if exposure == "Smog" else 0
        Exposure_Unknown = 1 if exposure == "Unknown" else 0

        features = [
            'Exposure_Air', 'Exposure_Smog', 'Exposure_Unknown',
            'Breathing Frequency', 'Tidal volume', 'Inspiratory Time',
            'Expiratory Time', 'Penh'
        ]

        data = pd.DataFrame([[
            Exposure_Air, Exposure_Smog, Exposure_Unknown,
            breathing_frequency, tidal_volume, inspiratory_time,
            expiratory_time, penh
        ]], columns=features)

        prediction = loaded_model.predict(data)[0]
        probability = loaded_model.predict_proba(data).max()

        if prediction == 0:
            st.success("Early-life **Normal Diet (ND)**", icon="✅")
        else:
            st.error("Early-life **Vitamin-D Deficient Diet (VDD)**", icon="🚩")

        st.metric("Model Confidence", f"{probability:.2f}")

        st.caption(
            "⚠️ This prediction is tentative. The model treats each observation as "
            "independent, but the data are longitudinal — interpret with caution."
        )

    else:
        st.info("Enter values in the sidebar to begin.")

