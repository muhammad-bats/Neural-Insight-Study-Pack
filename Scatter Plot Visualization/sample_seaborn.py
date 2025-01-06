import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# Using Seaborn

# Load the sample_ecommerce_dataset.csv file
  data = pd.read_csv('sample_ecommerce_dataset.csv')

# Create DataFrame
df = pd.DataFrame(data)

# Filter data for the "Beauty" category
beauty_df = df[df['Category'] == 'Beauty']

# Apply Seaborn theme
sns.set_theme(style="whitegrid")

# Plotting the scatter plot
plt.figure(figsize=(8, 6))
sns.scatterplot(data=beauty_df, x=beauty_df.index, y='Price (Rs.)', hue='Category', palette='deep', s=100, edgecolor='black')
plt.title('Scatter Plot: Prices vs Orders (Beauty Category)', fontsize=14)
plt.xlabel('Order Index', fontsize=12)
plt.ylabel('Price (Rs.)', fontsize=12)

# Customize legend
plt.legend(title='Category', loc='upper left')

# Show the plot
plt.tight_layout()
plt.show()
