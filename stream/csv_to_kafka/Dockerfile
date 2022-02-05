FROM python:3.6-slim
WORKDIR /app/
COPY requirements.txt csv_to_kafka.py ./
COPY sample ./sample
RUN pip install -r requirements.txt
# ENTRYPOINT python csv_to_kafka.py
ENTRYPOINT [ "tail","-f", "/dev/null" ]