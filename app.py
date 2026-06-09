import streamlit as st
from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

st.set_page_config(page_title="QA Copilot", page_icon="🧪")
st.title("🧪 QA Copilot")
st.caption("Your AI-powered QA Assistant")

def ask_ai(prompt):
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content

tab1, tab2, tab3, tab4 = st.tabs([
    "📝 Test Case Generator",
    "🐛 Bug Report Improver",
    "💬 QA Mentor Chat",
    "📊 Test Summary Generator"
])

with tab1:
    st.header("Test Case Generator")
    user_story = st.text_area("Paste your User Story here:")
    if st.button("Generate Test Cases"):
        if user_story:
            with st.spinner("Generating..."):
                prompt = f"You are a senior QA engineer. Generate detailed test cases for this user story:\n\n{user_story}"
                st.write(ask_ai(prompt))

with tab2:
    st.header("Bug Report Improver")
    bug_report = st.text_area("Paste your rough bug report here:")
    if st.button("Improve Bug Report"):
        if bug_report:
            with st.spinner("Improving..."):
                prompt = f"You are a senior QA engineer. Rewrite this bug report professionally with clear steps to reproduce, expected result, actual result, and severity:\n\n{bug_report}"
                st.write(ask_ai(prompt))

with tab3:
    st.header("QA Mentor Chat")
    question = st.text_input("Ask any QA question:")
    if st.button("Ask"):
        if question:
            with st.spinner("Thinking..."):
                prompt = f"You are an expert QA mentor. Answer this question clearly:\n\n{question}"
                st.write(ask_ai(prompt))

with tab4:
    st.header("Test Summary Generator")
    raw_results = st.text_area("Paste your raw test results here:")
    if st.button("Generate Summary"):
        if raw_results:
            with st.spinner("Generating..."):
                prompt = f"You are a senior QA engineer. Create a professional test summary report from these results:\n\n{raw_results}"
                st.write(ask_ai(prompt))