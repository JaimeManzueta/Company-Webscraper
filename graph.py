import matplotlib.pyplot as plt
import pandas as pd

# Read the CSV file
companies = pd.read_csv("companies.csv")


company_names = companies['Name']
company_rev  = companies['Revenue (USD millions)']

# Create a bar chart
plt.xlabel('Name',fontsize = 6)
plt.ylabel('Revenue (USD millions)', fontsize = 6)
plt.bar(company_names,company_rev)
# Customize the plot if needed


# Show the plot
plt.show()


