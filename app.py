import streamlit as st
import os

from src.transcriber import transcribe_audio
from src.sentiment_analyzer import analyze_sentiment
from src.summarizer import generate_summary
from src.keyword_extractor import extract_keywords
from src.report_generator import generate_pdf_report

st.set_page_config(
    page_title="AI Speech-to-Text Analyzer",
    page_icon="🎙️",
    layout="wide"
)

st.title("🎙️ AI Speech-to-Text & NLP Analyzer")
st.write("Upload an audio file to generate transcript, sentiment analysis, keywords, summary and downloadable reports.")

os.makedirs("outputs", exist_ok=True)

# Session state initialization
if "analysis_done" not in st.session_state:
    st.session_state.analysis_done = False

if "transcript" not in st.session_state:
    st.session_state.transcript = ""

if "sentiment" not in st.session_state:
    st.session_state.sentiment = ""

if "score" not in st.session_state:
    st.session_state.score = {}

if "summary" not in st.session_state:
    st.session_state.summary = ""

if "keywords" not in st.session_state:
    st.session_state.keywords = []

if "transcript_path" not in st.session_state:
    st.session_state.transcript_path = ""

if "pdf_path" not in st.session_state:
    st.session_state.pdf_path = ""

uploaded_file = st.file_uploader(
    "Upload an audio file",
    type=["mp3", "wav", "m4a"]
)

if uploaded_file is not None:
    audio_path = os.path.join("outputs", uploaded_file.name)

    with open(audio_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.audio(audio_path)

    if st.button("Analyze Audio"):
        with st.spinner("Transcribing audio... Please wait."):
            transcript = transcribe_audio(audio_path)

        if transcript.startswith("Transcription Error"):
            st.error(transcript)
            st.session_state.analysis_done = False
        else:
            sentiment, score = analyze_sentiment(transcript)
            summary = generate_summary(transcript)
            keywords = extract_keywords(transcript)

            transcript_path = "outputs/transcript.txt"
            with open(transcript_path, "w", encoding="utf-8") as f:
                f.write(transcript)

            pdf_path = generate_pdf_report(
                transcript,
                sentiment,
                summary,
                keywords
            )

            # Store everything in session state
            st.session_state.analysis_done = True
            st.session_state.transcript = transcript
            st.session_state.sentiment = sentiment
            st.session_state.score = score
            st.session_state.summary = summary
            st.session_state.keywords = keywords
            st.session_state.transcript_path = transcript_path
            st.session_state.pdf_path = pdf_path

# Display results if analysis is done
if st.session_state.analysis_done:
    st.success("Analysis completed successfully!")

    col1, col2, col3 = st.columns(3)

    col1.metric("Word Count", len(st.session_state.transcript.split()))
    col2.metric("Sentiment", st.session_state.sentiment)
    col3.metric("Keywords Found", len(st.session_state.keywords))

    st.subheader("Transcript")
    st.write(st.session_state.transcript)

    st.subheader("Summary")
    st.write(st.session_state.summary)

    with st.expander("View Detailed Sentiment Score"):
        st.json(st.session_state.score)

    st.subheader("Top Keywords")

    keyword_data = {
        "Keyword": [word for word, count in st.session_state.keywords],
        "Frequency": [count for word, count in st.session_state.keywords]
    }

    st.table(keyword_data)

    st.markdown("### Download Results")

    col_download1, col_download2, col_space = st.columns([1, 1, 5])

    with col_download1:
        with open(st.session_state.transcript_path, "rb") as file:
         st.download_button(
            label="Download Transcript",
            data=file,
            file_name="transcript.txt",
            mime="text/plain",
            key="download_transcript"
        )

    with col_download2:
        with open(st.session_state.pdf_path, "rb") as file:
            st.download_button(
                label="Download PDF Report",
                data=file,
                file_name="speech_analysis_report.pdf",
                mime="application/pdf",
                key="download_pdf"
            )

else:
    st.info("Please upload an audio file to begin analysis.")

st.markdown("<br><br><br><br>", unsafe_allow_html=True)
st.markdown("---")
st.caption("Built using Python, Streamlit, Whisper and NLP techniques.")