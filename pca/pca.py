import pandas as pd

df = pd.read_csv('iris.data.csv', header = None, sep = ',')

df.columns = ['sepal_len', 'sepal_wid', 'petal_len', 'petal_wid', 'class']
df.dropna(how = "all", inplace = True) # drops the empty line at file-end

df.tail()
