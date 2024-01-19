# Number of rows and columns in the table
num_rows = 5
num_columns = 5

# Display the table using nested loops
for i in range(1, num_rows + 1):
    row = ""
    for j in range(1, num_columns + 1):
        row += f"{i ** j:3}  "  # Format each element in the row
    print(row)
