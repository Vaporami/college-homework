def get_amount(table, cursor):
    cursor.execute(f"SELECT * FROM {table}")
    a = 0
    for r in cursor:
        a += 1
    return a
