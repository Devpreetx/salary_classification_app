import streamlit as st
import pandas as pd
import joblib
from sklearn.preprocessing import LabelEncoder

model = joblib.load('best_model.pkl')

Relation_categories = ['Husband','Not-in-family','Own-child','Unmarried','Wife', 'Other-relative']
workclass_categories = ['Private','Self-emp-not-inc','Local-gov','Others','Self-emp-inc','Federal-gov']
gender_categories = ['Male', 'Female']
occupation_categories = [
    'Prof-specialty', 'Craft-repair', 'Exec-managerial', 'Adm-clerical',
    'Sales', 'Other-service', 'Machine-op-inspct', 'Others',
    'Transport-moving', 'Handlers-cleaners', 'Farming-fishing',
    'Tech-support', 'Protective-serv', 'Priv-house-serv', 'Armed-Forces'
]
education_mapping = {
    '12th': 8,
    'HS-grad': 9,
    'Some-college': 10,
    'Assoc-voc': 11,
    'Assoc-acdm': 12,
    'Bachelors': 13,
    'Masters': 14,
    'Prof-school': 15,
    'Doctorate': 16
}
race_categories = ['White', 'Black', 'Asian-Pac-Islander', 'Amer-Indian-Eskimo', 'Other']
marital_categories = [
    'Married-civ-spouse',
    'Never-married',
    'Divorced',
    'Separated',
    'Widowed',
    'Married-spouse-absent',
    'Married-AF-spouse'
]
country_categories = [
    'United-States', 'Mexico', 'Philippines', 'Germany', 'Puerto-Rico', 'Canada',
    'El-Salvador', 'India', 'Cuba', 'England', 'China', 'South', 'Jamaica', 'Italy',
    'Dominican-Republic', 'Japan', 'Guatemala', 'Poland', 'Vietnam', 'Columbia',
    'Haiti', 'Portugal', 'Taiwan', 'Iran', 'Nicaragua', 'Greece', 'Peru', 'Ecuador',
    'France', 'Ireland', 'Thailand', 'Hong', 'Cambodia', 'Trinadad&Tobago', 'Laos',
    'Outlying-US(Guam-USVI-etc)', 'Yugoslavia', 'Scotland', 'Honduras', 'Hungary',
    'Holand-Netherlands', 'others'
]

relationship_encoder = LabelEncoder()
relationship_encoder.fit(Relation_categories)
workclass_encoder = LabelEncoder()
workclass_encoder.fit(workclass_categories)
gender_encoder = LabelEncoder()
gender_encoder.fit(gender_categories)
occupation_encoder = LabelEncoder()
occupation_encoder.fit(occupation_categories)
race_encoder = LabelEncoder()
race_encoder.fit(race_categories)
marital_encoder = LabelEncoder()
marital_encoder.fit(marital_categories)
country_encoder = LabelEncoder()
country_encoder.fit(country_categories)

st.subheader("🧑 Predict for New Employee")

col1, col2 = st.columns(2)

with col1:
    age = st.slider("🎂 Age", 17, 90, 30)
    workclass = st.selectbox("🏢 Workclass", workclass_categories)
    fnlwgt = st.number_input("🧮 Final Weight (Fnlwgt)", 10000, 1000000, 200000)
    education = st.selectbox("🎓 Education Level", list(education_mapping.keys()))
    marital_status = st.selectbox("💍 Marital Status", marital_categories)
    
with col2:
    occupation = st.selectbox("🛠️ Occupation", occupation_categories)
    relationship = st.selectbox("👥 Relationship Type", Relation_categories)
    race = st.selectbox("🌍 Race", race_categories)
    gender = st.selectbox("⚧️ Gender", gender_categories)


with st.expander("🔧 Advanced Settings"):
    capital_gain = st.number_input("💰 Capital Gain", 0, 100000, 0)
    capital_loss = st.number_input("📉 Capital Loss", 0, 5000, 0)
    hours_per_week = st.slider("🕒 Hours per Week", 1, 99, 40)
    country = st.selectbox("🌐 Native Country", country_categories)


workclass_value = workclass_encoder.transform([workclass])[0]
Relation_value = relationship_encoder.transform([relationship])[0]
gender_value = gender_encoder.transform([gender])[0]
occupation_value = occupation_encoder.transform([occupation])[0]
race_value = race_encoder.transform([race])[0]
marital_status= marital_encoder.transform([marital_status])[0]
education_value = education_mapping[education]
country_value = country_encoder.transform([country])[0]

with st.expander("🔍 Preview Inputs (click to expand)"):
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown(f"**Age:** {age}")
        st.markdown(f"**Fnlwgt:** {fnlwgt}")
        st.markdown(f"**Capital Gain:** {capital_gain}")
        st.markdown(f"**Race:** {race}")
    with col2:
        st.markdown(f"**Workclass:** {workclass}")
        st.markdown(f"**Education:** {education}")
        st.markdown(f"**Capital Loss:** {capital_loss}")
        st.markdown(f"**Gender:** {gender}")
    with col3:
        st.markdown(f"**Marital Status:** {marital_status}")
        st.markdown(f"**Occupation:** {occupation}")
        st.markdown(f"**Hours/Week:** {hours_per_week}")
        st.markdown(f"**Country:** {country}")

input_data = pd.DataFrame([[age, workclass_value, fnlwgt, education_value, marital_status,
                            occupation_value, Relation_value, race_value, gender_value,
                            capital_gain, capital_loss, hours_per_week,
                            country_value]])

if st.button("Predict Income"):
    prediction = model.predict(input_data)[0]
    st.success(f"🔮 Predicted Income Group: {prediction}")
