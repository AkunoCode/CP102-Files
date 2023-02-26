import pandas as pd

# Create a DataFrame
df = pd.DataFrame({
    'Name': ['John', 'Emily', 'Alex', 'Sara', 'Max', 'Mike', 'Emma', 'Sophie', 'Oliver', 'Isaac'],
    'Age': [25, 31, 45, 28, 33, 38, 27, 43, 26, 30],
    'Gender': ['Male', 'Female', 'Male', 'Female', 'Male', 'Male', 'Female', 'Female', 'Male', 'Male'],
    'Occupation': ['Engineer', 'Data Scientist', 'Marketing Manager', 'Software Developer', 'Accountant', 'Marketing Manager', 'Data Scientist', 'Engineer', 'Accountant', 'Software Developer']
})

# Print the first few rows of the DataFrame
print(df.head())

# Print some summary statistics of the DataFrame
print(df.describe())

# Get a count of the number of occurrences of each gender
print(df['Gender'].value_counts())

# Get a count of the number of occurrences of each occupation, grouped by gender
print(df.groupby(['Gender'])['Occupation'].value_counts())

# Sort the DataFrame by age, in descending order
df = df.sort_values(['Age'], ascending=False)

# Get a subset of the DataFrame containing only individuals aged 30 or older
print(df[df['Age'] >= 30])

# Get the names of all individuals aged 30 or older
print(df.query('Age >= 30')['Name'])

# Get the mean age of individuals, grouped by gender
print(df.groupby(['Gender'])['Age'].mean())

# Create a pivot table showing the mean age for each combination of gender and occupation
pivot_table = pd.pivot_table(
    df, values='Age', index='Gender', columns='Occupation', aggfunc='mean')

# Replace missing values in the pivot table with zeros
print(pivot_table.fillna(0))
