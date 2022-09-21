import sys
import sqlite3

# Opens database
conn = sqlite3.connect('SharedPower.db')
dbCursor = conn.cursor()


# Insert data in customer table
def toCustomerTable(customerId, email, username, password):
    dbCursor.execute("INSERT INTO customer VALUES(?, ?, ?, ?)", (customerId, email, username, password))

    # Final process in insertion
    conn.commit()



# Insert data in hired tool table
def toHiredToolTable(orderNo, customerId, serialNo, toolName, cost, noOfDays, dateOfHire, insurance):
    dbCursor.execute("INSERT INTO hiredTool VALUES(?, ?, ?, ?, ?, ?, ?, ?)",
                     (orderNo, customerId, serialNo, toolName, cost, noOfDays, dateOfHire, insurance))

    # Final process in insertion
    conn.commit()


# Insert data in returned tool table
def toReturnedToolTable(returnNo, customerId, serialNo, toolName, dateOfReturn, daysUsed, status):
    dbCursor.execute("INSERT INTO returnedTool VALUES(?, ?, ?, ?, ?, ?, ?)",
                     (returnNo, customerId, serialNo, toolName, dateOfReturn, daysUsed, status))

    # Final process in insertion
    conn.commit()



# Insert data in tool table
def insertToToolTable(serial_no , tool_name, tool_category, half_day_rate, per_day_rate):

    dbCursor.execute("INSERT INTO tool VALUES(?, ?, ?, ?, ?)",
                     (serial_no , tool_name, tool_category, half_day_rate, per_day_rate))

    # Final process in insertion
    conn.commit()
