import pandas as pd

data = pd.Series(['apple', 'banana', 'apple', 'orange', 'banana', 'apple'])
counts = data.value_counts()
print(data)
print(counts)
