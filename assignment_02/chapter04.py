import numpy as np
import pandas as pd


eq_df = pd.read_csv('data/earthquakes.csv')

print("Question 1\n", eq_df.query('magType == "mb" and parsed_place == "Japan" and mag >= 4.9'))

print("\nQuestion 2\n", eq_df.query("magType == 'ml'").assign(bin = lambda x: pd.cut(x.mag, np.arange(0, 10))).bin.value_counts())

faang_df = pd.read_csv('data/faang4.csv', index_col='date', parse_dates=True)

print("\nQuestion 3\n", faang_df.groupby('ticker').resample('1M').agg({'open': np.mean,'high': np.max,'low': np.min,'close': np.mean,'volume': np.sum}))

print("\nQuestion 4\n", pd.crosstab(eq_df.tsunami, eq_df.magType, values=eq_df.mag, aggfunc='max').fillna("N/A"))

print("\nQuestion 5\n", faang_df.groupby('ticker').rolling('60D').agg({'open': np.mean,'high': np.max,'low': np.min,'close': np.mean,'volume': np.sum}))

print('\nQuestion 6\n', faang_df.pivot_table(index='ticker'))

print("\nQuestion 7\n", faang_df.loc['2018-Q4'].query("ticker == 'AMZN'").drop(columns='ticker').apply(lambda x: x.sub(x.mean()).div(x.std())).head())

df = pd.DataFrame({'ticker': 'FB','date': pd.to_datetime(['2018-07-25', '2018-03-19', '2018-03-20']),'event': ['Disappointing user growth announced after close.','Cambridge Analytica story','FTC investigation']}).set_index(['date', 'ticker'])

merge_df = faang_df.reset_index().set_index(['date', 'ticker']).join(df, how='outer')

print("\nQuestion 8\n",merge_df)
faang_df = faang_df.reset_index().set_index(['date','ticker'])
trans_df = (faang_df/faang_df.groupby(level='ticker').transform('first'))

print('\nQuestion 9\n', trans_df)

c19_df = pd.read_csv('data/covid19_cases4.csv')
c19_df = c19_df.assign(date = lambda x: pd.to_datetime(x.dateRep)).set_index('date').replace({'United_States_of_America':'USA', "United_Kingdom":"UK"}).sort_index()

days_df = c19_df[c19_df.countriesAndTerritories.isin(c19_df.groupby('countriesAndTerritories').sum('cases').nlargest(5, 'cases').index)].groupby('countriesAndTerritories').cases.idxmax()

print('\nQuestion 10b\n', days_df)

avg_df = c19_df.assign(avg7 = lambda x: x.cases.rolling('7D').mean().diff())

avg_df = avg_df.reset_index().pivot(index='date', columns='countriesAndTerritories', values='avg7').last('7D')[c19_df.groupby('countriesAndTerritories').sum('cases').nlargest(5, 'cases').index]


print('\nQuestion 10c\n', avg_df)

first_df = c19_df.reset_index().pivot(index='date', columns='countriesAndTerritories', values='cases').drop(columns='China').apply(lambda x: x[(x > 0)].idxmin()).sort_values()

print('\nQuestion 10d\n', first_df)

rank_df = c19_df.pivot_table(columns='countriesAndTerritories', values='cases', aggfunc='sum').T.transform('rank', method='max', pct=True).sort_values('cases', ascending=False)

print('\nQuestion 10e\n', rank_df)

