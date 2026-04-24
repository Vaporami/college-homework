#!/home/vapori/programming/python/rkis/venv/bin/python3.11

import mariadb, search_recipe

from get_amount import get_amount
from export_to_csv import export_to_csv
from get_random_ingredients import get_random_ingredients

conn = mariadb.connect("mariadb://db:4231db@localhost/recipe")
cursor = conn.cursor()



amount = get_amount("ingredient", cursor)
print(f"Всего ингредиентов в базе данных: {amount}")
print()

print("Все рецепты, в названии которых есть слово \"блины\":")
recipes = search_recipe.search_by_name("блины", cursor)
for recipe in recipes:
    print(recipe.name)
    pass
print()

print("Все рецепты с луком: ")
recipes = search_recipe.search_by_ingredient("лук", cursor)
for recipe in recipes:
    print(recipe.name)
    pass
print()

print("Все рецепты, что принадлежат пользователю с логином \"katya_smile88\":")
recipes = search_recipe.search_by_user("katya_smile88", cursor)
for recipe in recipes:
    print(recipe.name)
    pass
print()

file_name = "test.csv"
print(f"Происходит экспорт в {file_name}...")
export_to_csv(recipes, file_name)
print()

print(f"Шесть случайных ингредиентов: {get_random_ingredients(6, cursor)}")



cursor.close()
conn.close()
