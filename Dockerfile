# syntax=docker/dockerfile:1
FROM python:3.10.12-bookworm

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install TeXLive and latexmk
RUN apt-get update
RUN apt-get install -y latexmk
RUN apt-get install -y texlive-latex-extra

# Copy necessary files
COPY app.py app.py
COPY requirements.txt requirements.txt
COPY .latexmkrc .latexmkrc

# Install Python dependencies
RUN pip3 install -r requirements.txt

# Install Gunicorn
RUN pip3 install gunicorn

# Create a directory for Gunicorn logs (production).
RUN mkdir -p /logs

# Allow the user to specify the port for the server.
ARG LATEX_PORT=32769

# Expose the port on which the server will run
EXPOSE $LATEX_PORT

# Set the environment variable for Flask
ENV FLASK_APP=app.py
ENV FLASK_RUN_PORT=$LATEX_PORT


# Run the Flask server
CMD ["flask", "run", "--host=0.0.0.0"]