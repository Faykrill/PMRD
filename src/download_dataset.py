import seaborn as sns
import pandas as pd


df = sns.load_dataset('penguins')
df.to_csv('data/raw/penguins.csv', index=False)

print("Датасет сохранён в data/raw/penguins.csv")