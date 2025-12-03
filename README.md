create a streamlit website 
allow user to enter size of house in text box
after user clicks button named predict
and using the machine learning model stored in pickle format in the file linear_regression_house_price_prediction.pkl make the prediction and display on website

# install Docker desktop
# Create docker file


To build and run your Docker container using the provided Dockerfile, follow these steps:

Navigate to the directory containing your Dockerfile: Open your terminal or command prompt and navigate to the directory where your Dockerfile is located.


cd path/to/your/project

Build the Docker image: Use the docker build command to create a Docker image from your Dockerfile. Replace your-image-name with a name for your Docker image.


docker build -t your-image-name .

Run the Docker container: Use the docker run command to start a new container from your image. Replace your-container-name with a name for your container.


docker run -p 8501:8501 --name your-container-name your-image-name


This command maps port 8501 on your local machine to port 8501 in the container, allowing you to access the Streamlit app in your browser at http://localhost:8501.

Verify the Streamlit app: Open your web browser and navigate to http://localhost:8501 to verify that your Streamlit app is running correctly.

Here is a summary of the commands you need to run:


cd path/to/your/project
docker build -t your-image-name .
docker run -p 8501:8501 --name your-container-name your-image-name
