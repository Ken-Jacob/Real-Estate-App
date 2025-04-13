import streamlit as st
import pandas as pd
from data_preprocessing import load_data, preprocess_data
from model_training import train_model
from logger import get_logger

logger = get_logger(__name__)
st.set_page_config(page_title="Real Estate Smart Predictor", layout="centered")

# Title
st.markdown("<h1 style='text-align: center;'>🏢 Real Estate Smart Predictor</h1>", unsafe_allow_html=True)
st.markdown("---")

try:
    df = load_data("data/final.csv")
    processed_df = preprocess_data(df)
    model = train_model(processed_df)

    st.markdown("### 📋 Enter Property Details")

    # Organize inputs in columns
    col1, col2 = st.columns(2)

    with col1:
        beds = st.number_input("Bedrooms", 1, 10, 3)
        sqft = st.number_input("Square Ft.", 500, 10000, 1500)
        year_built = st.number_input("Year Built", 1900, 2024, 2005)
        lot_size = st.number_input("Lot Size (acres)", 1.0, 100.0, 5.0)
        popular = st.selectbox("Popular Location?", [0, 1], format_func=lambda x: "Yes" if x else "No")

    with col2:
        baths = st.number_input("Bathrooms", 1, 10, 2)
        year_sold = st.number_input("Year Sold", 2000, 2025, 2023)
        basement = st.selectbox("Basement?", [0, 1], format_func=lambda x: "Yes" if x else "No")
        recession = st.selectbox("During Recession?", [0, 1], format_func=lambda x: "Yes" if x else "No")
        property_type = st.selectbox("Property Type", ["Bunglow", "Condo", "Other"])

    property_age = max(0,year_sold - year_built)
    input_df = pd.DataFrame([{
        'beds': beds, 'baths': baths, 'sqft': sqft,
        'year_built': year_built, 'lot_size': lot_size, 'basement': basement,
        'popular': popular, 'recession': recession, 'year_sold': year_sold,
        'property_age': property_age,
        'property_type_Bunglow': int(property_type == 'Bunglow'),
        'property_type_Condo': int(property_type == 'Condo')
    }])

    for col in processed_df.columns:
        if col not in input_df.columns and col != "price":
            input_df[col] = 0
    input_df = input_df[processed_df.drop("price", axis=1).columns]

    if st.button("🔍 Predict Price"):
        with st.spinner("Calculating..."):
            prediction = model.predict(input_df)
        st.markdown(
            f"<div style='text-align:center;padding:20px;background:#004d00;border-radius:10px;color:white;font-size:24px;'>"
            f"💰 Estimated Property Price: <strong>${prediction[0]:,.2f}</strong></div>",
            unsafe_allow_html=True
        )
except Exception as e:
    logger.error("Error in app execution", exc_info=True)
    st.error("Something went wrong. Please check the logs.")
