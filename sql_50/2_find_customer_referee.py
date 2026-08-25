import sqlite3

# Create/connect to database
conn = sqlite3.connect("leetcode.db")
cursor = conn.cursor()

# Create Customer table
cursor.execute("""
CREATE TABLE IF NOT EXISTS Customer (
    id INTEGER PRIMARY KEY,
    name TEXT,
    referee_id INTEGER
)
""")

# Clear old data so repeated runs don't duplicate rows
cursor.execute("DELETE FROM Customer")

# Insert sample data
customers = [
    (1, "Will", None),
    (2, "Jane", None),
    (3, "Alex", 2),
    (4, "Bill", None),
    (5, "Zack", 1),
    (6, "Mark", 2)
]

cursor.executemany(
    "INSERT INTO Customer (id, name, referee_id) VALUES (?, ?, ?)",
    customers
)

# Your LeetCode SQL query
query = """
SELECT name
FROM Customer
WHERE referee_id != 2
   OR referee_id IS NULL;
"""

# Execute query
cursor.execute(query)

# Print results
results = cursor.fetchall()

print("Customers:")
for row in results:
    print(row[0])

# Save changes and close
conn.commit()
conn.close()