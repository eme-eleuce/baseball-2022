import pandas as pd

csv_encoding = 'latin-1'

# Read the CSV file
df = pd.read_csv('riley_daily_stats.csv', encoding=csv_encoding)

# Remove the '�' symbol from all columns
df = df.replace('�', '', regex=True)
# Remove rows with incomplete date information 
df = df[df['Date'].str.contains('/')]

df['Date'] = pd.to_datetime(df['Date'], format='%d/%m/%Y')

# Add a new column with the day of the week
df['day_of_week'] = df['Date'].dt.day_name()

def add_zeros(x):
    if pd.notnull(x):
        if isinstance(x, str):
            if len(x) == 3:  # Incomplete number with one decimal (e.g., 0.1)
                return '0.00' + x[-1]
            elif len(x) == 4:  # Incomplete number with two decimals (e.g., 0.40)
                return '0.0' + x[-2:]
        elif isinstance(x, float):
            return format(x, '.3f')
    return x

# Apply the function to the specified columns
columns_to_modify = ['AVG', 'OBP', 'OPS', 'SLG']
df[columns_to_modify] = df[columns_to_modify].applymap(add_zeros)
# Save the cleaned data to a new CSV file
df.to_csv('riley_2022_daily_stats.csv', index=False)