from pyspark.sql.functions import lower, col, unix_timestamp, sum, desc
from common import read_table

city = read_table('city').filter(lower(col('city')).startswith('a') | col('city').contains('-'))

address = read_table('address')
customer = read_table('customer')
rental = read_table('rental')
inventory = read_table('inventory')
film_category = read_table('film_category')
category = read_table('category')

result = (
    customer.join(address, on='address_id', how='inner')
    .join(city, on='city_id', how='inner')
    .join(rental, on='customer_id', how='inner')
    .join(inventory, on='inventory_id', how='inner')
    .join(film_category, on='film_id', how='inner')
    .join(category, on='category_id', how='inner')
    .withColumn('rental_duration', (unix_timestamp('return_date') - unix_timestamp('rental_date')) / 3600)
    .groupBy('category_id', 'name')
    .agg(sum('rental_duration').alias('total_rental_duration'))
    .orderBy(desc('total_rental_duration'))
    .limit(1)
)

result.show()