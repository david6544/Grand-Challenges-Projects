#%%
import matplotlib.pyplot as plt
import geopandas as gpd
import pandas as pd
import numpy as np
from scipy.stats import linregress


data = pd.read_csv(r'./athlete_events.csv')
worldPop = pd.read_csv(r'./world_population.csv')

#Remove all sports that are not currently run

data = data.drop(data[data['Sport'] == 'Tug-Of-War'].index)
data = data.drop(data[data['Sport'] == 'Art Competitions'].index)
data = data.drop(data[data['Sport'] == 'Alpne Skiing'].index)
data = data.drop(data[data['Sport'] == 'Racquets'].index)
data = data.drop(data[data['Sport'] == 'Military Ski Patrol'].index)
data = data.drop(data[data['Sport'] == 'Croquet'].index)
data = data.drop(data[data['Sport'] == 'Jeu De Paume'].index)
data = data.drop(data[data['Sport'] == 'Roque'].index)
data = data.drop(data[data['Sport'] == 'Alpinism'].index)
data = data.drop(data[data['Sport'] == 'Basque Pelota'].index)
data = data.drop(data[data['Sport'] == 'Aeronautics'].index)
data = data.drop(data[data['Sport'] == 'Polo'].index)
data = data.drop(data[data['Sport'] == 'Cricket'].index)
data = data.drop(data[data['Sport'] == 'Softball'].index)
data = data.drop(data[data['Sport'] == 'Lacrosse'].index)
data = data.drop(data[data['Sport'] == 'Motorboating'].index)
data = data.drop(data[data['Sport'] == 'Water Motorsports'].index)
data = data.drop(data[data['Sport'] == 'Archery'].index)


current_sports = data['Sport'].unique()
print(data.columns)


#clean data
data = data.dropna(subset=['Height'])
data = data.dropna(subset=['Weight'])
data = data.dropna(subset=['Medal'])


data = data.drop(data[data['Season'] == 'Winter'].index)


#calc BMI
data['BMI'] = data['Weight'] / ((data['Height']/100) ** 2) 
print(data)


data_current_sports = data[data['Sport'].isin(current_sports)]
# Group data by Year and Sport, then calculate average age for each group
avg_age_by_year = data_current_sports.groupby('Year')['BMI'].mean()

x = avg_age_by_year.index
y = avg_age_by_year.values
slope, intercept, r_value, p_value, std_err = linregress(x, y)
trend_line = slope * x + intercept

# Plot the average age over time for all sports with the trend line
plt.figure(figsize=(10, 6))
plt.plot(x, y, label='Average BMI')
plt.plot(x, trend_line, linestyle='--', label='Trend Line')
plt.axvline(x=1918, color='red', linestyle=':', label='Year 1918')
plt.axvline(x=1940, color='blue', linestyle=':', label='Year 1940')
plt.title('Average BMI Over Time for All Sports with Trend Line')
plt.xlabel('Year')
plt.ylabel('Average BMI')
plt.legend()
plt.tight_layout()
plt.show()

#print average age over time for each sport
# %%
