FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY generate_report.py .
ENV HUGGING_FACE_MODEL_HUB=https://huggingface.co/models
ENV REPORT_INTERVAL=3600  
# Set the number of top models to report
ENV TOP_MODELS=10
# Run the report generation script
CMD ["python", "generate_report.py"]
