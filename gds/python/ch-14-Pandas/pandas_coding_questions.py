
import pandas as pd
import numpy as np

# Question 1:
# Create a Pandas DataFrame from a dictionary where keys are column names and values are lists of column data.
# The dictionary should have at least 3 columns and 5 rows.

data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Age': [25, 30, 35, 40, 45],
    'Salary': [50000, 60000, 70000, 80000, 90000]
}
df = pd.DataFrame(data)
print("DataFrame:\n", df)

# Question 2:
# Select and print the 'Age' column from the DataFrame created in Question 1.

age_column = df['Age']
print("Age column:\n", age_column)

# Question 3:
# Filter and print rows where the 'Salary' is greater than 60,000 from the DataFrame.

high_salary = df[df['Salary'] > 60000]
print("Rows with Salary > 60,000:\n", high_salary)

# Question 4:
# Add a new column 'Department' with values ['HR', 'IT', 'Finance', 'Marketing', 'Operations'] to the DataFrame.

df['Department'] = ['HR', 'IT', 'Finance', 'Marketing', 'Operations']
print("DataFrame with Department column:\n", df)

# Question 5:
# Sort the DataFrame by the 'Age' column in descending order and print the result.

sorted_df = df.sort_values(by='Age', ascending=False)
print("DataFrame sorted by Age (descending):\n", sorted_df)

# Question 6:
# Calculate and print the mean age from the DataFrame.

mean_age = df['Age'].mean()
print("Mean Age:", mean_age)

# Question 7:
# Create a new DataFrame with random values, having 4 rows and 3 columns.
# Name the columns 'A', 'B', and 'C'.

random_df = pd.DataFrame(np.random.rand(4, 3), columns=['A', 'B', 'C'])
print("Random DataFrame:\n", random_df)

# Question 8:
# Concatenate the original DataFrame with the new random DataFrame created in Question 7.

concatenated_df = pd.concat([df, random_df], ignore_index=True)
print("Concatenated DataFrame:\n", concatenated_df)

# Question 9:
# Remove the 'Department' column from the original DataFrame and print the result.

df_no_department = df.drop(columns='Department')
print("DataFrame without Department column:\n", df_no_department)

# Question 10:
# Calculate the sum of all numeric columns in the DataFrame and print the result.

column_sums = df_no_department.sum()
print("Sum of numeric columns:\n", column_sums)

# Question 11:
# Create a DataFrame from a CSV file 'sample_data.csv'. Print the first 5 rows.
# Assume the CSV file exists in the same directory.

# df_csv = pd.read_csv('sample_data.csv')
# print("First 5 rows of the CSV DataFrame:\n", df_csv.head())

# Question 12:
# Group the original DataFrame by the 'Department' column and calculate the average salary for each department.

department_avg_salary = df.groupby('Department')['Salary'].mean()
print("Average Salary by Department:\n", department_avg_salary)

# Question 13:
# Replace missing values in the DataFrame with the column mean.

df_with_nan = df.copy()
df_with_nan.loc[1, 'Age'] = np.nan  # Introduce a NaN value for demonstration
df_filled = df_with_nan.fillna(df_with_nan.mean(numeric_only=True))
print("DataFrame with NaNs filled by column mean:\n", df_filled)

# Question 14:
# Create a pivot table from the DataFrame showing the sum of 'Salary' for each 'Department' and 'Age' group.

pivot_table = df.pivot_table(values='Salary', index='Department', columns='Age', aggfunc='sum', fill_value=0)
print("Pivot Table:\n", pivot_table)

# Question 15:
# Add a column 'Bonus' to the DataFrame, calculated as 10% of the 'Salary'.

df['Bonus'] = df['Salary'] * 0.1
print("DataFrame with Bonus column:\n", df)

# Question 16:
# Convert the 'Name' column to uppercase in the DataFrame.

df['Name'] = df['Name'].str.upper()
print("DataFrame with Names in uppercase:\n", df)

# Question 17:
# Use the 'apply' method to create a new column 'Net Salary' calculated as 'Salary' plus 'Bonus'.

df['Net Salary'] = df.apply(lambda row: row['Salary'] + row['Bonus'], axis=1)
print("DataFrame with Net Salary column:\n", df)

# Question 18:
# Drop rows from the DataFrame where any element is missing (NaN) and print the result.

df_dropped_na = df.dropna()
print("DataFrame with dropped NaN rows:\n", df_dropped_na)

# Question 19:
# Create a date range with 10 consecutive days starting from today and add it as a new column 'Date' to the DataFrame.

date_range = pd.date_range(start=pd.Timestamp.today(), periods=10, freq='D')
df['Date'] = date_range[:len(df)]
print("DataFrame with Date column:\n", df)

# Question 20:
# Create a DataFrame that shows the cumulative sum of 'Salary' and 'Bonus' for each row.

df['Cumulative Salary'] = df['Salary'].cumsum()
df['Cumulative Bonus'] = df['Bonus'].cumsum()
print("DataFrame with cumulative sums:\n", df)

# Complex Question 21:
# For the original DataFrame, calculate the rolling average of the 'Salary' column with a window size of 2 and print the result.

rolling_avg_salary = df['Salary'].rolling(window=2).mean()
print("Rolling average of Salary with window size 2:\n", rolling_avg_salary)

# Complex Question 22:
# Find the correlation matrix of the DataFrame containing 'Age', 'Salary', and 'Bonus', and print it.

correlation_matrix = df[['Age', 'Salary', 'Bonus']].corr()
print("Correlation matrix:\n", correlation_matrix)

# Complex Question 23:
# Write a function to normalize each numeric column in the DataFrame and return a new DataFrame with normalized values.

def normalize_dataframe(dataframe):
    return (dataframe - dataframe.mean(numeric_only=True)) / dataframe.std(numeric_only=True)

normalized_df = normalize_dataframe(df[['Age', 'Salary', 'Bonus']])
print("Normalized DataFrame:\n", normalized_df)

# Complex Question 24:
# Merge the original DataFrame with another DataFrame on a common key (e.g., 'Department') and print the result.

other_data = {
    'Department': ['HR', 'IT', 'Finance', 'Marketing', 'Operations'],
    'Location': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix']
}
other_df = pd.DataFrame(other_data)
merged_df = pd.merge(df, other_df, on='Department')
print("Merged DataFrame:\n", merged_df)

# Complex Question 25:
# Create a DataFrame with hierarchical indexing (multi-index) and demonstrate selecting data using both levels of the index.

multi_index_data = {
    'Data': [10, 20, 30, 40, 50]
}
multi_index = pd.MultiIndex.from_tuples([('A', 1), ('A', 2), ('B', 1), ('B', 2), ('C', 1)], names=['Letter', 'Number'])
multi_index_df = pd.DataFrame(multi_index_data, index=multi_index)
print("Multi-index DataFrame:\n", multi_index_df)
print("Select data for Letter 'A':\n", multi_index_df.loc['A'])
print("Select data for Number '1':\n", multi_index_df.xs(1, level='Number'))
