FROM python:3.8-buster

# Copy the requirements.txt file to our Docker image
COPY requirements.txt .

# Install the requirements.txt
RUN pip install -r requirements.txt

COPY app.py .

COPY model.h5 .

COPY token.pkl .

# Inform Docker that the container is listening on the specified port at runtime.

# Run the specified command within the container.
CMD [ "python", "./app.py" ]