# INFO-B211_Assignment-8-Seaborn

## Overview
This project demonstrates the use of Seaborn to create insightful visualizations for two datasets:
- **Exercise Dataset**: Visualizing exercise-related data to uncover trends and patterns.
- **Planets Dataset**: Exploring planetary data to analyze trends in discoveries and planetary characteristics.

The project is designed to showcase the power of Seaborn in creating aesthetically pleasing and informative visualizations. A consistent pink theme is applied across all visualizations to enhance readability and aesthetics.

---

## Project Structure
The project is divided into two main sections:

#### Exercise Dataset Visualizations:
- Relational plots: Scatter plot and line plot.
- Distributional plots: Histogram and KDE plot.
- Categorical plots: Bar plot and count plot.

#### Planets Dataset Visualizations:
- Relational plots: Scatter plot and line plot.
- Distributional plots: Histogram and bar plot.
- Categorical plots: Count plot.

---

## Exercise Dataset Visualizations
#### Purpose
The exercise dataset visualizations aim to uncover trends in exercise habits, such as relationships between variables, data distributions, and category comparisons.

### Visualizations
#### Scatter Plot: Exercise Duration vs. Calories Burned

##### Purpose: 
Show the relationship between exercise duration and calories burned.
##### Implementation:
A scatter plot with distinct colors for different exercise types.
Includes a legend and grid for readability.
##### Limitations: 
Assumes clean data with no missing values.

#### Line Plot: Weekly Exercise Trends

##### Purpose: 
Visualize trends in exercise duration over a week.
##### Implementation:
A line plot with a pink theme.
Includes markers for each day and a legend for clarity.
##### Limitations:
Assumes data is aggregated by day of the week.

#### Histogram: Distribution of Exercise Durations

##### Purpose: 
Show the distribution of exercise durations across all activities.
##### Implementation:
A histogram with bins representing ranges of durations.
Uses a consistent pink color theme.
##### Limitations:
Outliers may skew the distribution.

#### Count Plot: Number of Exercises by Type

##### Purpose: 
Highlight the frequency of different exercise types.
##### Implementation:
A count plot with bars for each exercise type.
Includes a legend and grid for readability.
##### Limitations:
Assumes all exercise types are represented in the dataset.

---

## Planets Dataset Visualizations
#### Purpose
The planets dataset visualizations aim to explore trends in planetary discoveries and characteristics, such as orbital periods, masses, and detection methods.

### Visualizations
#### Scatter Plot: Orbital Period vs. Planet Mass

##### Purpose: 
Show the relationship between orbital period and planet mass, categorized by detection method.
##### Implementation:
A scatter plot with distinct colors for each detection method.
Includes a legend and grid for readability.
##### Limitations: 
Outliers may obscure trends in the data.

#### Line Plot: Planets Discovered Over Time

##### Purpose: 
Visualize the trend of planetary discoveries over the years.
##### Implementation:
A line plot with a pink theme.
Includes markers for each year and a legend for clarity.
##### Limitations:
Assumes data is aggregated by year.

#### Histogram: Distribution of Planet Masses

##### Purpose: 
Show the distribution of planet masses.
##### Implementation:
A histogram with bins representing ranges of masses.
Uses a consistent pink color theme.
##### Limitations:
Missing values are ignored.

#### Bar Plot: Average Planet Mass by Detection Method

##### Purpose: 
Compare the average planet mass across detection methods.
##### Implementation:
A bar plot with bars for each detection method.
Includes a legend and grid for readability.
##### Limitations:
Assumes missing values are handled appropriately.

#### Count Plot: Number of Planets Discovered by Method

##### Purpose: 
Highlight the frequency of planets discovered by each detection method.
##### Implementation:
A count plot with bars for each detection method.
Includes a legend and grid for readability.
##### Limitations:
Assumes all detection methods are represented in the dataset.

---

## Conclusion
This project demonstrates how Seaborn can be used to create insightful visualizations for different datasets. By analyzing the exercise and planets datasets, we can uncover trends and patterns that would otherwise be difficult to observe. The consistent use of a pink theme enhances the visual appeal and readability of the charts.
