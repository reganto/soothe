# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster
WORKDIR /home/files/code/projects/tornado/soothe 
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .
CMD [ "python3","app.py", "--port=8000" ]
