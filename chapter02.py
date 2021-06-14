import datetime as dt
import numpy as np
import pandas as pd

df = pd.read_csv('data/parsed.csv')

df_Japan = df.loc[df.parsed_place.str.contains(r'Japan$') & df.magType.str.contains(r'mb')]
J95 = np.percentile(df_Japan.mag, 95)
print(f'Question 1: {J95}')

df_Indo = df.loc[df.parsed_place.str.contains(r'Indonesia$')]
print(f"Question 2: {df_Indo.loc[df_Indo['tsunami'] == 1,'tsunami'].sum()/df_Indo.shape[0]}")

df_Nev = df.loc[df.parsed_place.str.contains(r'Nevada|NV$')]
print("Question 3:")
print(df_Nev.describe())

df_add = df
df_add['RoF'] = df_add.parsed_place.str.contains(r'"Mexico"|Alaska|Antarctic|Bolivia|California|Canada|Chile|Costa Rica|Ecuador|Fiji|Guatamala|Indonesia|Japan|Kermadec Islands|New Zealand|Peru|Philippines|Russia|Taiwan|Tonga|Washington$')

print("Question 5: RoF = {df_add.loc[df_add['RoF'] == True, 'RoF'].sum()}")


#print(f'Question 2: {}')

