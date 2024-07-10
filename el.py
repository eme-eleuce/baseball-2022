import pandas as pd

arraez = pd.read_csv('arraez-full-2023.csv')

arraez['count'] = arraez['balls'].astype(str) + '-' + arraez['strikes'].astype(str)
arraez['pfx_z_inches'] = arraez['pfx_z'] * 12
arraez['pfx_x_inches'] = arraez['pfx_x'] * -12

arraez.drop('pitch_type', axis=1, inplace=True)
# Move the "pitch_name" column to the first position
cols = arraez.columns.tolist()
cols.insert(0, cols.pop(cols.index('pitch_name')))
df = arraez[cols]
# Print the updated DataFrame
df.to_csv('arraez-2023-last.csv', index=False)