import pandas as pd
import matplotlib.pyplot as plt
# Using Matplot

# Load the sample_ecommerce_dataset.csv file
  data = pd.read_csv('sample_ecommerce_dataset.csv')

# Create DataFrame
df = pd.DataFrame(data)

# Convert 'Purchase_Date' to datetime format
df['Purchase_Date'] = pd.to_datetime(df['Purchase_Date'], format='%m/%d/%Y')

# Filter data for Clothing category and date range
filtered_df = df[(df['Category'] == 'Clothing') &
                 (df['Purchase_Date'] >= '2024-03-01') &
                 (df['Purchase_Date'] <= '2024-09-30')]

# Sort data by Purchase_Date
filtered_df = filtered_df.sort_values('Purchase_Date')

# Plotting
plt.plot(filtered_df['Purchase_Date'], filtered_df['Discount (%)'], marker='o', color='blue')
plt.xlabel('Purchase Date')
plt.ylabel('Discount (%)')
plt.title('Discount Trends for Clothing (March - September 2024)')
plt.grid()
plt.tight_layout()

# Show the plot
plt.show()
