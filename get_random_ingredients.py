from get_amount import get_amount
from random import randint

def get_random_ingredients(amount, cursor):
    query = "SELECT * FROM ingredient ORDER BY id"
    cursor.execute(query)
    rows = cursor.fetchall()
    arr = []
    ingredients_amount = get_amount("ingredient", cursor)
    offset = 1
    for i in range(amount):
        id = randint(0, ingredients_amount - offset)
        arr.append(rows[id][1])
        offset += 1
        rows.append(rows.pop(id))
    return arr
