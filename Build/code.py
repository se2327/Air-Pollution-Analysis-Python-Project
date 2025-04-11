            #Project Topic:-🌍 Air Quality Trends Analysis in India 

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv("C:\\Users\\hp\\Desktop\\ProjectP.csv")
print(df.head())  #--> will show some top rows
print(df.tail())   #---> will show last some rows data 
print(df.columns) #---> will shows all column names to us
print(df.info)
print(df.describe()) #---> will show Basic statistics like (mean,median,avg etc.)


print("\n")
'''Now check mising values'''
print(df.isnull())
print(df.isnull().sum()) #--> will show how many missing values(null values) per column
print(df.isnull().sum().sum())


print("\n")
'''Now Droping / filling teh missing values'''
    #here i preffered filling instead of dropna because it can loss my useful data because of only one null vlaue present..
df=df.ffill()  #---> ffill means filling previous value of that particular column
    #now checking again is there any missing value after filling
print(df.isnull().sum().sum())


print("\n")
'''Check for duplicates'''
print(df.duplicated().sum()) #-->check how many duplictes are in dataset
df=df.drop_duplicates()   #--> remove duplicates if any


print("\n")
'''Check Unique Values'''
print(df['state'].unique()) #--> will show name of unique states
print(df['pollutant_id'].value_counts()) #---> shows how many times each pollutant appears in the dataset

print("\n")
print(df.shape)
print(df.size)

'''So above was part of EDA(Exploratory Data Analysis) of our dataset for our better understanding..'''

# Objective1:-
'''To analyze the air quality trends across different cities and states in India over multiple years
 by identifying which cities have the highest and lowest AQI values and 
 understanding how air pollution levels have changed over time.'''


df['last_update'] = pd.to_datetime(df['last_update'])  # convert to datetime in proper format
df['year'] = df['last_update'].dt.year  #--> it will extract only years from it..
city_year_avg = df.groupby(['city', 'year'])['pollutant_avg'].mean().reset_index()  #--># Group by city and year, then take mean of pollutant_avg
highest = city_year_avg.sort_values(by='pollutant_avg', ascending=False).head(10)   # Highest average
lowest = city_year_avg.sort_values(by='pollutant_avg').head(10)  # lowest

# '''Both the barplots in one...'''
# Set figure size for both plots together
plt.figure(figsize=(12, 7))

# # First plot - Top 10 most polluted cities
plt.subplot(2, 1, 1)  # (rows, cols, position) -> this is 1st plot
sns.barplot(data=highest, x='pollutant_avg', y='city', palette='Reds_r',hue='city')
plt.title('Top 10 Most Polluted Cities (Highest Average AQI)')
plt.xlabel('Average AQI')
plt.ylabel('City')

# # Second plot - Top 10 least polluted cities
plt.subplot(2, 1, 2)  # this is 2nd plot
sns.barplot(data=lowest, x='pollutant_avg', y='city', palette='Greens',hue='city')
plt.title('Top 10 Least Polluted Cities (Lowest Average AQI)')
plt.xlabel('Average AQI')
plt.ylabel('City')

# # Show both together
plt.tight_layout()  #--> used for adjusts spacing to prevent overlap between plot elements
plt.show()

'''Now one more chart for this objective..'''
#Grouped Bar Chart, also known as a Clustered Bar Chart

# Filter top 5 cities with highest average pollution
top_cities = df.groupby('city')['pollutant_avg'].mean().sort_values(ascending=False).head(5).index
filtered_df = df[df['city'].isin(top_cities)]

# Plot grouped bar chart
plt.figure(figsize=(12, 6))
chart = sns.barplot(data=filtered_df, x='city', y='pollutant_avg', hue='state', palette='deep')

