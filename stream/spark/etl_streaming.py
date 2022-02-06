from pyspark import SparkContext
from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils

sc = SparkContext(appName="Kafka_to_Elasticsearch")
ssc = StreamingContext(sc,60)
message = KafkaUtils.createDirectStream(ssc,topics=["metrics_jems_kafka"],kafkaParams={"bootstrap.servers":"kafka:9092"})
