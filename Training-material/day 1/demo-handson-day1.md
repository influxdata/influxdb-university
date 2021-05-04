# Flux Training - Hands-on

## Authors

```
Marco Balduini - marco.balduini@quantiaconsulting.com
Emanuele Della Valle - emanuele.dellavalle@quantiaconsulting.com
Riccardo Tommasini - riccarco.tommasini@quantiaconsulting.com
```

## Use Case Description - Linear Pizza Oven
We have a linear oven to continuously cook pizza.

The cooking operation has two main steps:

* the cooking of the pizza base, and
* the mozzarella melting area.

There are two sensors:

* S1 measures the temperature and the relative humidity of the pizza base cooking area.
* S2 measures the temperature and the relative humidity of the mozzarella melting area. 

Both sensors send a temperature measurement every minute, but are not synchronised.

## Simple Data Modelling
[doc](https://v2.docs.influxdata.com/v2.0/write-data/)

**Note**: At this time we consider only the temperature measurements from the sensors

#### 1 - Model temperature and humidity data from two sensors

measurement|sensor|temperature|humidity|ts|
|-----------|------|-----------|--------|---|
|iot-oven|S1|290|30|1619006400000000000|
|iot-oven|S2|105|55|1619006415000000000|
|iot-oven|S1|305|38|1619006460000000000|
|iot-oven|S2|120|65|1619006475000000000|

### Solution

```
iot-oven,sensor=S1 temperature=290,humidity=30 1619006400000000000
iot-oven,sensor=S2 temperature=105,humidity=55 1619006415000000000
iot-oven,sensor=S1 temperature=305,humidity=38 1619006460000000000
iot-oven,sensor=S2 temperature=120,humidity=65 1619006475000000000
```

### Complete set of data to be loaded into the training bucket
```
iot-oven,sensor=S1 temperature=290,humidity=30 1619006400000000000
iot-oven,sensor=S2 temperature=105,humidity=55 1619006415000000000
iot-oven,sensor=S2 temperature=110,humidity=60 1619006445000000000
iot-oven,sensor=S1 temperature=305,humidity=38 1619006460000000000
iot-oven,sensor=S2 temperature=120,humidity=65 1619006475000000000
iot-oven,sensor=S2 temperature=115,humidity=60 1619006505000000000
iot-oven,sensor=S1 temperature=280,humidity=45 1619006520000000000
iot-oven,sensor=S2 temperature=110,humidity=67 1619006535000000000
iot-oven,sensor=S2 temperature=115,humidity=72 1619006565000000000
iot-oven,sensor=S1 temperature=280,humidity=22 1619006580000000000
iot-oven,sensor=S2 temperature=95,humidity=65 1619006595000000000
iot-oven,sensor=S2 temperature=90,humidity=60  1619006625000000000
iot-oven,sensor=S1 temperature=285,humidity=32 1619006640000000000
iot-oven,sensor=S2 temperature=100,humidity=55 1619006655000000000
iot-oven,sensor=S2 temperature=105,humidity=60 1619006685000000000
``` 

**Note: Time Range**
> Start Time: 2021-04-21 12:00:00 GMT (2021-04-21T12:00:00Z)
> End Time: 2021-04-21 12:05:00 GMT (2021-04-21T12:05:00Z)

## First Query (DEMO)

```
from(bucket: "training")
  |> range(start: v.timeRangeStart, stop: v.timeRangeStop)
  |> filter(fn: (r) => r._measurement == "iot-oven")
  |> filter(fn: (r) => r._field == "temperature")
  |> filter(fn: (r) => r.sensor == "S2")
  |> filter(fn: (r) => r._value < 100)
```

## 02 - Range and Tables (DEMO)
[doc](https://v2.docs.influxdata.com/v2.0/reference/flux/stdlib/built-in/transformations/range/)
#### Extract all the measurements in a given range
##### Absolute

###### Use a custom time range from the UI: Start: 2021-04-21 12:00:00, stop: 2021-04-21 12:05:00)
```
from(bucket: "training")
  |> range(start: v.timeRangeStart, stop: v.timeRangeStop)
```

###### Specify time range in the query
```
from(bucket: "training")
  |> range(start: 2021-04-21T12:00:00Z, stop: 2021-04-21T12:05:00Z)
```

##### Relative

###### Specify `Past 24h` from the UI
```
from(bucket: "training")
  |> range(start: v.timeRangeStart)
```

###### Specify `-24h` directly in the query
```
from(bucket: "training")
  |> range(start: -24h)
```

> From now on, we will use the UI Time Range `|> range(start: v.timeRangeStart, stop: v.timeRangeStop)`

## 03 - Filter By Tag
#### Extract the temperature data from the cooking base area (sensor S1)
[doc](https://v2.docs.influxdata.com/v2.0/reference/flux/stdlib/built-in/transformations/filter/)

```
from(bucket: "training")
  |> range(start: v.timeRangeStart, stop: v.timeRangeStop)
  |> filter(fn: (r) => r._measurement == "iot-oven")
  |> filter(fn: (r) => r._field == "temperature")
  |> filter(fn: (r) => r.sensor == "S1")
```
 
## 04 - Filter By Value
### Extract the measurements from the cooking base area (sensor S1) with a temperature under 300°  
[doc](https://v2.docs.influxdata.com/v2.0/reference/flux/stdlib/built-in/transformations/filter/)

```
from(bucket: "training")
  |> range(start: v.timeRangeStart, stop: v.timeRangeStop)
  |> filter(fn: (r) => r._measurement == "iot-oven")
  |> filter(fn: (r) => r._field == "temperature")
  |> filter(fn: (r) => r.sensor == "S1")
  |> filter(fn: (r) => r._value < 300)
```

## 05 - Functions 

### Grouping + Aggregator (mean) - Extract the average temperature and the average humidity along the different stages of the linear pizza oven

[doc](https://v2.docs.influxdata.com/v2.0/reference/flux/stdlib/built-in/transformations/aggregates/)

```
from(bucket: "training")
  |> range(start: v.timeRangeStart, stop: v.timeRangeStop)
  |> filter(fn: (r) => r._measurement == "iot-oven")
  |> group(columns: ["_field"])
  |> mean()
```

### Selector (last) - Extract the last humidity observation and the last temperature observation from the cooking base area

[doc](https://v2.docs.influxdata.com/v2.0/reference/flux/stdlib/built-in/transformations/selectors/)

```
from(bucket: "training")
  |> range(start: v.timeRangeStart, stop: v.timeRangeStop)
  |> filter(fn: (r) => r._measurement == "iot-oven")
  |> filter(fn: (r) => r.sensor == "S1")
  |> group(columns: ["_field"])
  |> last()
```

LIVE: show tail(n: 2) and discuss that selector might return more than one raw per table.
LIVE: show that |> group( columns: []) creates one single table (mention in the slide?)

## 06 - aggregateWindow
### Extract the moving average temperature observed in the cooking base area over a window of 2 minutes (DEMO)

[doc](https://v2.docs.influxdata.com/v2.0/reference/flux/stdlib/built-in/transformations/aggregates/aggregatewindow/)

```
from(bucket: "training")
  |> range(start: v.timeRangeStart, stop: v.timeRangeStop)
  |> filter(fn: (r) => r._measurement == "iot-oven")
  |> filter(fn: (r) => r._field == "temperature")
  |> filter(fn: (r) => r.sensor == "S1")
  |> aggregateWindow(every: 2m, fn: mean)
```

**NOTE** The flag `createEmpty: false` can be used to consider only the windows that contains data (its default value is `true`)

```
from(bucket: "training")
  |> range(start: v.timeRangeStart, stop: v.timeRangeStop)
  |> filter(fn: (r) => r._measurement == "iot-oven")
  |> filter(fn: (r) => r._field == "temperature")
  |> filter(fn: (r) => r.sensor == "S2")
  |> aggregateWindow(every: 3m, fn: mean, createEmpty: false)
```

### Extract the moving average temperature observed by S2 over a window of 3 minutes (hands-on)

```
from(bucket: "training")
  |> range(start: v.timeRangeStart, stop: v.timeRangeStop)
  |> filter(fn: (r) => r._measurement == "iot-oven")
  |> filter(fn: (r) => r._field == "temperature")
  |> filter(fn: (r) => r.sensor == "S2")
  |> aggregateWindow(every: 3m, fn: mean, createEmpty: false)
```

## 07 - Map and Custom Functions
### Correct the temperature observations of the cooking base area (S1) by subtracting a delta of 5°C to each value
[doc](https://v2.docs.influxdata.com/v2.0/query-data/guides/custom-functions/)

#### Inline map

```
from(bucket: "training")
  |> range(start: v.timeRangeStart, stop: v.timeRangeStop)
  |> filter(fn: (r) => r._measurement == "iot-oven")
  |> filter(fn: (r) => r._field == "temperature")
  |> filter(fn: (r) => r.sensor == "S1")
  |> map(fn: (r) => ({
      r with
      correctValue: r._value - 5.0
    }))
```
**Note** the `r with` clause maintains alla the original columns and adds the new one.

#### Create a custom function to be used in the inline map
```
adjValue = (x, y) => x + y
    
from(bucket: "training")
  |> range(start: v.timeRangeStart, stop: v.timeRangeStop)
  |> filter(fn: (r) => r._measurement == "iot-oven")
  |> filter(fn: (r) => r._field == "temperature")
  |> filter(fn: (r) => r.sensor == "S1")
  |> map(fn: (r) => ({
      r with
      correctValue: adjValue(x:r._value, y:-5.0)
  }))
```

#### Create a costume pipe forwardable function that contains a map

```
adjValues = (tables=<-, x) =>
  tables
    |> map(fn: (r) => ({ r with correctValue: r._value + x}))

from(bucket: "training")
  |> range(start: v.timeRangeStart, stop: v.timeRangeStop)
  |> filter(fn: (r) => r._measurement == "iot-oven")
  |> filter(fn: (r) => r._field == "temperature")
  |> filter(fn: (r) => r.sensor == "S1")
  |> adjValues(x:-5.0)
```

**Note** Most Flux functions manipulate data piped-forward into the function. In order for a custom function to process piped-forward data, one of the function parameters must capture the input tables using the `<-` pipe-receive expression.
