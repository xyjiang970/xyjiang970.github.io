Purpose of this project is to look into some covid statistics.


```python
# Importing needed libraries for data analysis.

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
```


```python
# Loading "Our World in Data's" Covid csv file into a dataframe.

df = pd.read_csv('owid-covid-data.csv')
```


```python
# Taking a look at what our dataframe looks like.

df
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
      <th>iso_code</th>
      <th>continent</th>
      <th>location</th>
      <th>date</th>
      <th>total_cases</th>
      <th>new_cases</th>
      <th>new_cases_smoothed</th>
      <th>total_deaths</th>
      <th>new_deaths</th>
      <th>new_deaths_smoothed</th>
      <th>...</th>
      <th>extreme_poverty</th>
      <th>cardiovasc_death_rate</th>
      <th>diabetes_prevalence</th>
      <th>female_smokers</th>
      <th>male_smokers</th>
      <th>handwashing_facilities</th>
      <th>hospital_beds_per_thousand</th>
      <th>life_expectancy</th>
      <th>human_development_index</th>
      <th>excess_mortality</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>AFG</td>
      <td>Asia</td>
      <td>Afghanistan</td>
      <td>2020-02-24</td>
      <td>5.0</td>
      <td>5.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>597.029</td>
      <td>9.59</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>37.746</td>
      <td>0.5</td>
      <td>64.83</td>
      <td>0.511</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1</th>
      <td>AFG</td>
      <td>Asia</td>
      <td>Afghanistan</td>
      <td>2020-02-25</td>
      <td>5.0</td>
      <td>0.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>597.029</td>
      <td>9.59</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>37.746</td>
      <td>0.5</td>
      <td>64.83</td>
      <td>0.511</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>AFG</td>
      <td>Asia</td>
      <td>Afghanistan</td>
      <td>2020-02-26</td>
      <td>5.0</td>
      <td>0.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>597.029</td>
      <td>9.59</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>37.746</td>
      <td>0.5</td>
      <td>64.83</td>
      <td>0.511</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3</th>
      <td>AFG</td>
      <td>Asia</td>
      <td>Afghanistan</td>
      <td>2020-02-27</td>
      <td>5.0</td>
      <td>0.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>597.029</td>
      <td>9.59</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>37.746</td>
      <td>0.5</td>
      <td>64.83</td>
      <td>0.511</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4</th>
      <td>AFG</td>
      <td>Asia</td>
      <td>Afghanistan</td>
      <td>2020-02-28</td>
      <td>5.0</td>
      <td>0.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>597.029</td>
      <td>9.59</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>37.746</td>
      <td>0.5</td>
      <td>64.83</td>
      <td>0.511</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>118129</th>
      <td>ZWE</td>
      <td>Africa</td>
      <td>Zimbabwe</td>
      <td>2021-09-16</td>
      <td>127368.0</td>
      <td>285.0</td>
      <td>187.429</td>
      <td>4560.0</td>
      <td>9.0</td>
      <td>5.571</td>
      <td>...</td>
      <td>21.4</td>
      <td>307.846</td>
      <td>1.82</td>
      <td>1.6</td>
      <td>30.7</td>
      <td>36.791</td>
      <td>1.7</td>
      <td>61.49</td>
      <td>0.571</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>118130</th>
      <td>ZWE</td>
      <td>Africa</td>
      <td>Zimbabwe</td>
      <td>2021-09-17</td>
      <td>127632.0</td>
      <td>264.0</td>
      <td>209.857</td>
      <td>4562.0</td>
      <td>2.0</td>
      <td>4.286</td>
      <td>...</td>
      <td>21.4</td>
      <td>307.846</td>
      <td>1.82</td>
      <td>1.6</td>
      <td>30.7</td>
      <td>36.791</td>
      <td>1.7</td>
      <td>61.49</td>
      <td>0.571</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>118131</th>
      <td>ZWE</td>
      <td>Africa</td>
      <td>Zimbabwe</td>
      <td>2021-09-18</td>
      <td>127739.0</td>
      <td>107.0</td>
      <td>217.000</td>
      <td>4563.0</td>
      <td>1.0</td>
      <td>3.857</td>
      <td>...</td>
      <td>21.4</td>
      <td>307.846</td>
      <td>1.82</td>
      <td>1.6</td>
      <td>30.7</td>
      <td>36.791</td>
      <td>1.7</td>
      <td>61.49</td>
      <td>0.571</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>118132</th>
      <td>ZWE</td>
      <td>Africa</td>
      <td>Zimbabwe</td>
      <td>2021-09-19</td>
      <td>127938.0</td>
      <td>199.0</td>
      <td>238.429</td>
      <td>4567.0</td>
      <td>4.0</td>
      <td>4.143</td>
      <td>...</td>
      <td>21.4</td>
      <td>307.846</td>
      <td>1.82</td>
      <td>1.6</td>
      <td>30.7</td>
      <td>36.791</td>
      <td>1.7</td>
      <td>61.49</td>
      <td>0.571</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>118133</th>
      <td>ZWE</td>
      <td>Africa</td>
      <td>Zimbabwe</td>
      <td>2021-09-20</td>
      <td>128186.0</td>
      <td>248.0</td>
      <td>255.286</td>
      <td>4569.0</td>
      <td>2.0</td>
      <td>3.714</td>
      <td>...</td>
      <td>21.4</td>
      <td>307.846</td>
      <td>1.82</td>
      <td>1.6</td>
      <td>30.7</td>
      <td>36.791</td>
      <td>1.7</td>
      <td>61.49</td>
      <td>0.571</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
<p>118134 rows × 62 columns</p>
</div>




```python
# Taking a look at the summary of our datafram (specifically the values and columns).

