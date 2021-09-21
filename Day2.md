```python
# https://youtu.be/i3-wsgtGhfs
```


```python
# Run once for bokeh data 
from bokeh import sampledata
sampledata.download()
```

    Creating /Users/jason/.bokeh directory
    Creating /Users/jason/.bokeh/data directory
    Using data directory: /Users/jason/.bokeh/data
    Downloading: CGM.csv (1589982 bytes)
       1589982 [100.00%]
    Downloading: US_Counties.zip (3171836 bytes)
       3171836 [100.00%]
    Unpacking: US_Counties.csv
    Downloading: us_cities.json (713565 bytes)
        713565 [100.00%]
    Downloading: unemployment09.csv (253301 bytes)
        253301 [100.00%]
    Downloading: AAPL.csv (166698 bytes)
        166698 [100.00%]
    Downloading: FB.csv (9706 bytes)
          9706 [100.00%]
    Downloading: GOOG.csv (113894 bytes)
        113894 [100.00%]
    Downloading: IBM.csv (165625 bytes)
        165625 [100.00%]
    Downloading: MSFT.csv (161614 bytes)
        161614 [100.00%]
    Downloading: WPP2012_SA_DB03_POPULATION_QUINQUENNIAL.zip (4816256 bytes)
       4816256 [100.00%]
    Unpacking: WPP2012_SA_DB03_POPULATION_QUINQUENNIAL.csv
    Downloading: gapminder_fertility.csv (64346 bytes)
         64346 [100.00%]
    Downloading: gapminder_population.csv (94509 bytes)
         94509 [100.00%]
    Downloading: gapminder_life_expectancy.csv (73243 bytes)
         73243 [100.00%]
    Downloading: gapminder_regions.csv (7781 bytes)
          7781 [100.00%]
    Downloading: world_cities.zip (645274 bytes)
        645274 [100.00%]
    Unpacking: world_cities.csv
    Downloading: airports.json (6373 bytes)
          6373 [100.00%]
    Downloading: movies.db.zip (5053420 bytes)
       5053420 [100.00%]
    Unpacking: movies.db
    Downloading: airports.csv (203190 bytes)
        203190 [100.00%]
    Downloading: routes.csv (377280 bytes)
        377280 [100.00%]
    Downloading: haarcascade_frontalface_default.xml (930127 bytes)
        930127 [100.00%]



```python
import numpy as np
from bokeh.plotting import figure, show
from bokeh.io import output_notebook, output_file

from bokeh.models import HoverTool
from bokeh.models import LogColorMapper
from bokeh.palettes import Viridis6 as palette
from bokeh.sampledata.us_counties import data as counties
from bokeh.sampledata.unemployment import data as unemployment

```


```python
output_notebook()
```



<div class="bk-root">
    <a href="https://bokeh.org" target="_blank" class="bk-logo bk-logo-small bk-logo-notebook"></a>
    <span id="1002">Loading BokehJS ...</span>
</div>





```python

```


```python
x = np.linspace(-10, 10, 500)
```


```python
y = np.sin(x)
```


```python
p = figure(title='y=sin(x)')
p.line(x, y)
p.xaxis.axis_label = 'x'
p.yaxis.axis_label = 'y'
show(p)
```








<div class="bk-root" id="fe38ecf7-4d5e-47df-a0ea-9f959ad35571" data-root-id="1003"></div>






```python

```


```python
# https://docs.bokeh.org/en/latest/docs/gallery.html
```


```python
n = 500
x = 2 + 2*np.random.standard_normal(n)
y = 2 + 2*np.random.standard_normal(n)

p = figure(title="Hexbin for 500 points", match_aspect=True,
           tools="wheel_zoom,reset", background_fill_color='#440154')
p.grid.visible = False

r, bins = p.hexbin(x, y, size=0.5, hover_color="pink", hover_alpha=0.8)

p.circle(x, y, color="white", size=1)

p.add_tools(HoverTool(
    tooltips=[("count", "@c"), ("(q,r)", "(@q, @r)")],
    mode="mouse", point_policy="follow_mouse", renderers=[r]
))

# output_file("hexbin.html")

show(p)
```








<div class="bk-root" id="50e897ad-8a65-4228-b8e6-16861630b88a" data-root-id="1192"></div>






```python

```


```python

palette.reverse()

counties = {
    code: county for code, county in counties.items() if county["state"] == "tx"
}

county_xs = [county["lons"] for county in counties.values()]
county_ys = [county["lats"] for county in counties.values()]

county_names = [county['name'] for county in counties.values()]
county_rates = [unemployment[county_id] for county_id in counties]
color_mapper = LogColorMapper(palette=palette)

data=dict(
    x=county_xs,
    y=county_ys,
    name=county_names,
    rate=county_rates,
)

TOOLS = "pan,wheel_zoom,reset,hover,save"

p = figure(
    title="Texas Unemployment, 2009", tools=TOOLS,
    x_axis_location=None, y_axis_location=None,
    tooltips=[
        ("Name", "@name"), ("Unemployment rate)", "@rate%"), ("(Long, Lat)", "($x, $y)")
    ])
p.grid.grid_line_color = None
p.hover.point_policy = "follow_mouse"

p.patches('x', 'y', source=data,
          fill_color={'field': 'rate', 'transform': color_mapper},
          fill_alpha=0.7, line_color="white", line_width=0.5)

show(p)
```


    ---------------------------------------------------------------------------

    AttributeError                            Traceback (most recent call last)

    <ipython-input-12-8ce2f71fe241> in <module>
    ----> 1 palette.reverse()
          2 
          3 counties = {
          4     code: county for code, county in counties.items() if county["state"] == "tx"
          5 }


    AttributeError: 'tuple' object has no attribute 'reverse'



```python

```


```python

```


```python

```


```python
# TODO: Use surface3d for 3d line plotting?
```


```python
fig = plt.figure()
ax3d = fig.gca(projection='3d')
t = np.linspace(0, 20, 500)
x = np.sin(t)
y = np.cos(t)
ax3d.plot(x, y, t)
ax3d.w_xaxis.set_ticks([-1, 0, 1])
ax3d.set_xlabel('x')
ax3d.w_yaxis.set_ticks([-1, 0, 1])
ax3d.set_ylabel('y')
ax3d.set_zlabel('time (s)');

```


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-13-9df56f56499c> in <module>
    ----> 1 fig = plt.figure()
          2 ax3d = fig.gca(projection='3d')
          3 t = np.linspace(0, 20, 500)
          4 x = np.sin(t)
          5 y = np.cos(t)


    NameError: name 'plt' is not defined



```python

```
