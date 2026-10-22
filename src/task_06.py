from pyspark.sql.functions import count, when, desc, col
from common import read_table

customer = read_table('customer')
address = read_table('address')
city = read_table('city')

result = (
    customer.join(address, on='address_id', how='inner')
    .join(city, on='city_id', how='inner')
    .groupBy('city_id', 'city')
    .agg(
        count(when(col('active') == 1, True)).alias('active_customers'),
        count(when(col('active') == 0, True)).alias('inactive_customers'),
    )
    .orderBy(desc('inactive_customers'))
    )

result.show()