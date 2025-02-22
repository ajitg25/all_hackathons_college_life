FROM python:3.7-alpine3.16

WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
EXPOSE 8889
CMD python ./main.py
 