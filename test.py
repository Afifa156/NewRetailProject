from lib.Utils import get_spark_session

spark=get_spark_session("LOCAL")

schema = "state string,count int"
result_df = spark.read \
    .format("csv") \
    .schema(schema) \
    .option("header","true")\
    .load("data/test_results/sg.csv")
    
result_df.show()