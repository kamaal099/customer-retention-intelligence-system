import streamlit as st
import numpy as np
import joblib

# -------------------------------
# Load Model
# -------------------------------
st.set_page_config(page_title="Customer Retention System", layout="centered")

st.write("🚀 App starting...")

try:
    model = joblib.load('churn_model.pkl')
    scaler = joblib.load('scaler.pkl')
    st.success("✅ Model loaded successfully!")
except Exception as e:
    st.error(f"❌ Error loading model: {e}")

# -------------------------------
# Title
# -------------------------------
st.title("💳 Customer Retention Intelligence System")
st.markdown("Predict customer churn and get **actionable retention strategies**")

# -------------------------------
# Input Section
# -------------------------------
st.subheader("📋 Enter Customer Details")

col1, col2 = st.columns(2)

with col1:
    credit_score = st.number_input("Credit Score", 300, 900, 600)
    age = st.slider("Age", 18, 100, 30)
    tenure = st.slider("Tenure (years)", 0, 10, 3)
    balance = st.number_input("Balance", value=50000.0)
    products = st.slider("Number of Products", 1, 4, 1)

with col2:
    country = st.selectbox("Country", ["France", "Spain", "Germany"])
    gender = st.selectbox("Gender", ["Male", "Female"])
    credit_card = st.selectbox("Has Credit Card", [0, 1])
    active = st.selectbox("Is Active Member", [0, 1])
    salary = st.number_input("Estimated Salary", value=50000.0)

# -------------------------------
# Encoding
# -------------------------------
country_map = {"France": 0, "Spain": 1, "Germany": 2}
gender_map = {"Male": 1, "Female": 0}

country = country_map[country]
gender = gender_map[gender]

# -------------------------------
# Prediction
# -------------------------------
if st.button("🔍 Predict Churn"):

    try:
        input_data = np.array([[credit_score, country, gender, age, tenure,
                                balance, products, credit_card, active, salary]])

        input_scaled = scaler.transform(input_data)

        # 🔥 Probability-based prediction
        prob = model.predict_proba(input_scaled)[0][1]
        prediction = (prob > 0.4).astype(int)

        st.markdown("---")
        st.subheader("📊 Prediction Result")

        st.write(f"🔎 **Churn Probability:** `{prob:.2f}`")

        if prediction == 1:
            st.error("⚠️ High Risk of Churn")

            st.subheader("💡 Recommended Actions")

            if age > 50:
                st.info("👉 Provide senior citizen benefits")
            elif balance > 100000:
                st.info("👉 Offer premium banking services")
            elif active == 0:
                st.info("👉 Increase engagement with personalized offers")
            elif products == 1:
                st.info("👉 Cross-sell additional products")
            else:
                st.info("👉 Provide discounts and loyalty rewards")

        else:
            st.success("✅ Low Risk Customer")
            st.info("👍 Maintain engagement and satisfaction")

    except Exception as e:
        st.error(f"❌ Prediction error: {e}")

# -------------------------------
# Footer
# -------------------------------
st.markdown("---")
st.markdown("🚀 Built with Streamlit | ML Project")