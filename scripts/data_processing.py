import pandas as pd

df = pd.read_csv("data/The-Office-Lines-V4.csv")
df = df[df["season"].isin(i for i in range(0, 5))]

with open("data/dialogue.txt", "w") as file:
    for index, row in df.iterrows():
        speaker = row['speaker']
        line = row['line']
        file.write(f"{speaker}:\n{line}\n\n")