import streamlit as st
from pdf_reader import extract_text_from_pdf
from llm_summarizer import summarize_paper, ask_question

st.title("AI Research Paper Simplifier")

uploaded_file = st.file_uploader("Upload Research Paper", type="pdf")

if uploaded_file:

    st.write("Reading PDF...")

    text = extract_text_from_pdf(uploaded_file)

    with st.spinner("Generating summary..."):
        summary = summarize_paper(text)

    st.subheader("Paper Summary")
    st.write(summary)

    st.divider()

    st.subheader("Chat with Research Paper")

    question = st.text_input("Ask a question about the paper")

    if st.button("Ask AI"):

        with st.spinner("Thinking..."):
            answer = ask_question(text, question)

        st.write(answer)