# This file is a notebook to explain how the code works
We start importing some libraries to work with data

```python 
import pandas as pd
import numpy as np
```
Now we can import or database

```python 
df = pd.read_csv('credit-data.csv')
```
If  you want see the table 

```python
df.describe()
```
