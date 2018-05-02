# File containing queries that will be used by API

#DEPRECATED

find_by_username = "SELECT * FROM users WHERE username = ?"
find_by_id = "SELECT * FROM users WHERE id = ?"
create_user_table = "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT, username text, password text)"
create_item_table = "CREATE TABLE IF NOT EXISTS item_model (name text, description text, traduction text)"
insert_user = "INSERT INTO users ( username, password) VALUES ( ?, ?)"
insert_item = "INSERT INTO items (nome, description, traduction) VALUES (?, ?, ?)"
delete_item = "DELETE FROM items WHERE nome = ?"
find_item = "SELECT * FROM items WHERE nome = ?"
find_all_items = "SELECT * FROM items"
update_item = "UPDATE items SET description = ? , traduction = ? WHERE name = ?"
