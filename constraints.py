import sqlite3
#connect to sqlite database (or create is not exists)
conn=sqlite3.connect('ff1.db')
cursor=conn.cursor()
#create products table
cursor.execute('''CREATE TABLE  products(
    product_id INTEGER PRIMARY KEY ,
    product_name TEXT NOT NULL     
);''')
#create orders table with foreign key constraint
cursor.execute('''CREATE TABLE orders(
    order_id INTEGER PRIMARY KEY,
    product_id INTEGER NOT NULL,
    quantity INTEGER NOT NULL,
    FOREIGN KEY (product_id) REFERENCES products(product_id)
);''')
#insert sample data into products table
cursor.execute('''INSERT INTO products (product_id,product_name) VALUES (1,'Product A');''')
cursor.execute('''INSERT INTO products (product_id,product_name) VALUES (2,'Product B');''')
#insert sample data into orders table
cursor.execute('''INSERT INTO orders (order_id,product_id,quantity) VALUES (101,1,10);''')
cursor.execute('''INSERT INTO orders (order_id,product_id,quantity) VALUES (102,2,5);''')
#fetch data using join query
cursor.execute('''SELECT orders.order_id, products.product_name, orders.quantity 
                  FROM orders INNER JOIN products ON 
                  orders.product_id = products.product_id;''')
#display fetched data
rows=cursor.fetchall()
for row in rows:
    print(row)