import sqlite3

# Connect to database (creates practice.db if it doesn't exist)
conn = sqlite3.connect("practice.db")

# Create cursor
cursor = conn.cursor()


# Create Products table
cursor.execute("""
CREATE TABLE IF NOT EXISTS Products (
    product_id INTEGER PRIMARY KEY,
    low_fats TEXT,
    recyclable TEXT
)
""")


# Insert sample data
cursor.execute("""
INSERT OR REPLACE INTO Products (product_id, low_fats, recyclable)
VALUES
    (0, 'Y', 'N'),
    (1, 'Y', 'Y'),
    (2, 'N', 'Y'),
    (3, 'Y', 'Y'),
    (4, 'N', 'N')
""")


# Your SQL query
query = """
SELECT product_id
FROM Products
WHERE low_fats = 'Y'
AND recyclable = 'Y';
"""


# Execute query
cursor.execute(query)

# Get all results
results = cursor.fetchall()

# Print results
for row in results:
    print(row)


# Save and close database
conn.commit()
conn.close()