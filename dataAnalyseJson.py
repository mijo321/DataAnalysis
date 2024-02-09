import pandas as pd
import matplotlib.pyplot as plt
import json
import numpy as np
import seaborn as sns

with open('13931_20240207-132511.json') as f:
    data = json.load(f)

values = data['dataset']['value']
tid = data['dataset']['dimension']['Tid']['category']['label']
tidsperiode = data['dataset']['dimension']['Tid']['category']['index']
forskjelligeTyper = data['dataset']['dimension']['UtslpTilLuft']['category']['label']

values_per_type = 33
num_types = len(forskjelligeTyper)
chunks = [values[i*values_per_type:(i+1)*values_per_type] for i in range(num_types)]


tiden = [tid[year] for year, index in tidsperiode.items()]


fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(16, 8))


colors = ['b', 'g', 'r', 'c', 'm', 'y', 'tab:purple', ]


for i, (typer, verdi) in enumerate(zip(forskjelligeTyper, chunks)):
    ax1.plot(tiden, verdi, color=colors[i % len(colors)], label=f'{forskjelligeTyper[typer]} co2 utslipp total')
ax1.set_xlabel('Tid')
ax1.set_ylabel('co2')
ax1.legend()

sns.set_theme()


totals = [sum(chunk) for chunk in chunks[1:]]  
labels = list(forskjelligeTyper.values())[1:]  
ax2.pie(totals, labels=labels, autopct='%1.1f%%', colors=colors[1:])

plt.tight_layout()
plt.show()