df.info(verbose = True)
```

    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 118134 entries, 0 to 118133
    Data columns (total 62 columns):
     #   Column                                 Non-Null Count   Dtype  
    ---  ------                                 --------------   -----  
     0   iso_code                               118134 non-null  object 
     1   continent                              112736 non-null  object 
     2   location                               118134 non-null  object 
     3   date                                   118134 non-null  object 
     4   total_cases                            112287 non-null  float64
     5   new_cases                              112284 non-null  float64
     6   new_cases_smoothed                     111269 non-null  float64
     7   total_deaths                           101591 non-null  float64
     8   new_deaths                             101746 non-null  float64
     9   new_deaths_smoothed                    111269 non-null  float64
     10  total_cases_per_million                111695 non-null  float64
     11  new_cases_per_million                  111692 non-null  float64
     12  new_cases_smoothed_per_million         110682 non-null  float64
     13  total_deaths_per_million               101012 non-null  float64
     14  new_deaths_per_million                 101167 non-null  float64
     15  new_deaths_smoothed_per_million        110682 non-null  float64
     16  reproduction_rate                      94434 non-null   float64
     17  icu_patients                           13351 non-null   float64
     18  icu_patients_per_million               13351 non-null   float64
     19  hosp_patients                          15319 non-null   float64
     20  hosp_patients_per_million              15319 non-null   float64
     21  weekly_icu_admissions                  1178 non-null    float64
     22  weekly_icu_admissions_per_million      1178 non-null    float64
     23  weekly_hosp_admissions                 2147 non-null    float64
     24  weekly_hosp_admissions_per_million     2147 non-null    float64
     25  new_tests                              51338 non-null   float64
     26  total_tests                            51205 non-null   float64
     27  total_tests_per_thousand               51205 non-null   float64
     28  new_tests_per_thousand                 51338 non-null   float64
     29  new_tests_smoothed                     60886 non-null   float64
     30  new_tests_smoothed_per_thousand        60886 non-null   float64
     31  positive_rate                          57623 non-null   float64
     32  tests_per_case                         56996 non-null   float64
     33  tests_units                            62772 non-null   object 
     34  total_vaccinations                     26180 non-null   float64
     35  people_vaccinated                      25042 non-null   float64
     36  people_fully_vaccinated                22031 non-null   float64
     37  total_boosters                         2345 non-null    float64
     38  new_vaccinations                       21696 non-null   float64
     39  new_vaccinations_smoothed              46739 non-null   float64
     40  total_vaccinations_per_hundred         26180 non-null   float64
     41  people_vaccinated_per_hundred          25042 non-null   float64
     42  people_fully_vaccinated_per_hundred    22031 non-null   float64
     43  total_boosters_per_hundred             2345 non-null    float64
     44  new_vaccinations_smoothed_per_million  46739 non-null   float64
     45  stringency_index                       98473 non-null   float64
     46  population                             117328 non-null  float64
     47  population_density                     109231 non-null  float64
     48  median_age                             104392 non-null  float64
     49  aged_65_older                          103230 non-null  float64
     50  aged_70_older                          103819 non-null  float64
     51  gdp_per_capita                         105003 non-null  float64
     52  extreme_poverty                        70510 non-null   float64
     53  cardiovasc_death_rate                  104688 non-null  float64
     54  diabetes_prevalence                    107869 non-null  float64
     55  female_smokers                         81759 non-null   float64
     56  male_smokers                           80571 non-null   float64
     57  handwashing_facilities                 52591 non-null   float64
     58  hospital_beds_per_thousand             95208 non-null   float64
     59  life_expectancy                        112063 non-null  float64
     60  human_development_index                104783 non-null  float64
     61  excess_mortality                       4200 non-null    float64
    dtypes: float64(57), object(5)
    memory usage: 55.9+ MB



```python
# Filtering by the most recent date when this project is started, which is Aug. 15th, 2021

