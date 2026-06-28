import streamlit as st

from ai.assistant import build_summary, ask_ai


def render(df, forecast):
    st.title("AI Assistant")
    st.caption("Ask business questions about the current filtered dashboard.")

    st.divider()

    summary = build_summary(df, forecast)

    st.subheader("Suggested Questions")

    suggestions = [
        "Why is profit low?",
        "Which category performs best?",
        "Which region generates the most revenue?",
        "How can sales improve?",
        "Are discounts affecting profitability?"
    ]

    selected_question = st.selectbox(
        "Choose a question",
        ["Choose a question..."] + suggestions
    )

    custom_question = st.text_area(
        "Or ask your own question",
        placeholder="Example: What should the business focus on next?",
        height=120
    )

    if custom_question.strip():
        question = custom_question.strip()
    elif selected_question != "Choose a question...":
        question = selected_question
    else:
        question = ""

    if st.button("✨ Analyze", use_container_width=True):
        if not question:
            st.warning("Please choose or type a question.")
        else:
            with st.spinner("AI is analyzing the dashboard..."):
                answer = ask_ai(question, summary)

            st.success("Analysis complete")
            st.markdown(answer)

    st.divider()
