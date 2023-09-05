#%%
import matplotlib.pyplot as plt
import geopandas as gpd
import pandas as pd
import numpy as np

# Load the datasets
world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
worldpop = pd.read_csv('world_population.csv')
medals = pd.read_csv('athlete_events.csv')

# Drop rows where Medal column is NaN

# Drop all but swimming and diving

# Categories Aquatic
#medals.drop(medals[medals['Sport'] == 'Swimming'].index, inplace=True)
medals.drop(medals[medals['Sport'] == 'Sailing' ].index, inplace=True)
medals.drop(medals[medals['Sport'] == 'Water Polo' ].index, inplace=True)
medals.drop(medals[medals['Sport'] == 'Rowing' ].index, inplace=True)
medals.drop(medals[medals['Sport'] == 'Diving' ].index, inplace=True)
medals.drop(medals[medals['Sport'] == 'Canoeing' ].index, inplace=True)
medals.drop(medals[medals['Sport'] == 'Synchronized Swimming' ].index, inplace=True)
medals.drop(medals[medals['Sport'] == 'Motorboating' ].index, inplace=True)
medals.drop(medals[medals['Sport'] == 'Water Motorsports' ].index, inplace=True)


# Categories Track & Field
medals.drop(medals[medals['Sport'] == 'Athletics' ].index, inplace=True)
medals.drop(medals[medals['Sport'] == 'Triathlon' ].index, inplace=True)
medals.drop(medals[medals['Sport'] == 'Modern Pentathlon' ].index, inplace=True)

# Categories Team Sports
medals.drop(medals[medals['Sport'] == 'Basketball'].index, inplace=True)
medals.drop(medals[medals['Sport'] == 'Football' ].index, inplace=True)
medals.drop(medals[medals['Sport'] == 'Tug-Of-War' ].index, inplace=True)
medals.drop(medals[medals['Sport'] == 'Rugby Sevens' ].index, inplace=True)
medals.drop(medals[medals['Sport'] == 'Beach Volleyball' ].index, inplace=True)
medals.drop(medals[medals['Sport'] == 'Handball' ].index, inplace=True)
medals.drop(medals[medals['Sport'] == 'Volleyball' ].index, inplace=True)
medals.drop(medals[medals['Sport'] == 'Hockey' ].index, inplace=True)
medals.drop(medals[medals['Sport'] == 'Lacrosse' ].index, inplace=True)
medals.drop(medals[medals['Sport'] == 'Polo' ].index, inplace=True)
medals.drop(medals[medals['Sport'] == 'Softball'].index, inplace=True)
medals.drop(medals[medals['Sport'] == 'Baseball'].index, inplace=True)
medals.drop(medals[medals['Sport'] == 'Rugby' ].index, inplace=True)
medals.drop(medals[medals['Sport'] == 'Cricket' ].index, inplace=True)


#Categories Combat Sports
medals.drop(medals[medals['Sport'] == 'Boxing' ].index, inplace=True)
medals.drop(medals[medals['Sport'] == 'Wrestling' ].index, inplace=True)
medals.drop(medals[medals['Sport'] == 'Judo' ].index, inplace=True)
medals.drop(medals[medals['Sport'] == 'Wrestling' ].index, inplace=True)
medals.drop(medals[medals['Sport'] == 'Taekwondo' ].index, inplace=True)


#Category Single Sports
medals.drop(medals[medals['Sport'] == 'Badminton'].index, inplace=True)
medals.drop(medals[medals['Sport'] == 'Table Tennis'].index, inplace=True)
medals.drop(medals[medals['Sport'] == 'Fencing' ].index, inplace=True)
medals.drop(medals[medals['Sport'] == 'Art Competitions'].index, inplace=True)
medals.drop(medals[medals['Sport'] == 'Weightlifting' ].index, inplace=True)
medals.drop(medals[medals['Sport'] == 'Equestrianism' ].index, inplace=True)
medals.drop(medals[medals['Sport'] == 'Shooting'].index, inplace=True)
medals.drop(medals[medals['Sport'] == 'Cycling'].index, inplace=True)
medals.drop(medals[medals['Sport'] == 'Tennis' ].index, inplace=True)
medals.drop(medals[medals['Sport'] == 'Golf' ].index, inplace=True)
medals.drop(medals[medals['Sport'] == 'Archery' ].index, inplace=True)



#Category Gymnastics
medals.drop(medals[medals['Sport'] == 'Rhythmic Gymnastics' ].index, inplace=True)
medals.drop(medals[medals['Sport'] == 'Gymnastics'].index, inplace=True)
medals.drop(medals[medals['Sport'] == 'Trampolining'].index, inplace=True)


