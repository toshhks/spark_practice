from common import spark, read_table

film = read_table('film')
inventory = read_table('inventory')

result = (
    film.join(inventory, on='film_id', how='left_anti')
    .select('title')
)

result.show()