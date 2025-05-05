import langchain_google_genai
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage
from dotenv import load_dotenv
import os

#load_dotenv()
#api_key = os.getenv("GOOGLE_API_KEY")
#api_key = GOOGLE_API_KEY

import streamlit as st

def get_gemini_response(input_text):
    llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    google_api_key=api_key,
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2
)
    message = [HumanMessage(content=input_text)]
    response=llm.invoke(message)
    return response.content


st.set_page_config(page_title = "Q&A demo")
st.header("💭Langchain Application💭")

input = st.text_input("Input:",key="input")


submit = st.button("Generate⚙️")

if submit:
    response = get_gemini_response(input)
    st.subheader("The Response is 🧠 ")
    st.write(response)
