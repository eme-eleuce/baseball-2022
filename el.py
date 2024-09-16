import pandas as pd

arraez = pd.read_csv('arraez-full-2023.csv')

arraez['count'] = arraez['balls'].astype(str) + '-' + arraez['strikes'].astype(str)
arraez['pfx_z_inches'] = arraez['pfx_z'] * 12
arraez['pfx_x_inches'] = arraez['pfx_x'] * -12
arraez['pitch_name'] = arraez['pitch_name'].str.replace('4-Seam Fastball', 'Four-Seam')

# Pitch Group:



# Launch Angle and Exit velocity:

launch_speed_angle_mapping = {
    1: 'Weak',
    2: 'Topped',
    3: 'Under',
    4: 'Flare/Burner',
    5: 'Solid Contact',
    6: 'Barrel'
}

# Replace the values in the 'launch_speed_angle' column
arraez['launch_speed_angle'] = arraez['launch_speed_angle'].map(launch_speed_angle_mapping)

# Launch angle regroup

def classify_launch_angle(launch_angle):
    if -90 <= launch_angle <= 0:
        return 'Topped'
    elif 1 <= launch_angle <= 7:
        return 'Burner'
    elif 8 <= launch_angle <= 32:
        return 'Sweet Spot'
    elif 33 <= launch_angle <= 39:
        return 'Flare'
    elif 40 <= launch_angle <= 90:
        return 'Under'
    else:
        return 'Other'

# Apply the classification to create the new column 'launch_angle_group'
arraez['launch_angle_group'] = arraez['launch_angle'].apply(classify_launch_angle)

arraez.drop('pitch_type', axis=1, inplace=True)
# Move the "pitch_name" column to the first position
cols = arraez.columns.tolist()
cols.insert(0, cols.pop(cols.index('pitch_name')))
df = arraez[cols]
# Print the updated DataFrame
df.to_csv('arraez-2023-last.csv', index=False)