from pyspark.sql.functions import col, count, desc, rank
from pyspark.sql.window import Window
from common import read_table

category = read_table('category').filter(col('name') == 'Children')
film_category = read_table('film_category')
film_actor = read_table('film_actor')
actor = read_table('actor')

window = Window.orderBy(desc('film_count'))

result = (
    category.join(film_category, on='category_id', how='inner')
    .join(film_actor, on='film_id', how='inner')
    .join(actor, on='actor_id', how='inner')
    .groupBy('actor_id', 'first_name', 'last_name')
    .agg(count('film_id').alias('film_count'))
    .withColumn('place', rank().over(window))
    .filter(col('place') <= 3)
    .orderBy(desc('film_count'))
)

result.show()
