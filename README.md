# 🎙️ AI Speech-to-Text & NLP Analyzer

An AI-powered web application that converts audio speech into text and performs Natural Language Processing (NLP) tasks such as sentiment analysis, keyword extraction, summary generation, and report downloading.

This project is built using **Python, Streamlit, OpenAI Whisper, and NLP techniques**.

---

## 🚀 Live Demo

🔗 **Deployed App:** https://speech-to-text-ai-analyzer-sahas.streamlit.app/

---

## 📌 Project Overview

The **AI Speech-to-Text & NLP Analyzer** allows users to upload an audio file and automatically convert the speech into text using an AI-based transcription model. After generating the transcript, the application analyzes the text to identify sentiment, extract important keywords, generate a short summary, and provide downloadable output files.

This project combines **Speech Recognition**, **Natural Language Processing**, and **Interactive Web App Development** into a single end-to-end application.

---

## ✨ Features

- 🎧 Upload audio files in MP3, WAV, or M4A format
- 📝 Convert speech into text using Whisper
- 📊 Display word count of the transcript
- 😊 Perform sentiment analysis on the transcript
- 🔑 Extract top keywords from the generated text
- 📄 Generate a short summary of the transcript
- 📥 Download transcript as a TXT file
- 📑 Download complete analysis report as a PDF
- 🌐 Interactive Streamlit-based user interface
- ☁️ Deployed on Streamlit Community Cloud

---

## 🛠️ Tech Stack

- **Python**
- **Streamlit**
- **OpenAI Whisper**
- **VADER Sentiment Analysis**
- **FPDF**
- **FFmpeg**
- **NLP Techniques**

---

## 📂 Project Structure

```text
Speech-to-Text-AI-Analyzer/
│
├── app.py
├── requirements.txt
├── packages.txt
├── README.md
├── .gitignore
│
├── src/
│   ├── transcriber.py
│   ├── sentiment_analyzer.py
│   ├── summarizer.py
│   ├── keyword_extractor.py
│   └── report_generator.py
│
├── sample_audio/
├── screenshots/
└── outputs/
