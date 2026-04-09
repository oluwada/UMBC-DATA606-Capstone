import pickle
import pandas as pd
import streamlit as st

# List of features
features =['Exposure_Air', 'Exposure_Smog', 'Exposure_Unknown', 'Breathing Frequency','Tidal volume','Inspiratory Time','Expiratory Time', 'Penh']
# Page configuration
st.set_page_config(page_title="Early Life Diet Predictor", page_icon="☀️💊🇩", layout="wide")
# App Customization 
st.markdown(
    """
    <style>
    .header {
        font-size: 36px;
        color: #758BF1; 
        font-weight: bold;
    }
    .subheader {
        font-size: 20px;
        color: #FFFFFF;
    }
    .stButton>button {
        background-color: #3f51b5;
        color: white;
        font-size:20px;
        border-radius: 5px;
        height: 40px;
        width: 150px;
        margin-top: 10px;
    }
    
    label {
        font-size: 18px;!important;
    }

    </style>
    """,
    unsafe_allow_html=True
)

# Header and subheader design 
st.markdown("<div class='header'>Early Life Diet Predictor(Mouse Model)</div>", unsafe_allow_html=True)
st.markdown("<div class='subheader'>Enter your details below to predict early life diet</div>", unsafe_allow_html=True)


# Load the pipeline from the file for prediction
with open('best_model.pkl', 'rb') as f:
    loaded_model = pickle.load(f)

# Form from streamlit
with st.form("diet_form"):

    # Respiratory Metrics
    st.markdown("## 💨Respiratory Metrics")
    breathing_metrics_1, breathing_metrics_2 = st.columns(2)
    # first column
    with breathing_metrics_1:
        breathing_frequency = st.number_input("Breathing Frequency", min_value=1.0, max_value=10.0, step=0.01)
        tidal_volume = st.number_input("Tidal Volume", min_value=0.0, max_value=1.0, step=0.0001)
        inspiratory_time = st.number_input("Inspiratory Time", min_value=0.0, max_value=0.7, step=0.001)

    # second column
    with breathing_metrics_2:
        expiratory_time = st.number_input("Expiratory Time", min_value=0.0, max_value=2.5, step=0.5)
        penh = st.number_input("Penh", min_value=0.0, max_value=3.0, step=0.01)
    #exposure column
    st.markdown("## 🌪️ Environmental Exposure")
    exposure = st.selectbox("Exposure", ["Air", "Smog","Unknown"])        

    # Submit button
    submitted = st.form_submit_button("Predict Early-life Diet")

# Display these results after form submission
# One hot-encode exposure column in streamlit
if submitted:

    Exposure_Air = 1 if exposure == "Air" else 0
    Exposure_Smog = 1 if exposure == "Smog" else 0
    Exposure_Unknown = 1 if exposure == "Unknown" else 0


    # Create dataframe from columns
    
    data = pd.DataFrame([[Exposure_Air, Exposure_Smog,Exposure_Unknown,breathing_frequency,tidal_volume, inspiratory_time, expiratory_time, penh]], columns=features)

    #Predict class using best model(Gradient Boosting)
    prediction = loaded_model.predict(data)[0]
    probability = loaded_model.predict_proba(data).max()

    # Predict admission chance
    if prediction == 0:
        st.success(f"This subject had an early-life normal diet(ND):",icon = "✅")
    else:
        st.warning(f"This subject had an early-life vitamin-D deficient diet(VDD):", icon="🚩")
    
    st.info(f"Model confidence: :{probability}")
    st.warning(f"This prediction is very tentative.\n The model currently treats each observation as independent, but the data are longitudinal — true patterns over time within each mouse are not captured. Interpret the results with caution.") 
