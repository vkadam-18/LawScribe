import os
import streamlit as st
import google.generativeai as genai
import PyPDF2
import docx
from io import BytesIO

def extract_text_from_pdf(file):
    """Extract text from a PDF file."""
    text = ""
    with BytesIO(file.read()) as f:
        reader = PyPDF2.PdfReader(f)
        for page in reader.pages:
            text += page.extract_text() + "\n"
    return text

def extract_text_from_docx(file):
    """Extract text from a DOCX file."""
    doc = docx.Document(BytesIO(file.read()))
    text = ""
    for paragraph in doc.paragraphs:
        text += paragraph.text + "\n"
    return text

def extract_text_from_txt(file):
    """Extract text from a TXT file."""
    text = file.read().decode("utf-8")  # Decode the byte stream to string
    return text

def save_summary_to_file(summary):
    """Save the summary to a text file."""
    with open("summary.txt", "w") as f:
        f.write(summary)

def main():
    # Set your Gemini API key directly here
    api_key = 'AIzaSyDnE8XWUYKgWqhmGRdWI6nZI_ODhRvo1jE'  
    genai.configure(api_key=api_key)

    # Set up the Streamlit interface
    st.title("Legal Document Summarizer")
    st.markdown("Upload a legal document and generate a concise summary.")

    # User input for file upload
    uploaded_file = st.file_uploader("Upload a legal document (PDF, DOCX, TXT)", type=["pdf", "docx", "txt"])

    summary_length = st.selectbox("Select summary length:", ["Short", "Medium", "Long"])

    # Preview the text extracted from the uploaded document
    if uploaded_file is not None:
        if uploaded_file.type == "application/pdf":
            text = extract_text_from_pdf(uploaded_file)
        elif uploaded_file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
            text = extract_text_from_docx(uploaded_file)
        elif uploaded_file.type == "text/plain":
            text = extract_text_from_txt(uploaded_file)
        else:
            st.warning("Unsupported file type. Please upload PDF, DOCX, or TXT files.")
            return

        st.subheader("Extracted Text Preview:")
        st.text_area("Preview of extracted text:", text, height=200)

    # Button to generate summary
    if st.button("Generate Summary") and uploaded_file is not None:
        if text.strip():
            # Create a prompt for generating the summary based on the selected length
            length_mapping = {
                "Short": "Summarize the following legal document into a concise summary in 50 words:",
                "Medium": "Summarize the following legal document into a medium-length summary in 150 words:",
                "Long": "Summarize the following legal document into a detailed summary in 300 words:"
            }
            prompt = f"""
            {length_mapping[summary_length]}

            "{text}"

            The summary should capture the main legal points and be suitable for a general audience.
            """

            try:
                #spinner
                with st.spinner("Generating summary..."):
                    model = genai.GenerativeModel("gemini-1.5-flash")
                    response = model.generate_content(prompt)
                    summary = response.text

                #session
                st.session_state.generated_summary = summary
                st.session_state.copy_status = "Copy Summary to Clipboard"  # copy btn

            except Exception as e:
                st.error(f"An error occurred: {e}")
                st.warning("We couldn't generate the summary. Please try again later.")
        else:
            st.warning("The uploaded document does not contain any text.")

    # session suru asel tr
    if 'generated_summary' in st.session_state:
        st.subheader("Your Generated Summary:")
        summary_text_area = st.text_area("Generated Summary:", st.session_state.generated_summary, height=200, key="summary_content")

        #dwnld btn
        if st.button("Download Summary"):
            save_summary_to_file(st.session_state.generated_summary)
            st.success("Summary saved as 'summary.txt'.")

        # Button to copy summary to clipboard
        copy_button = st.button(st.session_state.get('copy_status', "Copy Summary to Clipboard"), key="copy_button")

        if copy_button:
            # JavaScript code to copy the text and change button text
            st.write(f"""
                <script>
                function copyToClipboard() {{
                    var summaryContent = document.querySelector('#summary_content');
                    var range = document.createRange();
                    range.selectNode(summaryContent);
                    window.getSelection().removeAllRanges();  // Clear current selection
                    window.getSelection().addRange(range);  // Select the content
                    document.execCommand('copy');  // Copy the selected content
                    window.getSelection().removeAllRanges();  // Clear selection
                    document.getElementById('copy_button').innerText = 'COPIED';
                }}
                copyToClipboard();
                </script>
                """, unsafe_allow_html=True)
            st.session_state.copy_status = "COPIED"  # Update the button text to "COPIED"

    # Clear button to reset the application state
    if st.button("Clear All"):
        st.session_state.clear()  # Clear all session state

if __name__ == "__main__":
    main()