most_recent_date = df[df['date'] == '2021-08-30']

# Top tourist destinations and most populus countries in Asia, Europe, and North America
countries = ['France','Spain','United States','Italy','Turkey', 'Malaysia',
             'Mexico','Taiwan','Germany','United Kingdom','Cuba','Canada',
             'Japan','South Korea','Netherlands','India','Guatemala','Haiti',]

countries_of_interest = most_recent_date[most_recent_date['location'].isin(countries)]
```


```python
# Let's see what that looks like (only looking into the first 10 rows):

countries_of_interest
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
      <th>iso_code</th>
      <th>continent</th>
      <th>location</th>
      <th>date</th>
      <th>total_cases</th>
      <th>new_cases</th>
      <th>new_cases_smoothed</th>
      <th>total_deaths</th>
      <th>new_deaths</th>
      <th>new_deaths_smoothed</th>
      <th>...</th>
      <th>extreme_poverty</th>
      <th>cardiovasc_death_rate</th>
      <th>diabetes_prevalence</th>
      <th>female_smokers</th>
      <th>male_smokers</th>
      <th>handwashing_facilities</th>
      <th>hospital_beds_per_thousand</th>
      <th>life_expectancy</th>
      <th>human_development_index</th>
      <th>excess_mortality</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>19730</th>
      <td>CAN</td>
      <td>North America</td>
      <td>Canada</td>
      <td>2021-08-30</td>
      <td>1504157.0</td>
      <td>6874.0</td>
      <td>3245.571</td>
      <td>26972.0</td>
      <td>18.0</td>
      <td>22.429</td>
      <td>...</td>
      <td>0.5</td>
      <td>105.599</td>
      <td>7.37</td>
      <td>12.0</td>
      <td>16.6</td>
      <td>NaN</td>
      <td>2.50</td>
      <td>82.43</td>
      <td>0.929</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>26817</th>
      <td>CUB</td>
      <td>North America</td>
      <td>Cuba</td>
      <td>2021-08-30</td>
      <td>646513.0</td>
      <td>6075.0</td>
      <td>7699.143</td>
      <td>5219.0</td>
      <td>75.0</td>
      <td>85.857</td>
      <td>...</td>
      <td>NaN</td>
      <td>190.968</td>
      <td>8.27</td>
      <td>17.1</td>
      <td>53.3</td>
      <td>85.198</td>
      <td>5.20</td>
      <td>78.80</td>
      <td>0.783</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>38796</th>
      <td>FRA</td>
      <td>Europe</td>
      <td>France</td>
      <td>2021-08-30</td>
      <td>6834998.0</td>
      <td>7688.0</td>
      <td>18101.286</td>
      <td>114778.0</td>
      <td>151.0</td>
      <td>120.000</td>
      <td>...</td>
      <td>NaN</td>
      <td>86.060</td>
      <td>4.77</td>
      <td>30.1</td>
      <td>35.6</td>
      <td>NaN</td>
      <td>5.98</td>
      <td>82.66</td>
      <td>0.901</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>41309</th>
      <td>DEU</td>
      <td>Europe</td>
      <td>Germany</td>
      <td>2021-08-30</td>
      <td>3947035.0</td>
      <td>6823.0</td>
      <td>9343.143</td>
      <td>92208.0</td>
      <td>62.0</td>
      <td>25.714</td>
      <td>...</td>
      <td>NaN</td>
      <td>156.139</td>
      <td>8.31</td>
      <td>28.2</td>
      <td>33.1</td>
      <td>NaN</td>
      <td>8.00</td>
      <td>81.33</td>
      <td>0.947</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>44061</th>
      <td>GTM</td>
      <td>North America</td>
      <td>Guatemala</td>
      <td>2021-08-30</td>
      <td>465799.0</td>
      <td>740.0</td>
      <td>3684.571</td>
      <td>11886.0</td>
      <td>28.0</td>
      <td>52.857</td>
      <td>...</td>
      <td>8.7</td>
      <td>155.898</td>
      <td>10.18</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>76.665</td>
      <td>0.60</td>
      <td>74.30</td>
      <td>0.663</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>46511</th>
      <td>HTI</td>
      <td>North America</td>
      <td>Haiti</td>
      <td>2021-08-30</td>
      <td>20850.0</td>
      <td>17.0</td>
      <td>18.714</td>
      <td>584.0</td>
      <td>0.0</td>
      <td>0.143</td>
      <td>...</td>
      <td>23.5</td>
      <td>430.548</td>
      <td>6.65</td>
      <td>2.9</td>
      <td>23.1</td>
      <td>22.863</td>
      <td>0.70</td>
      <td>64.00</td>
      <td>0.510</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>49417</th>
      <td>IND</td>
      <td>Asia</td>
      <td>India</td>
      <td>2021-08-30</td>
      <td>32768880.0</td>
      <td>30941.0</td>
      <td>42015.286</td>
      <td>438560.0</td>
      <td>350.0</td>
      <td>492.857</td>
      <td>...</td>
      <td>21.2</td>
      <td>282.280</td>
      <td>10.39</td>
      <td>1.9</td>
      <td>20.6</td>
      <td>59.550</td>
      <td>0.53</td>
      <td>69.66</td>
      <td>0.645</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>53723</th>
      <td>ITA</td>
      <td>Europe</td>
      <td>Italy</td>
      <td>2021-08-30</td>
      <td>4534499.0</td>
      <td>4253.0</td>
      <td>6531.429</td>
      <td>129146.0</td>
      <td>53.0</td>
      <td>50.143</td>
      <td>...</td>
      <td>2.0</td>
      <td>113.151</td>
      <td>4.78</td>
      <td>19.8</td>
      <td>27.8</td>
      <td>NaN</td>
      <td>3.18</td>
      <td>83.51</td>
      <td>0.892</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>54890</th>
      <td>JPN</td>
      <td>Asia</td>
      <td>Japan</td>
      <td>2021-08-30</td>
      <td>1473847.0</td>
      <td>13625.0</td>
      <td>21526.143</td>
      <td>16016.0</td>
      <td>47.0</td>
      <td>47.857</td>
      <td>...</td>
      <td>NaN</td>
      <td>79.370</td>
      <td>5.72</td>
      <td>11.2</td>
      <td>33.7</td>
      <td>NaN</td>
      <td>13.05</td>
      <td>84.63</td>
      <td>0.919</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>65524</th>
      <td>MYS</td>
      <td>Asia</td>
      <td>Malaysia</td>
      <td>2021-08-30</td>
      <td>1725357.0</td>
      <td>19268.0</td>
      <td>21798.857</td>
      <td>16382.0</td>
      <td>295.0</td>
      <td>291.429</td>
      <td>...</td>
      <td>0.1</td>
      <td>260.942</td>
      <td>16.74</td>
      <td>1.0</td>
      <td>42.4</td>
      <td>NaN</td>
      <td>1.90</td>
      <td>76.16</td>
      <td>0.810</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>69289</th>
      <td>MEX</td>
      <td>North America</td>
      <td>Mexico</td>
      <td>2021-08-30</td>
      <td>3341264.0</td>
      <td>5564.0</td>
      <td>15664.000</td>
      <td>258491.0</td>
      <td>326.0</td>
      <td>709.286</td>
      <td>...</td>
      <td>2.5</td>
      <td>152.783</td>
      <td>13.06</td>
      <td>6.9</td>
      <td>21.4</td>
      <td>87.847</td>
      <td>1.38</td>
      <td>75.05</td>
      <td>0.779</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>75561</th>
      <td>NLD</td>
      <td>Europe</td>
      <td>Netherlands</td>
      <td>2021-08-30</td>
      <td>1973984.0</td>
      <td>2271.0</td>
      <td>2660.143</td>
      <td>18348.0</td>
      <td>6.0</td>
      <td>9.571</td>
      <td>...</td>
      <td>NaN</td>
      <td>109.361</td>
      <td>5.29</td>
      <td>24.4</td>
      <td>27.3</td>
      <td>NaN</td>
      <td>3.32</td>
      <td>82.28</td>
      <td>0.944</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>99373</th>
      <td>KOR</td>
      <td>Asia</td>
      <td>South Korea</td>
      <td>2021-08-30</td>
      <td>251421.0</td>
      <td>1370.0</td>
      <td>1733.429</td>
      <td>2285.0</td>
      <td>1.0</td>
      <td>8.143</td>
      <td>...</td>
      <td>0.2</td>
      <td>85.998</td>
      <td>6.80</td>
      <td>6.2</td>
      <td>40.9</td>
      <td>NaN</td>
      <td>12.27</td>
      <td>83.03</td>
      <td>0.916</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>100505</th>
      <td>ESP</td>
      <td>Europe</td>
      <td>Spain</td>
      <td>2021-08-30</td>
      <td>4847298.0</td>
      <td>15489.0</td>
      <td>7563.714</td>
      <td>84146.0</td>
      <td>146.0</td>
      <td>115.571</td>
      <td>...</td>
      <td>1.0</td>
      <td>99.403</td>
      <td>7.17</td>
      <td>27.4</td>
      <td>31.4</td>
      <td>NaN</td>
      <td>2.97</td>
      <td>83.56</td>
      <td>0.904</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>104556</th>
      <td>TWN</td>
      <td>Asia</td>
      <td>Taiwan</td>
      <td>2021-08-30</td>
      <td>15991.0</td>
      <td>8.0</td>
      <td>8.429</td>
      <td>834.0</td>
      <td>0.0</td>
      <td>0.857</td>
      <td>...</td>
      <td>NaN</td>
      <td>103.957</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>80.46</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>109230</th>
      <td>TUR</td>
      <td>Asia</td>
      <td>Turkey</td>
      <td>2021-08-30</td>
      <td>6366408.0</td>
      <td>19557.0</td>
      <td>18845.429</td>
      <td>56458.0</td>
      <td>245.0</td>
      <td>241.857</td>
      <td>...</td>
      <td>0.2</td>
      <td>171.285</td>
      <td>12.13</td>
      <td>14.1</td>
      <td>41.1</td>
      <td>NaN</td>
      <td>2.81</td>
      <td>77.69</td>
      <td>0.820</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>111935</th>
      <td>GBR</td>
      <td>Europe</td>
      <td>United Kingdom</td>
      <td>2021-08-30</td>
      <td>6789189.0</td>
      <td>26285.0</td>
      <td>33395.714</td>
      <td>132808.0</td>
      <td>48.0</td>
      <td>115.429</td>
      <td>...</td>
      <td>0.2</td>
      <td>122.137</td>
      <td>4.28</td>
      <td>20.0</td>
      <td>24.7</td>
      <td>NaN</td>
      <td>2.54</td>
      <td>81.32</td>
      <td>0.932</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>112543</th>
      <td>USA</td>
      <td>North America</td>
      <td>United States</td>
      <td>2021-08-30</td>
      <td>39150680.0</td>
      <td>259936.0</td>
      <td>159486.000</td>
      <td>639737.0</td>
      <td>1772.0</td>
      <td>1354.714</td>
      <td>...</td>
      <td>1.2</td>
      <td>151.089</td>
      <td>10.79</td>
      <td>19.1</td>
      <td>24.6</td>
      <td>NaN</td>
      <td>2.77</td>
      <td>78.86</td>
      <td>0.926</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
