import pandas as pd



#read_csv
#read_excel
#read_json
df = pd.read_csv('nedbør_smestad.csv', sep=';')



print(df.head(50))

#kolloner
print(df.columns)
#kolloner 
print(df[['Nedbør (mnd)','Tid(norsk normaltid)' ]][0:50])


#printer rader 
#print(df.iloc[1:4])
for i, row in df.iterrows():
    print(i, row['Tid(norsk normaltid)'])

#printer spesefikt sted (R,C)
#print(df.iloc[2,2])