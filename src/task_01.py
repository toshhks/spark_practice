from pyspark.sql.functions import count, desc
from common import spark, read_table

category = read_table('category')
film_category = read_table('film_category')

result = (
    film_category.join(category, on='category_id', how='inner')
    .groupBy('name')
    .agg(count('film_id').alias('film_count'))
    .orderBy(desc('film_count'))
)

result.show()