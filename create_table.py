import sqlite3
import query

# simple version of the creation of the schema,table and the first user

#DEPRECATED

connection = sqlite3.connect('api.db')
cursor = connection.cursor()
cursor.execute(query.create_user_table)
cursor.execute(query.create_item_table)
connection.commit()
connection.close()