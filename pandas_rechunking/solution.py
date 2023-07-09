import pandas as pd
from typing import List, Iterator

def convert_to_fixed_size(dataframes: List[pd.DataFrame], fixed_size: int) -> Iterator[pd.DataFrame]:
    # Your code here
    pass


df1 = pd.DataFrame({
    'Name': ['John', 'Jane', 'Mike', 'Emily'],
    'Age': [25, 30, 35, 28],
    'City': ['New York', 'London', 'Paris', 'Sydney']
})

df2 = pd.DataFrame({
    'Name': ['Alex', 'Bob'],
    'Age': [25, 30],
    'City': ['Chicago', 'Madrid']
})

df3 = pd.DataFrame({
    'Name': ['Jack', 'Peter', 'Paul', 'Jacob', 'Isaac', 'Carl', 'Simon', 'Emmy'],
    'Age': [25, 30, 35, 28, 23, 12, 45, 19],
    'City': ['New York', 'London', 'Paris', 'Sydney', 'Washington', 'Cannes', 'Edinburgh', 'Birmingham']
})

dataframes = [df1, df2, df3]  # Replace with your actual DataFrames
fixed_size = 3  # Replace with your desired fixed size

fixed_size_dfs = convert_to_fixed_size(dataframes, fixed_size)

dfs = []
for df in fixed_size_dfs:
    dfs.append(df)

for d in dfs:
    print(d)