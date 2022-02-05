FROM python:3.9.10-alpine3.15
WORKDIR /app/
COPY requirements.txt elastic_init.py ./
USER root
RUN pip install -r requirements.txt
ENTRYPOINT python elastic_init.py