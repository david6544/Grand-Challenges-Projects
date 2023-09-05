#%%
import matplotlib.pyplot as plt
import geopandas as gpd
import pandas as pd
import numpy as np
from scipy.stats import linregress


data = pd.read_csv(r'./athlete_events.csv')
worldPop = pd.read_csv(r'./world_population.csv')


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





#drop all years

#data = data.query("Sport == 'Swimming'")
                #| Sport == 'Sailing'  | Sport == 'Water Polo'  | Sport == 'Rowing'  | Sport == 'Diving' | Sport == 'Canoeing'  | Sport == 'Synchronized Swimming'  | Sport == 'Motorboating'")      

current_sports = data['Sport'].unique()
#print(data.columns)


data = data.dropna(subset=['Age'])
data = data.dropna(subset=['Medal'])
#drop winter
data = data.drop(data[data['Season'] == 'Winter'].index)
data = data.drop(data[data['Sex'] != 'F'].index)


data_current_sports = data[data['Sport'].isin(current_sports)]
# Group data by Year and Sport, then calculate average age for each group
avg_age_by_year = data_current_sports.groupby('Year')['Age'].mean()

x = avg_age_by_year.index
y = avg_age_by_year.values
slope, intercept, r_value, p_value, std_err = linregress(x, y)
trend_line = slope * x + intercept


#print the oldest athletes
print(data_current_sports.sort_values(by=['Age'], ascending=False).head(10))

# Plot the average age over time for all sports with the trend line
plt.figure(figsize=(10, 6))
plt.plot(x, y, label='Average Age')
plt.plot(x, trend_line, linestyle='--', label='Trend Line')
plt.axvline(x=1916, color='red', linestyle=':', label='Year 1918')
plt.axvline(x=1940, color='blue', linestyle=':', label='Year 1940')
plt.title('Average Age Over Time for All Sports with Trend Line')
plt.xlabel('Year')
plt.ylabel('Average Age')
plt.ylim(20, 30)
plt.legend()
plt.tight_layout()
plt.show()

#print average age over time for each sport
# %%