# Add titles and labels
plt.title("Grouped Bar Chart - Top 5 Most Polluted Cities by State", fontsize=14)
plt.xlabel("City")
plt.ylabel("Average Pollution Level")
plt.legend(title='State', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()

plt.show()



#Objective2:-
'''2. To compare the contribution of different pollutants such as PM2.5, NO2, CO, and SO2 in 
overall air pollution and determine which pollutant has the most significant impact on AQI levels.'''

pollutant_data = df.groupby('pollutant_id')['pollutant_avg'].mean()
#Set some colors 
colors = ['indianred', 'cornflowerblue', 'mediumseagreen', 'sandybrown', 'mediumorchid']

#  Make a pie chart (donut style)
plt.figure(figsize=(7, 7))
plt.pie(pollutant_data, 
        labels=pollutant_data.index, 
        colors=colors, 
        autopct='%1.1f%%',      #--->show slices with percentage labels
        startangle=140)     #--→ Rotates the chart so the slices are better positioned.

#Draw white circle in center to make it a donut 
circle = plt.Circle((0, 0), 0.30, color='white')
plt.gca().add_artist(circle)   #--> it basically adds a white circle in the center to create a donut chart

# Add a simple title
plt.title("Pollution by Type", fontsize=13, color='darkblue',backgroundcolor='lightblue')

plt.tight_layout()
plt.show()


#Objective 3:-
'''3. To study seasonal variations in air pollution by analyzing AQI data across different seasons 
(winter, summer, monsoon, and post-monsoon) and determine which season has the highest pollution levels.'''


# Extract month from the date
df['month'] = df['last_update'].dt.month

# Function to assign seasons based on month
def get_season(month):
    if month in [12, 1, 2]:
        return 'Winter'
    elif month in [3, 4, 5]:
        return 'Summer'
    elif month in [6, 7, 8]:
        return 'Monsoon'
    else:
        return 'Post-Monsoon'

# Create a new column 'season'
df['season'] = df['month'].apply(get_season)

# Create the box plot
plt.figure(figsize=(10, 6))
sns.boxplot(data=df, x='season', y='pollutant_avg', palette='muted',hue='season',legend=False)

# Add title and labels
plt.title("Seasonal Variation in Air Pollution (AQI)", fontsize=16,
            backgroundcolor='lightblue',
            fontweight='bold',
            pad=20
        )
plt.xlabel("Season")
plt.ylabel("Average AQI")

# Show the plot
plt.tight_layout()
plt.show()



'''Now for this objective one more way of visualising with heatmap'''
# Average AQI per month
df['month'] = pd.to_datetime(df['last_update']).dt.month
monthly_avg = df.groupby(['state', 'month'])['pollutant_avg'].mean().unstack()

# Plotting heatmap
plt.figure(figsize=(12, 8))
sns.heatmap(monthly_avg, cmap='coolwarm', linewidths=0.3, annot=True, fmt=".1f")

plt.title("Heatmap of Monthly Average AQI by State", fontsize=14)
plt.xlabel("Month")
plt.ylabel("State")
plt.tight_layout()
plt.show()


#Objective4:-
'''4. To rank Indian states based on their air quality index (AQI) by calculating the average AQI
 for each state and identifying the most and least polluted states.'''

state_avg = df.groupby('state')['pollutant_avg'].mean().sort_values(ascending=False)

# Plot the horizontal bar chart
plt.figure(figsize=(10, 7))
sns.barplot(x=state_avg.values, y=state_avg.index, palette='YlGnBu',hue=state_avg.index,legend=False)

# Add title and labels
plt.title("Average AQI by Indian States", fontsize=14, backgroundcolor='lightblue')
plt.xlabel("Average AQI")
plt.ylabel("State")

#Show the plot
plt.tight_layout()
plt.show()

#Objective:-(small part)
'''To understand how often different AQI levels occur by showing the overall distribution of air pollution using a histogram.'''
plt.figure(figsize=(8, 6))
sns.histplot(data=df, x='pollutant_avg', kde=True, bins=90, color='yellow')
plt.title("Histogram of Average AQI", backgroundcolor='lightblue')
plt.xlabel("Average AQI")
plt.ylabel("Frequency")
plt.tight_layout()
plt.show()


#Objective5:-
'''To compare the spread and distribution of AQI levels across different Indian states using a violin plot.'''
# Set the figure size
plt.figure(figsize=(12, 6))

# Create the violin plot
sns.violinplot(data=df, x='state', y='pollutant_avg', palette='pastel',hue='state',legend=False)

# Add title and labels
plt.title("AQI Distribution Across Indian States", backgroundcolor='lightblue', fontsize=14)
plt.xlabel("State")
plt.ylabel("Average AQI")

# Rotate state names if they overlap
plt.xticks(rotation=60,ha='right')   #--> ha used so that names don'y clash with eachother

# Show the plot
plt.tight_layout()     
plt.show()

#Objective6:-
'''"To compare different air quality values (like minimum, maximum, and average pollution) for each state
 in India, and to see if there are any patterns, similarities, or differences between them."'''

sns.set_palette('pastel')

# Create the pair plot
#-->here numerical values in dataset that's why making pairplot
pair_plot = sns.pairplot(
    df,
    hue='state',        #categorial data  
    height=1.7,
    diag_kind='kde',
)

# Add a title to the plot
pair_plot.fig.suptitle('Pairwise Relationships of Air Quality Indicators', y=1.02)

# Show the plot
plt.show()

#Objective7:-
'''To visualize the relationship between the average and maximum AQI values across different Indian states 
using a scatter plot.'''

plt.figure(figsize=(8, 6))

# Create scatter plot
sns.scatterplot(data=df, x='pollutant_avg', y='pollutant_max', hue='state', palette='colorblind')

# Add title and labels
plt.title("Scatter Plot: Avg vs Max AQI by State", fontsize=14, backgroundcolor='lightblue')
plt.xlabel("Average AQI")
plt.ylabel("Maximum AQI")
plt.tight_layout()
plt.show()
