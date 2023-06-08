import pandas as pd




df = pd.read_csv('stats.csv')
df = df.drop(['player_id', 'Unnamed: 30'], axis=1)  # Drop the specified columns
df['name'] = df['first_name'].str.cat(df['last_name'], sep=' ')

# Remove the 'first_name' and 'last_name' columns
df = df.drop(['first_name', 'last_name'], axis=1)
df['name'] = df['name'].str.strip()
cols = df.columns.tolist()
cols = ['name'] + [col for col in cols if col != 'name']
df = df[cols]

df.to_csv('2022_savant_stats.csv', index=False)
