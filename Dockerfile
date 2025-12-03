# name of official docker image on docker hub with python installed
FROM python:3

# Set the working directory in the container
WORKDIR /app

# Copy the requirements.txt file to the working directory
COPY requirements.txt .

# Install the required Python packages
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code to the working directory
COPY . .

# Expose the port that streamlit uses (default = 8501)
EXPOSE 8501

# Run the streamlit app
CMD ["streamlit", "run", "main.py"]

#Interminal Command to build the docker image
# docker build -t app name . (full stop is must)

#To run the docker image
# docker run -p 8501:8501 app name