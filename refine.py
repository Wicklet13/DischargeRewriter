import pandas as pd

df = pd.read_csv("data.csv")
refined = df[['note']]
refined.set_index(df['patient_id'])

refined = refined.sample(frac=.4)

print(refined.head())

refined.to_csv("refined.csv")