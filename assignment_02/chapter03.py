import pandas as pd 
import datetime as dt

corps = ['aapl', 'amzn', 'fb', 'goog', 'nflx']
faang_df = pd.DataFrame()
for i in corps:
    temp_df = pd.read_csv(f'data/{i}.csv')
    temp_df['ticker'] = i
    faang_df = faang_df.append(temp_df)

faang_df.to_csv('data/faang.csv')
print('\nQuestion 2')
faang_df['date'] = pd.to_datetime(faang_df['date'])
faang_df['volume'] = faang_df['volume'].astype(int)
print(faang_df.dtypes)

print('\nQuestion 3')
print(faang_df.nsmallest(7, 'volume'))

print('\nQuestion 4')
laang_df = faang_df.melt(id_vars=['ticker','date'], value_vars=['open','high', 'low', 'close', 'volume'])
print(laang_df.head())

print('\nQuestion 5\nDepends on the nature of the problem, if we can fix it we do, else we drop it')

c19_df = pd.read_csv('data/covid19_cases.csv')
c19_df = c19_df.assign(date = lambda x: pd.to_datetime(x.dateRep)).set_index('date').replace({'United_States_of_America':'USA', "United_Kingdom":"UK"})
c19_filt = c19_df[c19_df.countriesAndTerritories.isin(['Argentina','Brazil','China','Colombia','India','Italy','Mexico','Peru','Russia','Spain','Turkey','UK','USA'])].reset_index().pivot(index='date', columns='countriesAndTerritories', values='cases').fillna(0)
print('\nQuestion 6\n',c19_filt.head())

agg_df = pd.read_csv('data/covid19_total_cases.csv', index_col='index').T.nlargest(20,'cases')
print('\nQuestion 7\n',agg_df)