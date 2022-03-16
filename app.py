import streamlit as st
import pickle


model = pickle.load(open('Brainrf_mod.pkl', 'rb'))

st.title("Brain Stroke Prediction")
Gender = str(st.selectbox('gender', ['Male', 'Female']))
if Gender=='Male':
    Gender=1

elif Gender=='Female':
    Gender=0
else:
    Gender=2
Age = st.text_input("Age")

HyperTension = str(st.selectbox('hypertension', ['Yes', 'No']))

if HyperTension=='Yes':
    HyperTension=1
else:
    HyperTension=0
HeartDisease = str(st.selectbox('heart_disease', ['Yes', 'No']))
if HeartDisease=='Yes':
    HeartDisease=1
else:
    HeartDisease=0

EverMarried=str(st.selectbox('ever_married',['Yes','No']))

if EverMarried=='Yes':
    EverMarried=1
else:
    EverMarried=0

WorkType=str(st.selectbox('work_type',['Private','Self-employed','Govt_job','children','Never_worked']))

if WorkType=='Private':
    WorkType=2
elif WorkType=='Self-employed':
    WorkType=3
elif WorkType=='Govt_job':
    WorkType=0
elif WorkType=='children':
    WorkType=4
else:
    WorkType=1
ResidenceType=str(st.selectbox('Residence_type',['Urban','Rural']))
if ResidenceType=='Urban':
    ResidenceType=1
else:
    ResidenceType=0
AveargeGlucoseLevel=st.text_input('avg_glucose_level')
BMI=st.text_input('bmi')

SmokingStatus=str(st.selectbox('smoking_status',['formerly smoked','never smoked','smokes','Unknown']))
if SmokingStatus=='formerly smoked':
    SmokingStatus=1
elif SmokingStatus=='never smoked':
    SmokingStatus=2
elif SmokingStatus=='smokes':
    SmokingStatus=3
else:
    SmokingStatus=0

if st.button("Predict Brain Stroke"):
    query = model.predict([[Gender,Age, HyperTension,HeartDisease,EverMarried,WorkType,ResidenceType,AveargeGlucoseLevel,BMI,SmokingStatus]])
    if query[0]==0:
        st.success(f'Great! Not Stroke')
    else:
        st.success(f'Attention! It is Stroke')

