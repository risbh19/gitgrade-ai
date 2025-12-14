import streamlit as st

from utils.github_fetcher import fetch_repo_data
from utils.scoring import calculate_score
from utils.ai_feedback import generate_summary, generate_roadmap

st.set_page_config(page_title="GitGrade", layout="centered")

st.title("GitGrade – AI GitHub Repository Evaluator")
st.write("Analyze your GitHub repository like a recruiter or mentor.")

repo_url = st.text_input("Enter a public GitHub repository URL")

if st.button("Analyze Repository"):
    try:
        with st.spinner("Analyzing repository..."):
            data = fetch_repo_data(repo_url)
            score, reasons = calculate_score(data)
            summary = generate_summary(data, score)
            roadmap = generate_roadmap(data)

        st.success("Analysis Complete")

        st.subheader(f"Score: {score}/100")

        st.subheader("Summary")
        st.write(summary)

        st.subheader("Why this score?")
        for r in reasons:
            st.write(f"- {r}")

        st.subheader("Personalized Improvement Roadmap")
        for step in roadmap:
            st.write(f"- {step}")

    except Exception as e:
        st.error(f"Error: {str(e)}")
