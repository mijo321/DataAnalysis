import pandas as pd
import matplotlib.pyplot as plt

# Define a date parser
date_parser = lambda x: pd.to_datetime(x, format="%m.%Y")

# Read the Excel file and parse 'Tid' as dates
df = pd.read_excel('nedbør_smestad.xlsx', parse_dates=['Tid'], date_parser=date_parser)

# Set 'Tid' as the index
df.set_index('Tid', inplace=True)

# Convert 'Nedbør' to numeric, replacing errors with NaN
df['Nedbør'] = pd.to_numeric(df['Nedbør'], errors='coerce')


# Calculate the rolling average rainfall
df['Average'] = df['Nedbør'].rolling(window=12).mean()

# PlOTTING
plt.figure(figsize=(8,5))
plt.plot(df.index, df['Nedbør'], 'r_-', label='Nedbør over tid')
plt.plot(df.index, df['Average'], 'b*-', label='Average Nedbør over tid')  


# Labels
plt.xlabel('Tid')
plt.ylabel('Nedbør')
plt.xticks(rotation=45)

plt.legend()
plt.show()

# elsker deg <3333

