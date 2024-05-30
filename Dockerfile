# Use the official Python image from the Docker Hub
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

RUN pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu
RUN pip install transformers
RUN pip install flask

# Install any other needed packages specified in requirements.txt
# RUN pip install --no-cache-dir -r requirements.txt

# Run the specified Python script
CMD ["python", "run.py"]
