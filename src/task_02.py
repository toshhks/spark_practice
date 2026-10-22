from pyspark.sql.functions import count, desc
from common import read_table

rental = read_table('rental')
inventory = read_table('inventory')
film_actor = read_table('film_actor')
actor = read_table('actor')

result = (
    rental.join(inventory, on='inventory_id', how='inner')
    .join(film_actor, on='film_id', how='inner')
    .join(actor, on='actor_id', how='inner')
    .groupBy('actor_id', 'first_name', 'last_name')
    .agg(count('rental_id').alias('rental_count'))
    .orderBy(desc('rental_count'))
    .limit(10)
)

result.show()