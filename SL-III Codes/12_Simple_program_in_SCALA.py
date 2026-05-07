
# Write a Simple Program in Scala Using Apache Spark Framework
# 
# # CODE IMPLEMENTATION
# # Step 1: Set up your Spark Application 
# import org.apache.spark.sql.SparkSession
# object SparkExample {
#   def main(args: Array[String]): Unit = {
# # Step 1: Initialize Spark Session
#     val spark = SparkSession.builder()
#       .appName("Simple Spark Program")
#       .master("local")
#       .getOrCreate()
# # Step 2: Load data from a CSV file into a DataFrame
#  val df = spark.read.option("header", "true").csv("people.csv")
# # Step 3: Show the first few rows of the DataFrame
#     df.show()
# # Step 4: Perform a simple transformation and action
#     val filtered = df.filter($"age" > 30).select("name", "age")
#     println("Filtered Data:")
# # Step 5: Show the filtered results
#     filtered.show()
# # Step 6: Group by and Aggregate Data 
#     val avgAge = df.groupBy("department").avg("age")
#     println("Average Age:")
#     avgAge.show()
# # Stop the Spark session
#     spark.stop()
#   }
# }
# 


#code for the references
from pyspark.sql import SparkSession

# Start Spark
spark = SparkSession.builder.appName("Simple Spark Program").getOrCreate()

# Create Data
data = [
    ("Alice", 30, "HR"),
    ("Bob", 35, "Engineering"),
    ("Charlie", 40, "Marketing"),
    ("David", 28, "Engineering"),
    ("Eve", 45, "HR")
]

# Create DataFrame
df = spark.createDataFrame(data, ["name", "age", "department"])

# Show Original Data
print("Original Data:")
df.show()

# Filter
filtered = df.filter(df.age > 30).select("name", "age")
print("Filtered Data:")
filtered.show()

# Aggregation
avgAge = df.groupBy("department").avg("age")
print("Average Age:")
avgAge.show()

# Stop Spark
spark.stop()