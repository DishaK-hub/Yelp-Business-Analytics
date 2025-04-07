#!/usr/bin/python
from pyspark.sql import SparkSession

spark = SparkSession \
            .builder \
            .master('yarn') \
            .appName('Yelp') \
            .getOrCreate()

# Use the Cloud Storage bucket for temporary BigQuery export data used
# by the connector.
bucket = "final_project3033"
spark.conf.set('temporaryGcsBucket', bucket)

# Load data from BigQuery.
businesses = spark.read.format('bigquery') \
        .option('table', 'firstproject-436502.yelp.businesses') \
        .load()
businesses.createOrReplaceTempView('businesses')

# Perform word count.
businesses_query = spark.sql(
    'SELECT state AS state, SUM(review_count) as n_reviews FROM businesses GROUP BY state ORDER BY n_reviews DESC'
)
businesses_query.show()
businesses_query.printSchema()

# Saving the data to BigQuery
businesses_query.write.format('bigquery') \
    .option('table', 'firstproject-436502.yelp.business_state_reviews') \
    .mode('overwrite') \
    .save()

spark.stop()
