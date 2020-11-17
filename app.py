from summarizer import Summarizer
import streamlit as st

st.header('Text Summarizer:')
user_input = st.text_area('Insert raw text here:')
model = Summarizer()
min_length = st.slider('Summary Length', 30, 100, 60)
generate_sum = st.button('Generate Summary')
if generate_sum:
    summary = model(user_input, min_length=min_length)
    st.subheader('Summary')
    st.write(summary)
