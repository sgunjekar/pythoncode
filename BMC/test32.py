import pandas as pd

lists = [[1, 7, 11], [2, 8, 12], [4, 9, 13], [5, 10, 14]]

# Create a DataFrame
df = pd.DataFrame(lists)

# Stack to flatten column-wise, then sort
result = df.stack().sort_values().tolist()

print(result)