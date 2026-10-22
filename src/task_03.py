from pyspark.sql.functions import sum, desc
from common import read_table

payment = read_table('payment')
rental = read_table('rental')
inventory = read_table('inventory')
film_category = read_table('film_category')
category = read_table('category')

result = (
    payment.join(rental, on='rental_id', how='inner')
    .join(inventory, on='inventory_id', how='inner')
    .join(film_category, on='film_id', how='inner')
    .join(category, on='category_id', how='inner')
    .groupBy('category_id', 'name')
    .agg(sum('amount').alias('total_amount'))
    .orderBy(desc('total_amount'))
    .limit(1)
)

result.show()