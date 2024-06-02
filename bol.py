import pandas as pd

judge_2022_standard = pd.read_csv('bas.csv')
pitch_type_mapping = {
    'FF': 'Four-Seam Fastball',
    'SL': 'Slider',
    'SI': 'Sinker',
    'CH': 'Changeup',
    'FC': 'Cutter',
    'CU': 'Curveball',
    'ST': 'Sweeper',
    'FS': 'Splitter',
    'KC': 'Knuckle-curve',
    'SV': 'Slurve',
    'FA': 'Fastball',
    'EP': 'Eephus'
}

# Replace the acronym pitch types with their complete names in the 'pitch_type' column
judge_2022_standard['pitch'] = judge_2022_standard['pitch'].replace(pitch_type_mapping)

# Read the CSV file into a pandas DataFrame
judge_2022_standard = judge_2022_standard.replace('�', '', regex=True)
filas_con_vacios = judge_2022_standard[judge_2022_standard['ev'] == '--']
judge_2022_standard.loc[filas_con_vacios.index, ['pitch_result', 'pa_result']] = judge_2022_standard.loc[filas_con_vacios.index, ['pa_result', 'pitch_result']].values
judge_2022_standard.loc[filas_con_vacios.index, ['pitch_result', 'inning']] = judge_2022_standard.loc[filas_con_vacios.index, ['inning', 'pitch_result']].values
judge_2022_standard.loc[filas_con_vacios.index, ['inning', 'count']] = judge_2022_standard.loc[filas_con_vacios.index, ['count', 'inning']].values
judge_2022_standard.loc[filas_con_vacios.index, ['count', 'distance']] = judge_2022_standard.loc[filas_con_vacios.index, ['distance', 'count']].values
judge_2022_standard.to_csv('j_2022.csv', index=False)