<p>18 rows × 62 columns</p>
</div>




```python
# Creating a new DF with only the columns needed for now.

# The specific columns we are looking to use are:

# 1 -> continent
# 2 -> location (country)
# 4 -> total_cases
# 7 -> total_deaths
# 31 -> positive_rate
# 36 -> people_fully_vaccinated
# 45 -> stringency_index
# 46 -> population
# 59 -> life_expectancy
# 60 -> human_development_index

data = countries_of_interest.iloc[:,[1,2,4,7,36,31,45,46,59,60]] 

# Using iloc here because it is more efficient than typing out each name of the column.
```


```python
for i, j in enumerate(df.columns):
    print(i,j)
```

    0 iso_code
    1 continent
    2 location
    3 date
    4 total_cases
    5 new_cases
    6 new_cases_smoothed
    7 total_deaths
    8 new_deaths
    9 new_deaths_smoothed
    10 total_cases_per_million
    11 new_cases_per_million
    12 new_cases_smoothed_per_million
    13 total_deaths_per_million
    14 new_deaths_per_million
    15 new_deaths_smoothed_per_million
    16 reproduction_rate
    17 icu_patients
    18 icu_patients_per_million
    19 hosp_patients
    20 hosp_patients_per_million
    21 weekly_icu_admissions
    22 weekly_icu_admissions_per_million
    23 weekly_hosp_admissions
    24 weekly_hosp_admissions_per_million
    25 new_tests
    26 total_tests
    27 total_tests_per_thousand
    28 new_tests_per_thousand
    29 new_tests_smoothed
    30 new_tests_smoothed_per_thousand
    31 positive_rate
    32 tests_per_case
    33 tests_units
    34 total_vaccinations
    35 people_vaccinated
    36 people_fully_vaccinated
    37 total_boosters
    38 new_vaccinations
    39 new_vaccinations_smoothed
    40 total_vaccinations_per_hundred
    41 people_vaccinated_per_hundred
    42 people_fully_vaccinated_per_hundred
    43 total_boosters_per_hundred
    44 new_vaccinations_smoothed_per_million
    45 stringency_index
    46 population
    47 population_density
    48 median_age
    49 aged_65_older
    50 aged_70_older
    51 gdp_per_capita
    52 extreme_poverty
    53 cardiovasc_death_rate
    54 diabetes_prevalence
    55 female_smokers
    56 male_smokers
    57 handwashing_facilities
    58 hospital_beds_per_thousand
    59 life_expectancy
    60 human_development_index
    61 excess_mortality



