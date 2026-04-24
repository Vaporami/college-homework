import entities
def search_by_name(value, cursor):
    query = f"SELECT * FROM recipe WHERE name LIKE \"%{value}%\""
    cursor.execute(query)
    arr = []
    for row in cursor:
        arr.append(entities.Recipe(row[0], row[1], row[2], row[3]))
    return arr

def search_by_ingredient(value, cursor):
    query = f"SELECT DISTINCT r.* FROM recipe r INNER JOIN recipe_ingredient ri ON r.id = ri.recipe_id INNER JOIN ingredient i on ri.ingredient_id = i.id WHERE i.name = \"{value}\""
    cursor.execute(query)
    arr = []
    for row in cursor:
        arr.append(entities.Recipe(row[0], row[1], row[2], row[3]))
    return arr

def search_by_user(value, cursor):
    query = f"SELECT r.* FROM recipe r INNER JOIN user u ON r.user_id = u.id where u.login = \"{value}\""
    cursor.execute(query)
    arr = []
    for row in cursor:
        arr.append(entities.Recipe(row[0], row[1], row[2], row[3]))
    return arr
