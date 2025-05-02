# Air-Pollution-Analysis-Python-Project
This project analyzes air quality data from various cities and states across India. It uses Python libraries like Pandas, Matplotlib, and Seaborn to perform Exploratory Data Analysis (EDA) and derive insights about air pollution trends, seasonal variations, state and city comparisons, and pollutant contributions.
📁 Dataset
File used: ProjectP.csv

The dataset contains information about:
City and state names
Different pollutants like PM2.5, NO2, CO, SO2, etc.
Air Quality Index (AQI) values (average, min, and max)
Last updated date for each record

🧪 Tools & Libraries
#pandas – for data manipulation
matplotlib – for creating visualizations
seaborn – for enhanced statistical plots

🧼 Data Preprocessing
Displayed initial rows using head() and tail()
Checked column names, null values, and summary statistics
Filled missing values using forward fill (ffill)
Removed duplicate records
Extracted new columns like year, month, and season

🎯 Objectives and Insights

✅ Objective 1: Analyze Air Quality Trends Over Time
Visualized cities with the highest and lowest AQI over multiple years.
Identified Top 10 polluted and least polluted cities.
Created grouped bar charts for comparison across cities and states.

✅ Objective 2: Contribution of Different Pollutants
Used a donut-style pie chart to compare pollutants like PM2.5, NO2, CO, and SO2.
Found out which pollutants have a greater contribution to AQI.

✅ Objective 3: Seasonal Variation in Air Pollution
Categorized months into seasons: Winter, Summer, Monsoon, Post-Monsoon.
Visualized seasonal AQI levels using boxplots and heatmaps.
Found which season has the highest pollution levels.

✅ Objective 4: Ranking Indian States by AQI
Calculated average AQI per state.
Visualized rankings using horizontal bar charts.

✅ Objective 5: Distribution of AQI Levels
Used a histogram to show how frequently different AQI levels occur.

✅ Objective 6: Spread of AQI Across States
Used violin plots to visualize AQI distribution across different Indian states.

✅ Objective 7: Compare Air Quality Stats (Min, Max, Avg)
Created a pairplot to study relationships between different AQI stats for each state.
Used a scatter plot to explore the relation between average and maximum AQI values.


📌 Key Insights
Certain cities consistently report higher AQI levels across years.
Winter tends to have the worst air quality due to various environmental and human factors.
PM2.5 contributes the most to overall pollution in many cities.
States like Delhi and Uttar Pradesh show consistently high average AQI.


📷 Visualizations
The project includes:
Bar plots
Pie chart (donut style)
Boxplots and violin plots
Heatmaps
Pair plots
Scatter plots
All plots are designed to highlight trends, make comparisons, and reveal patterns in air pollution data.

📚 How to Run
Make sure you have Python installed.

Install required libraries:
pip install pandas matplotlib seaborn
Place the dataset ProjectP.csv in the specified path or update the path in the code.
Run the Python script in your IDE or terminal.


🙋‍♀️ Author
Easha Sharma
Student of BTech (Computer Science and Engineering)
Passionate about data analysis and environmental awareness.
