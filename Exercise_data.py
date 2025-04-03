import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
data = pd.read_csv('Exercise_Data.csv')

# Reshape the data for the heatmap
pulse_data = data.melt(id_vars=['diet', 'kind'], value_vars=['1 min', '15 min', '30 min'],
                       var_name='Time', value_name='Pulse')

# Create a pivot table for the heatmap
heatmap_data = pulse_data.pivot_table(index='diet', columns=['kind', 'Time'], values='Pulse', aggfunc='mean')

# Set a pink color palette and style
sns.set_palette("pink")  # Use a pink-based color palette
sns.set_style("whitegrid")  # Use a clean grid style
plt.rcParams.update({'font.size': 12})  # Increase font size for better readability

# Heatmap of pulse data
plt.figure(figsize=(14, 8))
sns.heatmap(heatmap_data, annot=True, fmt=".1f", cmap='RdPu', cbar_kws={'label': 'Pulse'}, linewidths=0.5)
plt.title('Heatmap of Average Pulse by Diet, Exercise Type, and Time', fontsize=16, weight='bold')
plt.xlabel('Exercise Type and Time', fontsize=14)
plt.ylabel('Diet Type', fontsize=14)
plt.xticks(rotation=45, ha='right', fontsize=12)
plt.yticks(fontsize=12)
plt.tight_layout()
plt.show()

# Categorical plot of pulse values by diet and exercise type
catplot = sns.catplot(
    data=pulse_data,
    x='diet',
    y='Pulse',
    hue='kind',
    kind='bar',
    col='Time',
    height=6,
    aspect=1.2,
    palette='RdPu'  # Use the same pink palette for consistency
)

# Adjust the layout and add a title
catplot.fig.subplots_adjust(top=0.85)  # Adjust the top margin for the title
catplot.fig.suptitle('Pulse Values by Diet, Exercise Type, and Time', fontsize=16, weight='bold')  # Add a bold title
catplot.set_axis_labels("Diet Type", "Pulse", fontsize=14)  # Set axis labels with larger font
catplot.set_titles("{col_name}", size=14)  # Set column titles with larger font
catplot.set_xticklabels(rotation=45, fontsize=12)  # Rotate x-axis labels for better readability
catplot.set_yticklabels(fontsize=12)  # Increase y-axis label font size

plt.show()

"""
Conclusions:
1. Exercise increases heart rate (pulse), and the type of exercise affects how much the pulse increases.
2. Running causes the highest increase in pulse, followed by walking, while resting has the lowest pulse.
3. A healthy diet (low fat or no fat) combined with exercise helps maintain a healthy heart.
4. This shows the importance of staying active and eating well for a strong and healthy heart!
"""