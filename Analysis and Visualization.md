# **Data Science**
Data Science is an interdisciplinary field that focuses on extracting meaningful insights and knowledge from structured and unstructured data. By combining techniques from statistics, mathematics, computer science, and domain expertise, data science enables the analysis, interpretation, and visualization of complex datasets. The goal of data science is to uncover patterns, make predictions, and drive decision-making in various domains, from business and healthcare to finance and technology. Leveraging tools like machine learning, data wrangling, and big data processing, it plays a crucial role in solving real-world problems and guiding strategic actions.

At its core, data science encompasses several techniques:
- **Data Visualization**: The graphical representation of data to communicate insights effectively.
- **Data Analysis**: The process of examining datasets to identify patterns and trends.
- **Machine Learning**: Using algorithms to predict outcomes or classify data.

## **Datasets**
Datasets are fundamental collections of data that are carefully organized to facilitate analysis, visualization, and machine learning tasks. In the field of data science, datasets serve as the backbone for deriving meaningful insights, recognizing patterns, and making data-driven decisions. Analysts and data scientists use datasets to explore relationships between variables, test hypotheses, and create predictive models. The organization and quality of the dataset directly impact the success of data analysis and machine learning processes.

Datasets can consist of both **structured** and **unstructured data**, each of which is used differently in data science. **Structured data**, such as tables or spreadsheets, is organized into rows and columns with predefined features and attributes. It is the easiest form to analyze and visualize, often through charts, graphs, or pivot tables. Examples include financial data, customer demographics, or scientific measurements. On the other hand, **unstructured data**, which includes images, text, and audio, is more complex and may require additional preprocessing steps.

Regardless of the type, datasets are the starting point for data analysis and visualization, driving the exploration and interpretation of data in various scientific and business applications.

### Public Dataset Repositories
Public dataset repositories provide valuable resources for researchers, data scientists, and developers by offering free access to large collections of diverse datasets. These platforms not only facilitate the development and testing of machine learning models but also help accelerate research across a variety of domains.

Numerous platforms offer publicly available datasets for research and development. Some popular repositories include:
- **Kaggle Datasets**: Kaggle provides a wide range of datasets across domains like healthcare, finance, sports, and e-commerce.
- **Hugging Face Datasets**: Hugging Face offers diverse datasets for NLP, vision, and audio tasks, with easy integration into machine learning workflows

### Loading Datasets
Loading datasets is a crucial step in data analysis and machine learning, as it enables you to access and work with the data for further processing, analysis, or model training. There are several ways to load datasets, depending on the format and the source.

1. **Downloading and Organizing Datasets Locally**
If you're using a dataset from a public repository (like Kaggle or Hugging Face), you can download it manually to your local machine. Once downloaded, you should organize the files into appropriate directories (e.g., separating training and validation sets) to make them easier to use.

2. **Loading Datasets with Python**
Many datasets can be directly downloaded and loaded into your Python environment using libraries such as `requests`, `urllib`, or specialized libraries like `datasets` for Hugging Face, or `kaggle` for Kaggle datasets. This eliminates the need for manual downloading and organizing.

