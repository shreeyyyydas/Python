import sqlite3

try:
    # Connect to SQLite database (create or open 'full.db')
    conn = sqlite3.connect("infosys")  # Use your actual database name here
    cursor = conn.cursor()
    
    print("Connected to the database!")

    # Ensure table 't' exists with proper schema
    create_table_query = '''
    CREATE TABLE IF NOT EXISTS tilu (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER NOT NULL
    );
    '''
    cursor.execute(create_table_query)
    conn.commit()

    # Get input from the user
    name = input("Enter name: ")
    age = int(input("Enter age: "))

    # Insert data into the table
    query = "INSERT INTO t(name, age) VALUES (?, ?)"
    values = (name, age)

    # Execute query
    cursor.execute(query, values)
    conn.commit()
    
    print("✅ Data inserted!")

except sqlite3.Error as e:
    print(f"Error: {e}")

finally:
    # Close connection
    if cursor:
        cursor.close()
    if conn:
        conn.close()
    print("🔌 Connection closed.")
