





import pandas as pd
df = pd.read_csv('answerlist.txt', sep='|')

filtered = (df[df['System Answer']=='Answer not found'])

for index, row in filtered.iterrows():
	print(row["Question"])
