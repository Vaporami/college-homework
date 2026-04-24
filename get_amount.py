def get_amount(table, cursor):
    cursor.execute(f"SELECT * FROM {table}")
    amount = 0
    for row in cursor:
        amount += 1
    return amount
