import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# Using Seaborn

# Load the sample_ecommerce_dataset.csv file
  data = pd.read_csv('sample_ecommerce_dataset.csv')

# Create DataFrame
df = pd.DataFrame(data)

# Filter data for the specific User_ID
user_id = 'a83c145c'
filtered_df = df[df['User_ID'] == user_id]

# Count the occurrences of each category for the user
category_counts = filtered_df['Category'].value_counts()

# Apply Seaborn style
sns.set_theme(style="whitegrid")

# Plotting the pie chart
plt.figure(figsize=(8, 6))
plt.pie(category_counts, labels=category_counts.index, autopct='%1.1f%%', startangle=140, colors=sns.color_palette("pastel"))
plt.title(f'Order Categories for User ID: {user_id}')
plt.tight_layout()

# Show the plot
plt.show()
