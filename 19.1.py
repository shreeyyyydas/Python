import sqlite3

# Connect to MySQL
conn = sqlite3.connect(
        database="nay"       # Replace with your database name
)

cursor = conn.cursor()
print("Connected to MySQL!")
"""# Get input from user
name = input("Enter name: ")
age = int(input("Enter age: "))

# Insert data
query = "INSERT INTO t(name, age) VALUES (?,?)"
values = (name, age)

cursor.execute(query, values)
conn.commit()
print("✅ Data inserted!")

# Close connection
cursor.close()
conn.close()
print("🔌 Connection closed.")"""
query="SELECT * FROM niy"
cursor.execute(query)
rows=cursor.fetchall()
for row in rows:
    print (row)

cursor.close()
conn.close()
