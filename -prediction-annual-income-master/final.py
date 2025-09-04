import streamlit as st
import pandas as pd
import joblib  

st.set_page_config(page_title="Income Prediction App", layout="wide")

st.title(" Income Prediction App")
st.write("This app predicts whether a person earns **<=50K or >50K** based on census data features.")


# Sidebar Inputsst.sidebar.header("User Input Features")
age = st.sidebar.number_input("Age", min_value=17, max_value=90, value=38, step=1)

workclass = st.sidebar.selectbox("Workclass", options=[
    ' Self-emp-not-inc', ' Private', ' State-gov', ' Federal-gov',
    ' Local-gov', ' ?', ' Self-emp-inc', ' Without-pay',
    ' Never-worked'
])

education = st.sidebar.selectbox("Education", options=[
       ' Bachelors', ' HS-grad', ' 11th', ' Masters', ' 9th',
       ' Some-college', ' Assoc-acdm', ' Assoc-voc', ' 7th-8th',
       ' Doctorate', ' Prof-school', ' 5th-6th', ' 10th', ' 1st-4th',
       ' Preschool', ' 12th'])

occupation = st.sidebar.selectbox("Occupation", options=[
       ' Exec-managerial', ' Handlers-cleaners', ' Prof-specialty',
       ' Other-service', ' Adm-clerical', ' Sales', ' Craft-repair',
       ' Transport-moving', ' Farming-fishing', ' Machine-op-inspct',
       ' Tech-support', ' ?', ' Protective-serv', ' Armed-Forces',
       ' Priv-house-serv'
])


relationship = st.sidebar.selectbox("Relationship", options=[
' Husband', ' Not-in-family', ' Wife', ' Own-child', ' Unmarried',
       ' Other-relative'
])

race = st.sidebar.selectbox("Race", options=[
    ' White', ' Black', ' Asian-Pac-Islander', ' Amer-Indian-Eskimo',
       ' Other'
])

sex = st.sidebar.selectbox("Sex", options=["Male", "Female"])

capital_gain = st.sidebar.number_input("Capital Gain", min_value=0, max_value=100000, value=0, step=100)
capital_loss = st.sidebar.number_input("Capital Loss", min_value=0, max_value=100000, value=0, step=100)
hours_per_week = st.sidebar.number_input("Hours per Week", min_value=13, max_value=95, value=40, step=1)
# Collect Data

input_data = {
    "age": age,
    "workclass": workclass,
    "education": education,
    "occupation": occupation,
    "relationship": relationship,
    "race": race,
    "sex": sex,
    "capital-gain": capital_gain,
    "capital-loss": capital_loss,
    "hours-per-week": hours_per_week
}

df_input = pd.DataFrame([input_data])

st.subheader("User Input Summary")
st.dataframe(df_input)



if st.button("Predict"):
    # Model Prediction (replace with your model)
    model = joblib.load("income_model.pkl")
    prediction = model.predict(df_input)    
    print(prediction)
    if prediction[0] == " >50K":
        st.success("The income is greater than 50k")
    else:
        st.success("The income is less than 50k")



