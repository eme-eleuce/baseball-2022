import pandas as pd

new_row = {
    'name': 'Mike Trout', 
    'year': 2022,
    'home_run': 40,
    'k_percent': 28.0,
    'bb_percent': 10.0,
    'b_rbi': 0,
    'exit_velocity_avg': 91.5,
    'hard_hit_percent': 50.8,
    'pitch_count': 2105
}


df = pd.read_csv('savant_2022_batting_stats.csv')
df = df.drop(['player_id', 'Unnamed: 11'], axis=1)  # Drop the specified columns
df['name'] = df['first_name'].str.cat(df['last_name'], sep=' ')

# Remove the 'first_name' and 'last_name' columns
df = df.drop(['first_name', 'last_name'], axis=1)
df['name'] = df['name'].str.strip()
cols = df.columns.tolist()
cols = ['name'] + [col for col in cols if col != 'name']
df = df[cols]
df = pd.concat([df, pd.DataFrame([new_row], columns=df.columns)], ignore_index=True)
df.to_csv('savant_2022_stats.csv', index=False)
