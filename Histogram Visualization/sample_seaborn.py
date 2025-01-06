import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# Using Seaborn

# Load the sample_ecommerce_dataset.csv file
  data = pd.read_csv('sample_ecommerce_dataset.csv')

# Create DataFrame
df = pd.DataFrame(data)

# Filter data for Credit Card payments
credit_card_df = df[df['Payment_Method'] == 'Credit Card']

# Calculate total sales (Price × Quantity)
credit_card_df['Total_Sales'] = credit_card_df['Price (Rs.)'] * credit_card_df['Quantity']

# Apply Seaborn theme
sns.set_theme(style="whitegrid")

# Plot histograms using Seaborn
plt.figure(figsize=(10, 6))
sns.histplot(
    data=credit_card_df,
    x='Total_Sales',
    hue='Category',
    multiple='stack',  # Stacked histogram
    kde=False,
    bins=10,
    palette='deep'
)

# Customize plot
plt.title('Histogram of Total Sales for Categories Using Credit Card', fontsize=14)
plt.xlabel('Total Sales (Rs.)', fontsize=12)
plt.ylabel('Frequency', fontsize=12)
plt.legend(title='Categories')
plt.tight_layout()

# Show the plot
plt.show()
