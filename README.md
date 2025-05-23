# LawScribe
Legal Document Summarizer using Python
# 🧾 Legal Document Summarizer

The **Legal Document Summarizer** is a cloud-native web application built using **Python** and **Streamlit** that enables users to generate concise summaries of legal documents in **PDF**, **DOCX**, or **TXT** formats. With the power of **Google’s Gemini API**, this app provides flexible summarization (Short, Medium, Long) tailored to user needs.

The application is containerized using **Docker** for consistency across environments and deployed on **AWS EC2** to leverage scalable and secure cloud infrastructure.

---

## 🚀 Project Overview

- **Frontend/UI**: Built using **Streamlit** for simplicity and responsiveness.
- **Backend**: Utilizes **Google Gemini API** for natural language processing and summarization.
- **Containerization**: Powered by **Docker** for portable deployment.
- **Deployment**: Hosted on **AWS EC2** for scalability and high availability.

This application is designed to simplify legal document analysis for legal professionals, researchers, and knowledge workers by combining powerful NLP with cloud-native engineering.

---

## ✨ Key Features

- ✅ **Flexible Summary Options**  
  Choose from Short, Medium, or Long summaries.

- 📄 **Multiple File Format Support**  
  Supports uploading of `.pdf`, `.docx`, and `.txt` files.

- 🔍 **Text Extraction and Preview**  
  Extract and preview document content before summarization.

- 💾 **Download & Copy**  
  Download the summary as a `.txt` file or copy it directly to clipboard.

- 🧑‍💻 **User-Friendly Interface**  
  Simple and responsive UI designed with Streamlit.

- 🐳 **Docker Deployment**  
  Includes a `Dockerfile` for streamlined, environment-independent deployment.

---

## ☁️ Prerequisites

### For EC2 Deployment

- **AWS Account**  
  Required to launch and manage an EC2 instance.

- **EC2 Security Group**  
  Allow inbound traffic on **port `8501`** (used by Streamlit).

- **SSH Access**  
  Ensure SSH access to the EC2 instance.

- **GitHub Repository**  
  Clone this project:
  ```bash
  git clone https://github.com/your-username/your-repository-url

