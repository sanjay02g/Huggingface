Dockerfile:
The Dockerfile uses the latest Python 3.9 image.
It sets the working directory to /app.
It copies the requirements.txt file and installs the dependencies.
It copies the generate_report.py script.
It sets environment variables for the Hugging Face model hub, report interval, and number of top models.
It sets the command to run the generate_report.py script.
generate_report.py:
It fetches data from the Hugging Face model hub.
It generates a report by sorting the models by downloads and selecting the top models.
It runs the report generation script in an infinite loop with the specified interval.
requirements.txt:
It lists the dependencies required by the generate_report.py script.
