import pandas as pd
# Using Matplot

# Load the sample_ecommerce_dataset.csv file
data = pd.read_csv('sample_ecommerce_dataset.csv')

# Create DataFrame
df = pd.DataFrame(data)

# Count orders by Payment_Method
payment_method_counts = df['Payment_Method'].value_counts()

# Plotting
plt.bar(payment_method_counts.index, payment_method_counts.values, color='skyblue')
plt.xlabel('Payment Method')
plt.ylabel('Number of Orders')
plt.title('Orders by Payment Method')
plt.xticks(rotation=45)
plt.tight_layout()

# Show the plot
plt.show()
