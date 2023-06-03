import streamlit as st 
import pandas as pd 
from utils import unique_values
from model_loader import Model


st.set_page_config(
    page_title="Salary Predictor",
    page_icon="💖",
    initial_sidebar_state="collapsed",
)
st.markdown("""<style>.css-9s5bis.edgvbvh3 {visibility:hidden;}.css-h5rgaw.egzxvld1{visibility:hidden;}</style>""",unsafe_allow_html=True)
st.header("Welcome.. Please fill the form below carefully  ")
st.caption("It can give you a great Idea about how much your salary can be based on your preference of the job")

with st.form("my_form",clear_on_submit=True):
   output = dict()

   output['Size'] = st.selectbox('Enter the size of company you are searching for:',options=unique_values('Size'))
   output['Type of ownership'] = st.selectbox("select the type of company you want to work for: ",options=unique_values("Type of ownership"))
   output['Industry'] = st.selectbox("select the Type of Industry you want to work for:",options=unique_values("Industry"))
   output['Revenue'] = st.selectbox("overall Revenue of Company you are expecting:",options=unique_values("Revenue"))
   output['job_state'] = st.selectbox('select the job state **applicable only for west countries**',options=unique_values('job_state'))
   output['age'] = st.number_input('enter your age',min_value=18,max_value=50)

   title = st.selectbox('Select the Job role ',options=unique_values("job_simp"))
   sen = st.selectbox('What can be your Level?',options=unique_values("seniority"))
   tech_stack = st.multiselect('Select the Tools you are familiar with...',['Python','AWS','Spark','SQL','Excel'])

   submitted = st.form_submit_button("Submit")
   
   output['python_yn'] = 1 if 'Python' in tech_stack else 0
   output['spark'] = 1 if 'Spark' in tech_stack else 0
   output['aws'] = 1 if 'AWS' in tech_stack else 0
   output['excel'] = 1  if 'Excel' in tech_stack else 0

   output['job_simp'] =title
   output['seniority'] = sen 
if submitted:
    df = pd.DataFrame(output,index=[0])

    processing = Model()
    transformation = processing.preprocessing(df)
    prediction = processing.Predict(transformation)
    st.write(f"You May find a job of Salary range around ${round(prediction[0])}K")

