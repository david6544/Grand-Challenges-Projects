#%%
import matplotlib.pyplot as plt
import geopandas as gpd
import pandas as pd
import numpy as np

# Load the datasets
world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
worldpop = pd.read_csv('world_population.csv')
medals = pd.read_csv('athlete_events.csv')


# delete repeated athletes
#

# drop non gold medals
#print(medals)

#data.drop(data[data['Medal'] != 'Gold'].index, inplace=True)


# Calculate the count of medals for each Team
medal_counts = data['Team'].value_counts()
#print(medal_counts.head(5))

# Calculate the total count of athletes for each Team
athlete_counts = medals['Team'].value_counts()

#print(athlete_counts.head(5))

# Calculate the ratio of medalists to total athletes for each Team
ratio = medal_counts 

#remove all countries with less than 5 percent

# Filter out countries not in the world population dataset
valid_countries = worldpop['Country/Territory'].tolist()
ratio = ratio[ratio.index.isin(valid_countries)]

#Rename united States to USA
ratio.rename(index={'United States': 'United States of America'}, inplace=True)


# Merge medalist ratio data with world map data
world = world.merge(ratio, how='left', left_on='name', right_index=True)

# sort ratio
ratio = ratio.sort_values(ascending=False)

#only include countries with greater than 5 percent
#print top 20
print(ratio.head(20))

# Create the density map
fig, ax = plt.subplots(1, 1, figsize=(20, 15))
world.boundary.plot(ax=ax, linewidth= 0.5, color='black')
world.plot(column=ratio.name, ax=ax, legend=True, cmap='Wistia', legend_kwds={'label': "Olympic Medals", 'orientation': "horizontal"})
plt.title('Total Number of Olympic Medals')
plt.show()








# %%
