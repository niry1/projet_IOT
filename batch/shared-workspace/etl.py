from pyspark.sql import SparkSession
from pyspark.sql.functions import to_timestamp

spark = SparkSession.\
        builder.\
        appName("pyspark-notebook").\
        master("spark://spark-master:7077").\
        config("spark.executor.memory", "512m").\
        getOrCreate()

data = spark.read.csv(path="/hdfs", sep=";", header=True)

data = data.withColumn("dateHour",to_timestamp("dateHour"))

data.write.format("es").option("es.nodes.wan.only","true").option("es.nodes","elasticsearch").save("metrics_jems_batch")