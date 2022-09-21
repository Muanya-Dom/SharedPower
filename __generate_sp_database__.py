import sqlite3

# Sqlite Data Tyeps
#NULL. The value is a NULL value.
#INTEGER. The value is a signed integer, stored in 1, 2, 3, 4, 6, or 8 bytes depending on the magnitude of the value.
#REAL. The value is a floating point value, stored as an 8-byte IEEE floating point number.
#TEXT. The value is a text string, stored using the database encoding (UTF-8, UTF-16BE or UTF-16LE).
#BLOB. The value is a blob of data, stored exactly as it was input.

# Open database
# Creates database
conn = sqlite3.connect('SharedPower.db')
dbCursor = conn.cursor()

# Creates customer table
customer = '''CREATE TABLE IF NOT EXISTS customer(
            customer_id INTEGER,
            email TEXT,
            username TEXT,
            password TEXT
            )'''
dbCursor.execute(customer)

# Creates tools table
tools = '''CREATE TABLE IF NOT EXISTS tool(
            serial_no INTEGER,
            tool_name TEXT,
            tool_category TEXT,
            per_day_rate REAL,
            half_day_rate REAL
            )'''
dbCursor.execute(tools)

# Creates hired tools table
hiredTools = '''CREATE TABLE IF NOT EXISTS hiredTool(
            order_no INTEGER,
            customer_id INTEGER,
            serial_no INTEGER,
            tool_name TEXT,
            cost REAL,
            no_of_days INTEGER,
            date_of_hire TEXT,
            insurance TEXT
            )'''
dbCursor.execute(hiredTools)


# Creates returned tools table
returnedTools = '''CREATE TABLE IF NOT EXISTS returnedTool(
            return_no INTEGER,
            customer_id INTEGER,
            serial_no INTEGER,
            tool_name TEXT,
            date_of_return TEXT,
            days_used INTEGER,
            status TEXT
            )'''
dbCursor.execute(returnedTools)


# Insert data into customer table
dbCursor.execute("INSERT INTO customer VALUES(1909129, 'chimuanya.umeh@email.com', 'Dominic', '1909129')")


# Insert data into tools table
dbCursor.execute("INSERT INTO tool VALUES(67457, 'Stanley Vs Wrench', 'Wrenches', 4, 2)")
dbCursor.execute("INSERT INTO tool VALUES(79898, 'C.K Wire Stripper', 'Cutters', 6, 3)")
dbCursor.execute("INSERT INTO tool VALUES(12343, 'Bosch GSB 18 V-50', 'Drills', 10, 5)")
dbCursor.execute("INSERT INTO tool VALUES(90898, 'Stanley Fibre Claw', 'Hammers', 2, 1)")
dbCursor.execute("INSERT INTO tool VALUES(45566, 'Magnusson Clamp', 'Clamps', 8, 4)")


# Insert data into hiredTools table
dbCursor.execute("INSERT INTO hiredTool VALUES(12133, NULL, NULL, NULL, NULL, NULL, NULL, NULL)")

# Insert data into hiredTools table
dbCursor.execute("INSERT INTO returnedTool VALUES(73487, NULL, NULL, NULL, NULL, NULL, NULL)")

# Final step in insert
conn.commit()

# Close database
dbCursor.close()
conn.close()






