# Sequence / string search with NumPy in pandas DataFrames

## pip install a-pandas-ex-sequence-search

### Tested against Windows 10 / Python 3.11 / Anaconda 


```python
import pandas as pd
from a_pandas_ex_sequence_search import pd_add_find_sequence
pd_add_find_sequence()
df = pd.read_csv("https://raw.githubusercontent.com/pandas-dev/pandas/main/doc/data/titanic.csv")
df.Name.s_find_sequence('Mr', exception_val=pd.NA, distance=1)
0     [8]
1     [9]
2      []
3    [10]
4     [7]
5     [7]
6    [10]
7      []
8     [9]
9     [8]
```