```python
# Sorting in alphabetical order by continent.

data.sort_values('continent')
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
      <th>continent</th>
      <th>location</th>
      <th>total_cases</th>
      <th>total_deaths</th>
      <th>people_fully_vaccinated</th>
      <th>positive_rate</th>
      <th>stringency_index</th>
      <th>population</th>
      <th>life_expectancy</th>
      <th>human_development_index</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>54890</th>
      <td>Asia</td>
      <td>Japan</td>
      <td>1473847.0</td>
      <td>16016.0</td>
      <td>57369554.0</td>
      <td>0.159</td>
      <td>52.31</td>
      <td>1.260508e+08</td>
      <td>84.63</td>
      <td>0.919</td>
    </tr>
    <tr>
      <th>109230</th>
      <td>Asia</td>
      <td>Turkey</td>
      <td>6366408.0</td>
      <td>56458.0</td>
      <td>36765581.0</td>
      <td>0.065</td>
      <td>32.41</td>
      <td>8.504274e+07</td>
      <td>77.69</td>
      <td>0.820</td>
    </tr>
    <tr>
      <th>104556</th>
      <td>Asia</td>
      <td>Taiwan</td>
      <td>15991.0</td>
      <td>834.0</td>
      <td>900651.0</td>
      <td>0.000</td>
      <td>NaN</td>
      <td>2.385501e+07</td>
      <td>80.46</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>49417</th>
      <td>Asia</td>
      <td>India</td>
      <td>32768880.0</td>
      <td>438560.0</td>
      <td>146228416.0</td>
      <td>0.023</td>
      <td>70.83</td>
      <td>1.393409e+09</td>
      <td>69.66</td>
      <td>0.645</td>
    </tr>
    <tr>
      <th>65524</th>
      <td>Asia</td>
      <td>Malaysia</td>
      <td>1725357.0</td>
      <td>16382.0</td>
      <td>14989026.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>3.277620e+07</td>
      <td>76.16</td>
      <td>0.810</td>
    </tr>
    <tr>
      <th>99373</th>
      <td>Asia</td>
      <td>South Korea</td>
      <td>251421.0</td>
      <td>2285.0</td>
      <td>15246121.0</td>
      <td>0.044</td>
      <td>50.93</td>
      <td>5.130518e+07</td>
      <td>83.03</td>
      <td>0.916</td>
    </tr>
    <tr>
      <th>38796</th>
      <td>Europe</td>
      <td>France</td>
      <td>6834998.0</td>
      <td>114778.0</td>
      <td>40040630.0</td>
      <td>0.026</td>
      <td>66.67</td>
      <td>6.756425e+07</td>
      <td>82.66</td>
      <td>0.901</td>
    </tr>
    <tr>
      <th>41309</th>
      <td>Europe</td>
      <td>Germany</td>
      <td>3947035.0</td>
      <td>92208.0</td>
      <td>50342010.0</td>
      <td>NaN</td>
      <td>62.04</td>
      <td>8.390047e+07</td>
      <td>81.33</td>
      <td>0.947</td>
    </tr>
    <tr>
      <th>100505</th>
      <td>Europe</td>
      <td>Spain</td>
      <td>4847298.0</td>
      <td>84146.0</td>
      <td>32996436.0</td>
      <td>0.071</td>
      <td>47.69</td>
      <td>4.674521e+07</td>
      <td>83.56</td>
      <td>0.904</td>
    </tr>
    <tr>
      <th>53723</th>
      <td>Europe</td>
      <td>Italy</td>
      <td>4534499.0</td>
      <td>129146.0</td>
      <td>36539599.0</td>
      <td>0.028</td>
      <td>65.28</td>
      <td>6.036747e+07</td>
      <td>83.51</td>
      <td>0.892</td>
    </tr>
    <tr>
      <th>111935</th>
      <td>Europe</td>
      <td>United Kingdom</td>
      <td>6789189.0</td>
      <td>132808.0</td>
      <td>42790585.0</td>
      <td>0.042</td>
      <td>43.98</td>
      <td>6.820711e+07</td>
      <td>81.32</td>
      <td>0.932</td>
    </tr>
    <tr>
      <th>75561</th>
      <td>Europe</td>
      <td>Netherlands</td>
      <td>1973984.0</td>
      <td>18348.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>41.67</td>
      <td>1.717309e+07</td>
      <td>82.28</td>
      <td>0.944</td>
    </tr>
    <tr>
      <th>19730</th>
      <td>North America</td>
      <td>Canada</td>
      <td>1504157.0</td>
      <td>26972.0</td>
      <td>25361100.0</td>
      <td>0.042</td>
      <td>69.91</td>
      <td>3.806791e+07</td>
      <td>82.43</td>
      <td>0.929</td>
    </tr>
    <tr>
      <th>46511</th>
      <td>North America</td>
      <td>Haiti</td>
      <td>20850.0</td>
      <td>584.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>55.56</td>
      <td>1.154168e+07</td>
      <td>64.00</td>
      <td>0.510</td>
    </tr>
    <tr>
      <th>44061</th>
      <td>North America</td>
      <td>Guatemala</td>
      <td>465799.0</td>
      <td>11886.0</td>
      <td>1197918.0</td>
      <td>0.307</td>
      <td>66.20</td>
      <td>1.824987e+07</td>
      <td>74.30</td>
      <td>0.663</td>
    </tr>
    <tr>
      <th>26817</th>
      <td>North America</td>
      <td>Cuba</td>
      <td>646513.0</td>
      <td>5219.0</td>
      <td>3792398.0</td>
      <td>NaN</td>
      <td>71.76</td>
      <td>1.131750e+07</td>
      <td>78.80</td>
      <td>0.783</td>
    </tr>
    <tr>
      <th>69289</th>
      <td>North America</td>
      <td>Mexico</td>
      <td>3341264.0</td>
      <td>258491.0</td>
      <td>33922392.0</td>
      <td>0.397</td>
      <td>67.13</td>
      <td>1.302622e+08</td>
      <td>75.05</td>
      <td>0.779</td>
    </tr>
    <tr>
      <th>112543</th>
      <td>North America</td>
      <td>United States</td>
      <td>39150680.0</td>
      <td>639737.0</td>
      <td>173832202.0</td>
      <td>0.099</td>
      <td>57.87</td>
      <td>3.329151e+08</td>
      <td>78.86</td>
      <td>0.926</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Filling in NaN values manually with the most recent info. on that datapoint online.

data.at[104556,"stringency_index"] = 56.48 # stringency_index of Taiwan is 56.48 (2021)
data.at[104556, "human_development_index"] = 0.916 # HDI of Taiwan is  (201)
#data.at[65524, "positive_rate"] =  #

data.sort_values('continent')
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
      <th>continent</th>
      <th>location</th>
      <th>total_cases</th>
      <th>total_deaths</th>
      <th>people_fully_vaccinated</th>
      <th>positive_rate</th>
      <th>stringency_index</th>
      <th>population</th>
      <th>life_expectancy</th>
      <th>human_development_index</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>54890</th>
      <td>Asia</td>
      <td>Japan</td>
      <td>1473847.0</td>
      <td>16016.0</td>
      <td>57369554.0</td>
      <td>0.159</td>
      <td>52.31</td>
      <td>1.260508e+08</td>
      <td>84.63</td>
      <td>0.919</td>
    </tr>
    <tr>
      <th>109230</th>
      <td>Asia</td>
      <td>Turkey</td>
      <td>6366408.0</td>
      <td>56458.0</td>
      <td>36765581.0</td>
      <td>0.065</td>
      <td>32.41</td>
      <td>8.504274e+07</td>
      <td>77.69</td>
      <td>0.820</td>
    </tr>
    <tr>
      <th>104556</th>
      <td>Asia</td>
      <td>Taiwan</td>
      <td>15991.0</td>
      <td>834.0</td>
      <td>900651.0</td>
      <td>0.000</td>
      <td>56.48</td>
      <td>2.385501e+07</td>
      <td>80.46</td>
      <td>0.916</td>
    </tr>
    <tr>
      <th>49417</th>
      <td>Asia</td>
      <td>India</td>
      <td>32768880.0</td>
      <td>438560.0</td>
      <td>146228416.0</td>
      <td>0.023</td>
      <td>70.83</td>
      <td>1.393409e+09</td>
      <td>69.66</td>
      <td>0.645</td>
    </tr>
    <tr>
      <th>65524</th>
      <td>Asia</td>
      <td>Malaysia</td>
      <td>1725357.0</td>
      <td>16382.0</td>
      <td>14989026.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>3.277620e+07</td>
      <td>76.16</td>
      <td>0.810</td>
    </tr>
    <tr>
      <th>99373</th>
      <td>Asia</td>
      <td>South Korea</td>
      <td>251421.0</td>
      <td>2285.0</td>
      <td>15246121.0</td>
      <td>0.044</td>
      <td>50.93</td>
      <td>5.130518e+07</td>
      <td>83.03</td>
      <td>0.916</td>
    </tr>
    <tr>
      <th>38796</th>
      <td>Europe</td>
      <td>France</td>
      <td>6834998.0</td>
      <td>114778.0</td>
      <td>40040630.0</td>
      <td>0.026</td>
      <td>66.67</td>
      <td>6.756425e+07</td>
      <td>82.66</td>
      <td>0.901</td>
    </tr>
    <tr>
      <th>41309</th>
      <td>Europe</td>
      <td>Germany</td>
      <td>3947035.0</td>
      <td>92208.0</td>
      <td>50342010.0</td>
      <td>NaN</td>
      <td>62.04</td>
      <td>8.390047e+07</td>
      <td>81.33</td>
      <td>0.947</td>
    </tr>
    <tr>
      <th>100505</th>
      <td>Europe</td>
      <td>Spain</td>
      <td>4847298.0</td>
      <td>84146.0</td>
      <td>32996436.0</td>
      <td>0.071</td>
      <td>47.69</td>
      <td>4.674521e+07</td>
      <td>83.56</td>
      <td>0.904</td>
    </tr>
    <tr>
      <th>53723</th>
      <td>Europe</td>
      <td>Italy</td>
      <td>4534499.0</td>
      <td>129146.0</td>
      <td>36539599.0</td>
      <td>0.028</td>
      <td>65.28</td>
      <td>6.036747e+07</td>
      <td>83.51</td>
      <td>0.892</td>
    </tr>
    <tr>
      <th>111935</th>
      <td>Europe</td>
      <td>United Kingdom</td>
      <td>6789189.0</td>
      <td>132808.0</td>
      <td>42790585.0</td>
      <td>0.042</td>
      <td>43.98</td>
      <td>6.820711e+07</td>
      <td>81.32</td>
      <td>0.932</td>
    </tr>
    <tr>
      <th>75561</th>
      <td>Europe</td>
      <td>Netherlands</td>
      <td>1973984.0</td>
      <td>18348.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>41.67</td>
      <td>1.717309e+07</td>
      <td>82.28</td>
      <td>0.944</td>
    </tr>
    <tr>
      <th>19730</th>
      <td>North America</td>
      <td>Canada</td>
      <td>1504157.0</td>
      <td>26972.0</td>
      <td>25361100.0</td>
      <td>0.042</td>
      <td>69.91</td>
      <td>3.806791e+07</td>
      <td>82.43</td>
      <td>0.929</td>
    </tr>
    <tr>
      <th>46511</th>
      <td>North America</td>
      <td>Haiti</td>
      <td>20850.0</td>
      <td>584.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>55.56</td>
      <td>1.154168e+07</td>
      <td>64.00</td>
      <td>0.510</td>
    </tr>
    <tr>
      <th>44061</th>
      <td>North America</td>
      <td>Guatemala</td>
      <td>465799.0</td>
      <td>11886.0</td>
      <td>1197918.0</td>
      <td>0.307</td>
      <td>66.20</td>
      <td>1.824987e+07</td>
      <td>74.30</td>
      <td>0.663</td>
    </tr>
    <tr>
      <th>26817</th>
      <td>North America</td>
      <td>Cuba</td>
      <td>646513.0</td>
      <td>5219.0</td>
      <td>3792398.0</td>
      <td>NaN</td>
      <td>71.76</td>
      <td>1.131750e+07</td>
      <td>78.80</td>
      <td>0.783</td>
    </tr>
    <tr>
      <th>69289</th>
      <td>North America</td>
      <td>Mexico</td>
      <td>3341264.0</td>
      <td>258491.0</td>
      <td>33922392.0</td>
      <td>0.397</td>
      <td>67.13</td>
      <td>1.302622e+08</td>
      <td>75.05</td>
      <td>0.779</td>
    </tr>
    <tr>
      <th>112543</th>
      <td>North America</td>
      <td>United States</td>
      <td>39150680.0</td>
      <td>639737.0</td>
      <td>173832202.0</td>
      <td>0.099</td>
      <td>57.87</td>
      <td>3.329151e+08</td>
      <td>78.86</td>
      <td>0.926</td>
    </tr>
  </tbody>
</table>
</div>




```python

```
