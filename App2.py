import streamlit as st
from PIL import Image

st.title('My First Web App')

img = Image.open('Web2.jpg')
st.image(img)

st.text_input('Name', placeholder='Edet, Bassey Dominic')
st.text_area('Description', max_chars=150)
st.number_input('Weight', min_value=2, max_value=150, step=2)
st.radio('Gender', ['Male', 'Female'])
st.sidebar.selectbox('Country', ['Algeria', 'Denmark', 'Ghana', 'Nigeria', 'United States', 'United Kingdom'])
st.sidebar.multiselect('Skills Acquired', ['MS Excel', 'MySQL', 'Power BI', 'Python', 'Java', 'R'])


if st.checkbox('Agree'):
    st.write('Permission granted')
else:
    st.error('Click Agree')

if st.button('Calculate'):
    st.success('Calculation Successful')
    st.balloons()

st.file_uploader('Upload your CV', type=['PDF', '.docx'])

st.sidebar.camera_input('Say Cheese')
st.date_input('Date of Birth')