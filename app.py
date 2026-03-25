
import streamlit as st
from ocr.ocr_engine import extract_text
from grading.semantic_grader import grade_answer

st.title("Handwritten Answer Evaluation (Question-wise)")

question = st.text_area("Question")
answer_key = st.text_area("Answer Key")
image = st.file_uploader("Upload Handwritten Answer Image", type=["jpg","png","jpeg"])

if st.button("Evaluate") and image and answer_key:
    text = extract_text(image)
    score, marks = grade_answer(text, answer_key)
    st.subheader("Extracted Text")
    st.write(text)
    st.subheader("Result")
    st.write(f"Similarity Score: {score}")
    st.write(f"Marks: {marks}/5")
