import streamlit as st


age = st.sidebar.number_input("Age",min_value=0,max_value=80,value=20,step=1)
workclass = st.sidebar.selectbox("Workclass", options=["Private",
                                                       "Self-emp-not-inc",
                                                       "Local-gov","Unknow",
                                                       "State-gov","Self-emp-inc",
                                                       "Federal-gov","Without-pay",""
                                                       "Never-worked"],
                                                       index=0)

education_num = st.sidebar.number_input("Education Number")
occupation = st.sidebar.selectbox("Occupation",options=["Prof-specialty",
                                                        "Craft-repair",
                                                        "Exec-managerial"])
relationship = st.sidebar.selectbox("Relationship",options=["Husband",
                                                            "Not-in-family",
                                                            "Own-child",
                                                            "Unmarried","Wife",
                                                            "Other-relative"])
race = st.sidebar.selectbox("Race", options=["White","Black",
                                             "Asian-Pac-Islander",
                                             "Asian-Indain-Eskimo",
                                             "Other"])
sex = st.sidebar.selectbox("Sex", options=["Male", "Female"])
capital_gain = st.sidebar.number_input("Capital Gain",0,30,10) 
capital_loss = st.sidebar.number_input("Capital Loss",0,30,10) 
hours_per_week = st.sidebar.number_input("Capital Gain",0,50,10) 

st.write("workclass", workclass)