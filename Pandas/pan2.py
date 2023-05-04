import pandas as pd

my_dict = {
    'car': ['lamborghini', 'ultima', 'diablo'],
    'cost': [10000, 50000, 60000]
}

df = pd.DataFrame(my_dict)

print(df.head())

print('Average cost car:', df['cost'].mean())
