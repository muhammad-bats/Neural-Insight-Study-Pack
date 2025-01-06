import pandas as pd
import matplotlib.pyplot as plt
# Using Matplot

# Load the sample_ecommerce_dataset.csv file
  data = pd.read_csv('sample_ecommerce_dataset.csv')

# Create DataFrame
df = pd.DataFrame(data)

# Filter data for the "Beauty" category
beauty_df = df[df['Category'] == 'Beauty']

# Plotting the scatter plot
plt.figure(figsize=(8, 6))
plt.scatter(beauty_df.index, beauty_df['Price (Rs.)'], color='blue', edgecolors='black', alpha=0.7)
plt.title('Scatter Plot: Prices vs Orders (Beauty Category)', fontsize=14)
plt.xlabel('Order Index', fontsize=12)
plt.ylabel('Price (Rs.)', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.5)

# Annotating points (optional)
for i, price in enumerate(beauty_df['Price (Rs.)']):
    plt.text(beauty_df.index[i], price + 20, f'Rs.{price}', fontsize=8, ha='center')

# Show the plot
plt.tight_layout()
plt.show()
