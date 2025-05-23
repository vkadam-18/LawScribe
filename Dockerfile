# Use the official Python image as a base image
FROM python:3.12-slim

# Set the working directory in the container
WORKDIR /app

# Copy the application files to the container
COPY . /app

# Install required Python packages
RUN pip install --no-cache-dir streamlit PyPDF2 python-docx google-generativeai

# Expose the port that Streamlit will run on
EXPOSE 8501

# Run the Streamlit app
CMD ["streamlit", "run", "app.py", "--server.headless=true", "--server.port=8501"]