To use Kaggle datasets with the `kaggle` Python library, you first need to sign up on [Kaggle](https://www.kaggle.com/) and obtain your API credentials. These credentials are required to authenticate your requests when using the Kaggle API.

After obtaining your API credentials, ensure that the kaggle library is installed in your Conda Python environment. To do this, run the following command in the Anaconda Prompt or your terminal:  
```bash
  pip install kaggle
```
> Refer to the `Artificial Intelligence and Computer Vision` branch for more information on Conda Environments.

Once the library is installed, you can download a dataset from Kaggle using the following Python script:
```python
  import kaggle

  # Set up your Kaggle API key (ensure it is properly set up in your environment)
  # Download the dataset
  kaggle.api.dataset_download_files('dataset-owner/dataset-name', path='your/destination/folder', unzip=True)
```
Replace `'dataset-owner/dataset-name'` with the appropriate Kaggle dataset identifier, and `'your/destination/folder'` with the local directory where you want the dataset to be saved. This script will download the dataset and automatically unzip it for use in your environment.

Downloaded Datasets stored as CSV or Excel files can then be loaded directly into your Python Environment using appropriate libraries like `pandas` for tabular data.
```python
  import pandas as pd

  # Load the CSV file
  data = pd.read_csv('path/to/your/dataset.csv')
```
This Python code snippet utilizes the `pandas` library to load data from a CSV file into a DataFrame, which is a two-dimensional, size-mutable, and potentially heterogeneous tabular data structure with labeled axes (rows and columns). In pandas, a DataFrame is a primary data structure used for data manipulation and analysis. It allows for efficient data handling and provides various functionalities to analyze and manipulate the data.

Once your Dataset is loaded into your Python Environment as a DataFrame, you can use it for Data Analysis and Visualization.

# **Data Visualization**
Data Visualization is a key component of data science that involves representing data graphically to uncover patterns, trends, and insights. It transforms raw data into visual formats like charts, graphs, and maps, making complex datasets easier to interpret and understand. By leveraging visual representations, data visualization helps communicate information effectively, enabling both technical and non-technical audiences to grasp key findings.

Applications of data visualization span various fields, including tracking sales trends in business, monitoring health metrics in healthcare, and analyzing user behavior in technology. It plays a crucial role in decision-making processes by providing clear and actionable insights from data.

## **Data Visualization Techniques**
Data visualization techniques are methods used to represent datasets graphically, used to uncover trends, patterns, and relationships within the data. Different techniques serve different purposes, whether it’s comparing categories, analyzing trends, or visualizing distributions. Selecting the right visualization is crucial for effectively conveying insights.

Data visualization uses Python libraries such as `Matplotlib` and `Seaborn` to help users create charts, graphs, and other visual representations of data.

This guide features a sample e-commerce dataset sourced from **Kaggle**, provided in the repository as `sample_ecommerce_dataset.csv`. To practice data visualization, it is recommended to either download the dataset or clone the repository via Git to practice locally. 

Before proceeding with visualizations, the dataset must be imported into the Python environment. This involves loading it into a structured format, such as a Pandas DataFrame, enabling efficient data manipulation, analysis, and visualization.
```python
  import pandas as pd

  # Load the sample_ecommerce_dataset.csv file
  data = pd.read_csv('sample_ecommerce_dataset.csv')  #if the dataset.csv file and your script is in the same directory then you do not need to specify the complete path

  # Create DataFrame
  df = pd.DataFrame(data)

  # Display the DataFrame
  print(df)
```
This Python script loads the dataset and stores it in a Pandas DataFrame `df`, making it ready for analysis and visualization tasks.

### **Bar Chart Visualization**
Bar charts are a simple yet effective way to visualize categorical data, showing the distribution of data points across different categories. They are often used to compare quantities or frequencies between discrete categories, making it easy to identify patterns or differences.

Here are examples of how to plot a bar chart using both Matplotlib and Seaborn for the e-commerce dataset, specifically for the total quantity sold with each payment_method.
```python
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
```

```python
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
```

### **Line Chart Visualization**
Line charts are useful for visualizing trends over a continuous range, such as time or ordered categories. They are particularly effective when you want to highlight relationships between two variables or show changes in a variable over time or categories.

This example, plots line graphs of discounts for the "Clothing" category in the dataset against time, considering only the data from March 2024 to September 2024
```python
  import pandas as pd
  import matplotlib.pyplot as plt
  
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
```

```python
  import pandas as pd
  import seaborn as sns
  import matplotlib.pyplot as plt
  # Using Seaborn
  
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
  
  # Plotting with Seaborn
  sns.lineplot(x='Purchase_Date', y='Discount (%)', data=filtered_df, marker='o', color='purple')
  plt.xlabel('Purchase Date')
  plt.ylabel('Discount (%)')
  plt.title('Discount Trends for Clothing (March - September 2024)')
  plt.xticks(rotation=45)
  plt.grid()
  plt.tight_layout()
  
  # Show the plot
  plt.show()
```

### **Pie Chart Visualization**
Pie charts are used to represent data as proportional slices of a whole, making it easy to see the relative size of categories.

This example visualizes the proportion of categories from all orders of a specific user (*a83c145c*)
```python
  import pandas as pd
  import matplotlib.pyplot as plt
  # Using Matplot
  
  # Load the sample_ecommerce_dataset.csv file
  data = pd.read_csv('sample_ecommerce_dataset.csv')
  
  # Create DataFrame
  df = pd.DataFrame(data)
  
  # Filter data for the specific User_ID
  user_id = 'a83c145c'
  filtered_df = df[df['User_ID'] == user_id]
  
  # Count the occurrences of each category for the user
  category_counts = filtered_df['Category'].value_counts()
  
  # Plotting the pie chart
  plt.figure(figsize=(8, 6))
  plt.pie(category_counts, labels=category_counts.index, autopct='%1.1f%%', startangle=140, colors=plt.cm.Paired.colors)
  plt.title(f'Order Categories for User ID: {user_id}')
  plt.tight_layout()
  
  # Show the plot
  plt.show()
```

```python
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
```

### **Scatter Plot Visualization**
Scatter plots are used to visualize relationships or correlations between two continuous variables.

This example analyzes the relationship between the prices and all orders in the Beauty category.
```python
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
```

```python
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
```

### **Histogram Visualization**
Histograms are used to display the distribution of a single variable by dividing it into intervals or bins.

In this example, we will visualize the total sales (calculated as price × quantity) for each category that used *Credit Card* payment_method, in the dataset.
```python
```

```python
```

This repository has directories made for each Visualization Technique discussed, the directories contain sample python files for matplot and seaborn which were discussed in the guide. 
For additional information and hands-on practice with these Python libraries, refer to their official documentation. These resources provide comprehensive guides, examples, and best practices to help you master data visualization using libraries like Matplotlib and Seaborn.
- [Matplotlib - Visualization with Python](https://matplotlib.org)
- [Seaborn - Statistical Data Visualization](https://seaborn.pydata.org)
