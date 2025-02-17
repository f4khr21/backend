import pandas as pd


data = {
    'Student': ['ahmed', 'mohamed', 'mahmoud', 'marwa', 'sama'],
    'Grade': [85, 70, 90, 50,40],
    'Pass/Fail': ['Pass', 'Pass', 'Pass', 'Fail', 'Fail']
}
df = pd.DataFrame(data)

print("Row with index 1:")
print(df.iloc[1])

df_pass = df[df['Pass/Fail'] == 'Pass']

print("\nFiltered DataFrame with 'Pass':")
print(df_pass)
