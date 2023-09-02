# syntax=docker/dockerfile:1
FROM python:3.10.12-bookworm

# Install TeXLive and latexmk
RUN apt-get update

RUN apt-get install -y latexmk

RUN apt-get install -y texlive-full

# Copy necessary files
COPY app.py app.py
COPY requirements.txt requirements.txt
COPY .latexmkrc .latexmkrc

# Install Python dependencies
RUN pip3 install -r requirements.txt

# Expose the port on which the Flask server will run
EXPOSE 5000

# Set the environment variable for Flask
ENV FLASK_APP=app.py

# Shows print logs from our server in the container logs.
ENV PYTHONUNBUFFERED=1

# Run the Flask server
CMD ["flask", "run", "--host=0.0.0.0"]