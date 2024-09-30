import pandas as pd

# Sample data to create a DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Age': [24, 30, 22, 35, 29],
    'Salary': [50000, 60000, 45000, 70000, 65000],
    'Department': ['HR', 'IT', 'HR', 'Finance', 'IT']
}

# Create DataFrame
df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

# 1. Get a list of the column headers
column_headers = df.columns.tolist()
print("\nColumn Headers:")
print(column_headers)

# 2. Delete a column by name
df.drop(columns=['Department'], inplace=True)
print("\nDataFrame after deleting 'Department' column:")
print(df)

# 3. Delete a column by index (e.g., index 1 which corresponds to 'Age')
df.drop(df.columns[1], axis=1, inplace=True)
print("\nDataFrame after deleting column at index 1:")
print(df)

# 4. Add a new column to the existing DataFrame
df['Location'] = ['New York', 'Los Angeles', 'Chicago', 'Houston']
print("\nDataFrame after adding new 'Location' column:")
print(df)
