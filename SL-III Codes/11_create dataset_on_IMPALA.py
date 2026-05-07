
# Creating Databases and Tables, Inserting Data, and Running Simple Queries Using Impala

# #Simulated Impala Output in VS Code JUST FOR REFERENCE 
# #ACTUAL CODE IN IMPALA IS BELOW
# #CODE IMPLEMENTATION
# #Step 1: Creating a Database – Creating a new database 
# # CREATE DATABASE test_db; 
# #Step 2: Creating a Table -- Creating a table within the created database
# # USE test_db; 
# #-- Switch to the created database
# # CREATE TABLE employees ( id INT, name STRING, age INT, department STRING ); 
# #Step 3: Inserting Data into the Table – Inserting some sample data into the table
# # INSERT INTO employees VALUES (1, 'Alice', 30, 'HR'); 
# # INSERT INTO employees VALUES (2, 'Bob', 35, 'Engineering'); 
# # INSERT INTO employees VALUES (3, 'Charlie', 40, 'Marketing');
# #Step 4: Querying Data -- Running a simple query to fetch all records from the table 
# # SELECT * FROM employees; 
# #-- Query to fetch employees from a specific department
#  # SELECT * FROM employees WHERE department = 'Engineering';
#  #Step 5: Dropping the Table and Database (Optional Cleanup) – Dropping the table and database (useful for cleanup) 
# # DROP TABLE employees; 
# # DROP DATABASE test_db;
# 


# Simulated Impala Output in VS Code JUST FOR REFERENCE 


##BELOW CODE IS TO JUST SHOW THE EXAMPLE OF THE QUERY OUTPUT USING IMPALA ( IMP:NOT FOR PRACTICAL USE)
def print_line():
    print("-" * 50)

print("[Impala] > CREATE DATABASE test_db;")
print("Query: CREATE DATABASE test_db")
print("Fetched 0 row(s) in 0.10s\n")

print("[Impala] > USE test_db;")
print("Query: USE test_db")
print("Fetched 0 row(s) in 0.01s\n")

print("[Impala] > CREATE TABLE employees (id INT, name STRING, age INT, department STRING);")
print("Query: CREATE TABLE employees")
print("Fetched 0 row(s) in 0.12s\n")

print("[Impala] > INSERT INTO employees VALUES (1, 'Alice', 30, 'HR');")
print("Inserted 1 row(s) in 0.20s")

print("[Impala] > INSERT INTO employees VALUES (2, 'Bob', 35, 'Engineering');")
print("Inserted 1 row(s) in 0.18s")

print("[Impala] > INSERT INTO employees VALUES (3, 'Charlie', 40, 'Marketing');")
print("Inserted 1 row(s) in 0.19s\n")

print("[Impala] > SELECT * FROM employees;")

print("+----+----------+-----+-------------+")
print("| id | name     | age | department  |")
print("+----+----------+-----+-------------+")
print("| 1  | Alice    | 30  | HR          |")
print("| 2  | Bob      | 35  | Engineering |")
print("| 3  | Charlie  | 40  | Marketing   |")
print("+----+----------+-----+-------------+")
print("Fetched 3 row(s) in 0.15s\n")

print("[Impala] > SELECT * FROM employees WHERE department = 'Engineering';")

print("+----+------+-----+-------------+")
print("| id | name | age | department  |")
print("+----+------+-----+-------------+")
print("| 2  | Bob  | 35  | Engineering |")
print("+----+------+-----+-------------+")
print("Fetched 1 row(s) in 0.10s\n")

print("[Impala] > DROP TABLE employees;")
print("Query: DROP TABLE employees")
print("Fetched 0 row(s) in 0.08s\n")

print("[Impala] > DROP DATABASE test_db;")
print("Query: DROP DATABASE test_db")
print("Fetched 0 row(s) in 0.09s")