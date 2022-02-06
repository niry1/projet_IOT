import pandas as pd
import glob
import json

from kafka import KafkaProducer
from kafka import KafkaConsumer

producer = KafkaProducer(bootstrap_servers = 'kafka:9092')

for file in glob.glob('/app/sample/*.csv'):
    print("traitement du fichier : " + file)
    data = pd.read_csv(file, sep=';')
    for row in data.to_dict('records'):
        producer.send('metrics_jems_kafka', json.dumps(str(row)).encode('utf-8'))
        producer.flush()
        print(row)