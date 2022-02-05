import pandas as pd
import glob
import json

from kafka import KafkaProducer

def row_to_kafka(data,producer):
    data_dict = data.to_dict(orient="records")
    for row in data_dict:
        producer.send(b"metrics_changerv1",str(row))

producer = KafkaProducer(bootstrap_servers='kafka:9092',value_serializer =lambda x:json.dumps(x).encode("utf-8"))

for file in glob.glob("/app/sample/*.csv"):
    data = pd.read_csv(file, sep=";")
    for row in data.to_dict("records"):
        producer.send(b"metrics_changerv1",str(row))