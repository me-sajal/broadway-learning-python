from estd_connection import estd_connection

cursor = estd_connection()

sql = """
CREATE TABLE STUDENT(
    ID CHAR(20),
    NAME CHAR(100),
    AGE INT
)
"""

cursor.execute(sql)
print("Table created successfully !!")