This quick project is to familiarize myself with pandas, matplotlib, and numpy. I decided to take a look into my doordash orders in the past year to see how much I've spent and which stores I tend to order from.


```python
# Importing needed libraries for analysis
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
```


```python
df = pd.read_csv("consumer_order_details.csv")
```


```python
# Looking at the first few rows of the csv file
df.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>ITEM</th>
      <th>CATEGORY</th>
      <th>STORE_NAME</th>
      <th>UNIT_PRICE</th>
      <th>QUANTITY</th>
      <th>SUBTOTAL</th>
      <th>Unnamed: 6</th>
      <th>Unnamed: 7</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Double Quarter Pounder with Cheese Meal</td>
      <td>Most Popular</td>
      <td>McDonald's</td>
      <td>13.09</td>
      <td>1</td>
      <td>13.09</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1</th>
      <td>French Fries</td>
      <td>Fries, Sides &amp; More</td>
      <td>McDonald's</td>
      <td>5.99</td>
      <td>1</td>
      <td>5.99</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Sunshine Roll (10 pcs)</td>
      <td>Specialty Rolls</td>
      <td>Hibachi Master (5th Ave)</td>
      <td>10.99</td>
      <td>1</td>
      <td>10.99</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Snow White Roll (8 pcs)</td>
      <td>Specialty Rolls</td>
      <td>Hibachi Master (5th Ave)</td>
      <td>10.99</td>
      <td>1</td>
      <td>10.99</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Alaska Roll (6 pcs)</td>
      <td>Specialty Rolls</td>
      <td>Hibachi Master (5th Ave)</td>
      <td>10.99</td>
      <td>1</td>
      <td>10.99</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Removing the last two "Unnamed" columns
df = df.drop(columns="Unnamed: 6")
df = df.drop(columns="Unnamed: 7")
df.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>ITEM</th>
      <th>CATEGORY</th>
      <th>STORE_NAME</th>
      <th>UNIT_PRICE</th>
      <th>QUANTITY</th>
      <th>SUBTOTAL</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Double Quarter Pounder with Cheese Meal</td>
      <td>Most Popular</td>
      <td>McDonald's</td>
      <td>13.09</td>
      <td>1</td>
      <td>13.09</td>
    </tr>
    <tr>
      <th>1</th>
      <td>French Fries</td>
      <td>Fries, Sides &amp; More</td>
      <td>McDonald's</td>
      <td>5.99</td>
      <td>1</td>
      <td>5.99</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Sunshine Roll (10 pcs)</td>
      <td>Specialty Rolls</td>
      <td>Hibachi Master (5th Ave)</td>
      <td>10.99</td>
      <td>1</td>
      <td>10.99</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Snow White Roll (8 pcs)</td>
      <td>Specialty Rolls</td>
      <td>Hibachi Master (5th Ave)</td>
      <td>10.99</td>
      <td>1</td>
      <td>10.99</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Alaska Roll (6 pcs)</td>
      <td>Specialty Rolls</td>
      <td>Hibachi Master (5th Ave)</td>
      <td>10.99</td>
      <td>1</td>
      <td>10.99</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Looking at a quick summary of our doordash orders dataframe
df.info()
```

    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 97 entries, 0 to 96
    Data columns (total 6 columns):
     #   Column      Non-Null Count  Dtype  
    ---  ------      --------------  -----  
     0   ITEM        97 non-null     object 
     1   CATEGORY    97 non-null     object 
     2   STORE_NAME  97 non-null     object 
     3   UNIT_PRICE  97 non-null     float64
     4   QUANTITY    97 non-null     int64  
     5   SUBTOTAL    97 non-null     float64
    dtypes: float64(2), int64(1), object(3)
    memory usage: 4.7+ KB



```python

```
