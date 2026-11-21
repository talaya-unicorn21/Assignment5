
# Program Name: Assignment5.py
# Course: IT3883/Section W01
# Student Name: Talaya Jones
# Assignment Number: Lab 5
# Due Date: 11/20/2026
# Purpose: This program reads temperature records from a text file,
# stores the information in a SQLite database, and calculates the
# average temperatures for Sunday and Thursday.
# Resources Used: Course assignment instructions, Python sqlite3
# documentation, and ChatGPT for help understanding the assignment.

import sqlite3
# Connect to the database. SQLite creates it if it does not exist.
connection = sqlite3.connect("temperatures.db")
cursor = connection.cursor()

# Create a table to store the temperature records.
cursor.execute("""
CREATE TABLE IF NOT EXISTS TemperatureReadings (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Day_Of_Week TEXT,
    Temperature_Value REAL
)
""")

# Read the temperature information from the input file.
with open("Assignment5input.txt", "r") as input_file:
    for line in input_file:
        information = line.split()

        # Separate the day from the temperature.
        day = information[0]
        temperature = float(information[1])

        # Insert each record into the database.
        cursor.execute(
            "INSERT INTO TemperatureReadings (Day_Of_Week, Temperature_Value) VALUES (?, ?)",
            (day, temperature)
        )

# Save the inserted records.
connection.commit()

# Calculate the average temperature for Sunday.
cursor.execute("""
SELECT AVG(Temperature_Value)
FROM TemperatureReadings
WHERE Day_Of_Week = 'Sunday'
""")
sunday_average = cursor.fetchone()[0]

# Calculate the average temperature for Thursday.
cursor.execute("""
SELECT AVG(Temperature_Value)
FROM TemperatureReadings
WHERE Day_Of_Week = 'Thursday'
""")
thursday_average = cursor.fetchone()[0]

# Display both averages.
print("Average temperature for Sunday:", round(sunday_average, 2))
print("Average temperature for Thursday:", round(thursday_average, 2))

# Close the database connection.
connection.close()
