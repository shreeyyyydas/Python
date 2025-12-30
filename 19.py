import sqlite3

# Step 1: Connect to MySQL
try:
    conn = mysql.connector.connect(
        host="localhost",       # or use your host, e.g., "127.0.0.1"
        user="root",            # your MySQL username
        password="nik@123N",  # your MySQL password
        database="kay"      # your database name
    )

    cursor = conn.cursor()

    # Step 2: Create a table (if not exists)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(100),
            age INT
        )
    """)

    # Step 3: Insert data
    name = input("Enter name: ")
    age = int(input("Enter age: "))

    insert_query = "INSERT INTO users (name, age) VALUES (%s, %s)"
    values = (name, age)

    cursor.execute(insert_query, values)
    conn.commit()  # Save changes

    print("✅ Data inserted successfully!")

except mysql.connector.Error as err:
    print("❌ Error:", err)

finally:
    if conn.is_connected():
        cursor.close()
        conn.close()
        print("🔌 Connection closed.")
