import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
# Using Seaborn

# Load the sample_ecommerce_dataset.csv file
data = pd.read_csv('sample_ecommerce_dataset.csv')

# Create DataFrame
df = pd.DataFrame(data)

# Count orders by Payment_Method
payment_method_counts = df['Payment_Method'].value_counts().reset_index()
payment_method_counts.columns = ['Payment_Method', 'Number_of_Orders']

# Plotting with Seaborn
sns.barplot(x='Payment_Method', y='Number_of_Orders', data=payment_method_counts, palette='viridis')
plt.xlabel('Payment Method')
plt.ylabel('Number of Orders')
plt.title('Orders by Payment Method')
plt.xticks(rotation=45)
plt.tight_layout()

# Show the plot
plt.show()
