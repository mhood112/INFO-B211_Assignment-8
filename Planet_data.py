import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Set a pink theme
sns.set_theme(style="whitegrid", palette="pink")

# Load the planets dataset
planets = sns.load_dataset('planets')

# Relational Plots
plt.figure(figsize=(12, 6))

# Scatter plot: Orbital period vs. Planet mass
plt.subplot(1, 2, 1)
sns.scatterplot(data=planets, x='orbital_period', y='mass', hue='method')
plt.title('Orbital Period vs. Planet Mass')
plt.xlabel('Orbital Period (days)')
plt.ylabel('Mass (Jupiter Mass)')
plt.legend(title='Detection Method', bbox_to_anchor=(1.05, 1), loc='upper left')

# Line plot: Year vs. Number of planets discovered
plt.subplot(1, 2, 2)
sns.lineplot(data=planets.groupby('year').size().reset_index(name='count'), x='year', y='count')
plt.title('Planets Discovered Over Time')
plt.xlabel('Year')
plt.ylabel('Number of Planets Discovered')
plt.tight_layout()
plt.show()

# Distributional Plots
plt.figure(figsize=(12, 6))

# Histogram: Distribution of planet masses
plt.subplot(1, 2, 1)
sns.histplot(planets['mass'].dropna(), bins=30, kde=True)
plt.title('Distribution of Planet Masses')
plt.xlabel('Mass (Jupiter Mass)')
plt.ylabel('Frequency')

# Bar plot: Average planet mass by detection method
plt.subplot(1, 2, 2)
sns.barplot(data=planets.dropna(subset=['mass']), x='method', y='mass', estimator=np.mean)
plt.title('Average Planet Mass by Detection Method')
plt.xlabel('Detection Method')
plt.ylabel('Average Mass (Jupiter Mass)')
plt.xticks(rotation=90)

plt.tight_layout()
plt.show()

# Categorical Plots
plt.figure(figsize=(12, 6))

# Count plot: Number of planets discovered by method
plt.subplot(1, 2, 1)
sns.countplot(data=planets, y='method', order=planets['method'].value_counts().index)
plt.title('Number of Planets Discovered by Method')
plt.xlabel('Count')
plt.ylabel('Detection Method')

plt.tight_layout()
plt.show()

# Analysis of Notable Graphs
"""
The scatter plot of Orbital Period vs. Planet Mass is particularly notable because it shows
a wide range of orbital periods and masses, with some clustering around specific detection methods.
This illustrates how different methods are better suited for detecting planets with certain characteristics.

Additionally, the count plot of planets discovered by method highlights the dominance of certain
detection methods, such as Radial Velocity and Transit, in discovering exoplanets.
"""