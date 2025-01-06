import pandas as pd
import matplotlib.pyplot as plt
# Using Matplot

# Load the sample_ecommerce_dataset.csv file
  data = pd.read_csv('sample_ecommerce_dataset.csv')

# Create DataFrame
df = pd.DataFrame(data)

# Filter data for Credit Card payments
credit_card_df = df[df['Payment_Method'] == 'Credit Card']

# Calculate total sales (Price × Quantity)
credit_card_df['Total_Sales'] = credit_card_df['Price (Rs.)'] * credit_card_df['Quantity']

# Group data by category
categories = credit_card_df['Category'].unique()

# Plot histograms for each category
plt.figure(figsize=(10, 6))
for category in categories:
    category_data = credit_card_df[credit_card_df['Category'] == category]
    plt.hist(category_data['Total_Sales'], bins=5, alpha=0.7, label=category)

# Customize plot
plt.title('Histogram of Total Sales for Categories Using Credit Card', fontsize=14)
plt.xlabel('Total Sales', fontsize=12)
plt.ylabel('Frequency', fontsize=12)
plt.legend(title='Categories')
plt.grid(alpha=0.3)

# Show the plot
plt.tight_layout()
plt.show()
