import pandas as pd
import matplotlib.pyplot as plt


#read_csv
#read_excel
#read_json




#print(df.head(50))

#kolloner
#print(df.columns)
#kolloner 
#print(df[['Nedbør','Tid' ]][0:50])


#printer rader 
#print(df.iloc[1:4])
#for i, row in df.iterrows():
    #print(i, row['Tid'])

#print(df.describe())
#printer spesefikt sted (R,C)
#print(df.iloc[2,2])


#print(df.sort_values('stasjon', ascending=False))


# Leser csv filen
df = pd.read_csv('nedbør_smestad.csv', sep=';', decimal=',')

print(df['Tid'].head)

# konverterer tid til datetime. ellers replacer med NaT
df['Tid'] = pd.to_datetime(df['Tid'], format='%m.%Y', errors='coerce')

# konverter nedbør til numeric eller replacer med NaN
df['Nedbør'] = pd.to_numeric(df['Nedbør'], errors='coerce')


df['Average'] = df['Nedbør'].rolling(window=12).mean()
plt.figure(figsize=(8,5))
plt.plot(df['Tid'], df['Nedbør'], 'r.-', label='Nedbør over tid')
plt.plot(df['Tid'], df['Average'], 'b.-', label='Average Nedbør over tid')  # Plot the average

# Labels
plt.xlabel('Tid')
plt.ylabel('Nedbør')
plt.xticks(rotation=45)

print(df['Tid'].unique())
plt.legend()
plt.show()


# lage average