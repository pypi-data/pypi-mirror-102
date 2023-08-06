
# JamesBot     ![](https://images.vexels.com/media/users/3/184146/isolated/preview/b3fa5a3182f67f9c4905879aba6fc5a4-colorful-3d-letter-j-by-vexels.png) 

My name is Bot, I'm a [James](https://github.com/felipe-fp/JamesBot).

JamesBot is a python package that download and retain financial data from Yahoo Finance API, making possible to load financial time series previously loaded locally.


## Installation


Install JamesBot package using **pip**:
```
 pip install jamesbot --upgrade
```

## How to use


```python
from jamesbot import *

dl = DataLoader() # creates DataLoader
df = dl.load('AMZN','2014-07-01', '2021-04-01') # loads Amazon's stock price 

print(df) # prints DataFrame

```

