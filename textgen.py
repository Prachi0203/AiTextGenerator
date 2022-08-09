
import streamlit as st
from aitextgen import aitextgen
st.title("AITEXTGEN Web App")
ai = aitextgen()
prompt_text = st.text_input(label = "enter your prompt text....", value = "Computer is beautiful")
with st.spinner("AI is at Work.."):
	gpt_text = ai.generate_one(prompt = prompt_text,max_length = 100)
st.success("AI successfully generated below text")
st.balloons()
print(gpt_text)
st.text(gpt_text)
