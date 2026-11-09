from pyspark.sql.functions import col, desc, lower, round, sum, unix_timestamp
from common import read_table

city = read_table('city')
address = read_table('address')
customer = read_table('customer')
rental = read_table('rental')
inventory = read_table('inventory')
film_category = read_table('film_category')
category = read_table('category')

rental_hours = (
    city.join(address, on='city_id', how='inner')
    .join(customer, on='address_id', how='inner')
    .join(rental, on='customer_id', how='inner')
    .join(inventory, on='inventory_id', how='inner')
    .join(film_category, on='film_id', how='inner')
    .join(category, on='category_id', how='inner')
    .filter(col('return_date').isNotNull())
    .withColumn(
        'rental_hours',
        (unix_timestamp('return_date') - unix_timestamp('rental_date')) / 3600,
    )
    .select('city', col('name').alias('category'), 'rental_hours')
    .cache()
)


def top_category(city_filter):
    return (
        rental_hours.filter(city_filter)
        .groupBy('category')
        .agg(round(sum('rental_hours'), 2).alias('total_rental_hours'))
        .orderBy(desc('total_rental_hours'))
        .limit(1)
    )


cities_starting_with_a = top_category(lower(col('city')).startswith('a'))
cities_with_dash = top_category(col('city').contains('-'))

cities_starting_with_a.show()
cities_with_dash.show()
