# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set the working directory to /app
WORKDIR /app
# Install any needed packages specified in requirements.txt
RUN pip install --upgrade pip
COPY requirements.txt .
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Define environment variable
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTONUNBUFFERED 1

COPY /docker-entrypoint.sh /docker-entrypoint.sh
RUN chmod +x /docker-entrypoint.sh

# Copy the current directory contents into the container at /app
COPY . /app


