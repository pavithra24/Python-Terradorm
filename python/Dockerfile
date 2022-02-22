#using python-slim image to create light weight image
FROM python:3.8-slim

WORKDIR /app
COPY . /app

RUN pip3 install boto3

CMD ["python3", "s3_write.py", "qa"]
