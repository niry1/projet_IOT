from pyspark.sql import SparkSession
from pyspark.sql.functions import to_timestamp

spark = SparkSession.\
        builder.\
        appName("pyspark-notebook").\
        master("spark://spark-master:7077").\
        config("spark.executor.memory", "512m").\
        getOrCreate()

data = spark.read.csv(path="/hdfs/X46789_2018-01-19T05-37-42.612Z.csv", sep=";", header=True)

data = data.withColumn("dateHour",to_timestamp("dateHour"))

data.write.format("es").option("es.nodes.wan.only","true").option("es.nodes","elasticsearch").save("metrics_jems")