#Category Winter Sports
medals.drop(medals[medals['Sport'] == 'Ski Jumping' ].index, inplace=True)
medals.drop(medals[medals['Sport'] == 'Alpine Skiing' ].index, inplace=True)
medals.drop(medals[medals['Sport'] == 'Snowboarding' ].index, inplace=True)
medals.drop(medals[medals['Sport'] == 'Freestyle Skiing' ].index, inplace=True)
medals.drop(medals[medals['Sport'] == 'Nordic Combined' ].index, inplace=True)
medals.drop(medals[medals['Sport'] == 'Short Track Speed Skating' ].index, inplace=True)
medals.drop(medals[medals['Sport'] == 'Speed Skating' ].index, inplace=True)
medals.drop(medals[medals['Sport'] == 'Figure Skating' ].index, inplace=True)
medals.drop(medals[medals['Sport'] == 'Bobsleigh' ].index, inplace=True)
medals.drop(medals[medals['Sport'] == 'Luge' ].index, inplace=True)
medals.drop(medals[medals['Sport'] == 'Curling' ].index, inplace=True)
medals.drop(medals[medals['Sport'] == 'Skeleton' ].index, inplace=True)
medals.drop(medals[medals['Sport'] == 'Ice Hockey' ].index, inplace=True)
medals.drop(medals[medals['Sport'] == 'Biathlon' ].index, inplace=True)
medals.drop(medals[medals['Sport'] == 'Cross Country Skiing' ].index, inplace=True)


# Category Other
medals.drop(medals[medals['Sport'] == 'Racquets' ].index, inplace=True)
medals.drop(medals[medals['Sport'] == 'Motorboating' ].index, inplace=True)
medals.drop(medals[medals['Sport'] == 'Military Ski Patrol' ].index, inplace=True)
medals.drop(medals[medals['Sport'] == 'Croquet'].index, inplace=True)
medals.drop(medals[medals['Sport'] == 'Jeu De Paume'].index, inplace=True)
medals.drop(medals[medals['Sport'] == 'Roque' ].index, inplace=True)
medals.drop(medals[medals['Sport'] == 'Alpinism' ].index, inplace=True)
medals.drop(medals[medals['Sport'] == 'Basque Pelota' ].index, inplace=True)
medals.drop(medals[medals['Sport'] == 'Aeronautics'].index, inplace=True)

#rename United States to Untited States of America in Team
medals['Team'] = medals['Team'].replace(['United States'], 'United States of America')



athlete_info = medals


# delete repeated athletes
medals.drop_duplicates(subset=['Name'], inplace=True) 
#
medals = medals.drop (medals[medals['Sex'] == 'F'].index)

# drop non gold medals
#print(medals)

data = medals.dropna(subset=['Medal'])
#data.drop(data[data['Medal'] != 'Gold'].index, inplace=True)


# Calculate the count of medals for each Team
medal_counts = data['Team'].value_counts()
#print(medal_counts.head(5))

# Calculate the total count of athletes for each Team
athlete_counts = medals['Team'].value_counts()

#print(athlete_counts.head(5))

# Calculate the ratio of medalists to total athletes for each Team
ratio = medal_counts / athlete_counts * 100

#remove all countries with less than 5 percent

# Filter out countries not in the world population dataset
valid_countries = worldpop['Country/Territory'].tolist()
ratio = ratio[ratio.index.isin(valid_countries)]
ratio.rename(index={'United States': 'United States of America'}, inplace=True)

#Rename united States to USA

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
world.plot(column=ratio.name, ax=ax, legend=True, cmap='Wistia', legend_kwds={'label': "Medalist Percentage", 'orientation': "horizontal"})
plt.title('Medalist Percentage Density Map')
plt.show()



## Make another graph showing the average height and weight of olympians of these countries
# %%

athlete_info.dropna(subset=['Sex'], inplace=True)

#remove non medalists
athlete_info.dropna(subset=['Medal'], inplace=True)
#Only include male athletes
athlete_info = athlete_info.drop (athlete_info[athlete_info['Sex'] == 'F'].index)

# rename United States to USA in athelete_info

# Filter athlete_info dataset to include only valid countries
athlete_info_filtered = athlete_info[athlete_info['Team'].isin(valid_countries)]

#only use modern data
athlete_info_filtered = athlete_info_filtered.drop(athlete_info_filtered[athlete_info_filtered['Year'] < 1980].index)

# Calculate average height and weight for each country
average_height_weight = athlete_info_filtered.groupby('Team')[['Height','Weight']].mean()

#sort by their position in medal ratio
average_height_weight = average_height_weight.reindex(ratio.index)

print(average_height_weight.head(20))

average_height_weight.dropna(subset=['Height'], inplace=True)

print(average_height_weight.head(15))
#average_height_weight = average_height_weight.head(10)
#average BMI
bmi = average_height_weight['Weight'] / (average_height_weight['Height'] / 100) ** 2

x = np.arange(len(bmi))
slope, intercept = np.polyfit(x, bmi, 1)

# Create a bar plot for average height and weight with trend line
fig, ax = plt.subplots(figsize=(10, 8))
bmi.plot(kind='bar', ax=ax)
plt.plot(x, slope * x + intercept, color='red', linestyle='--', label='Trend Line')
plt.title('Average BMI of Aquatic Sports Medalists by Country')
plt.xlabel('Country')
plt.ylabel('Average BMI')
plt.legend()
plt.ylim(21, 25)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()







# %%
