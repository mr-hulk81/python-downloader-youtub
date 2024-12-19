# Use official Python image
FROM python:3.10

# Set working directory
WORKDIR /app

# Copy project files
COPY . /app

# copy cookies 
COPY ./cookies.txt /app/cookies.txt

# Install dependencies
RUN pip install --upgrade pip && pip install -r requirements.txt

# Create downloads folder
RUN mkdir -p /downloads

# Expose the directory for access
VOLUME /downloads

# Run the application
CMD ["python", "main.py"]
