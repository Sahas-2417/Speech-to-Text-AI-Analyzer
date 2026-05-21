from fpdf import FPDF
import os

def generate_pdf_report(transcript, sentiment, summary, keywords, output_path="outputs/report.pdf"):
    pdf = FPDF()
    pdf.add_page()

    pdf.set_font("Arial", "B", 16)
    pdf.cell(0, 10, "AI Speech-to-Text Analysis Report", ln=True, align="C")

    pdf.ln(10)

    pdf.set_font("Arial", "B", 12)
    pdf.cell(0, 10, "Sentiment Analysis:", ln=True)

    pdf.set_font("Arial", "", 11)
    pdf.multi_cell(0, 8, f"Overall Sentiment: {sentiment}")

    pdf.ln(5)

    pdf.set_font("Arial", "B", 12)
    pdf.cell(0, 10, "Summary:", ln=True)

    pdf.set_font("Arial", "", 11)
    pdf.multi_cell(0, 8, summary)

    pdf.ln(5)

    pdf.set_font("Arial", "B", 12)
    pdf.cell(0, 10, "Top Keywords:", ln=True)

    pdf.set_font("Arial", "", 11)
    for word, count in keywords:
        pdf.cell(0, 8, f"{word} - {count}", ln=True)

    pdf.ln(5)

    pdf.set_font("Arial", "B", 12)
    pdf.cell(0, 10, "Transcript:", ln=True)

    pdf.set_font("Arial", "", 10)
    pdf.multi_cell(0, 7, transcript)

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    pdf.output(output_path)

    return output_path