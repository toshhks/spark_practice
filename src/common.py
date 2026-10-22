from pyspark.sql import SparkSession

spark = (
    SparkSession.builder
    .appName('Pagila')
    .config('spark.jars.packages', 'org.postgresql:postgresql:42.7.4')
    .getOrCreate()
)

URL = "jdbc:postgresql://localhost:5433/pagila"
PROPS = {
    'user': 'postgres',
    'password': '123456',
    'driver': 'org.postgresql.Driver'
}

def get_spark_session():
    return spark

def get_url():
    return URL

def get_props():
    return PROPS

def read_table(table_name):
    return spark.read.jdbc(url=URL, table=table_name, properties=PROPS)