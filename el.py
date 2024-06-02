import pandas as pd

arraez = pd.read_csv('savant_data.csv')

arraez['count'] = arraez['balls'].astype(str) + '-' + arraez['strikes'].astype(str)
arraez.drop('pitch_type', axis=1, inplace=True)
# Move the "pitch_name" column to the first position
cols = arraez.columns.tolist()
cols.insert(0, cols.pop(cols.index('pitch_name')))
df = arraez[cols]
# Print the updated DataFrame
df.to_csv('arraez-2022.csv', index=False)