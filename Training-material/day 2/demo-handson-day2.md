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

## 08 - Join 
[doc](https://v2.docs.influxdata.com/v2.0/query-data/guides/join/)

### Extract the difference between the temperature of the base cooking area and the mozzarella melting area

#### Join assuming synchronous time-series

```
ts = from(bucket: "training")
  |> range(start: v.timeRangeStart, stop: v.timeRangeStop)
  |> filter(fn: (r) => r._measurement == "iot-oven")
  |> filter(fn: (r) => r._field == "temperature")
  
ts1 = ts |> filter(fn: (r) => r.sensor == "S1")
ts2 = ts |> filter(fn: (r) => r.sensor == "S2")

join(tables: {key1: ts1, key2: ts2}, on: ["_time"], method: "inner")

```
**Note** No results!!!

#### Join assuming a fixed delta (timeShift)
**Note** Use `timeShift()` function.
[doc](https://v2.docs.influxdata.com/v2.0/reference/flux/stdlib/built-in/transformations/timeshift/)

```
temp = from(bucket: "training")
  |> range(start: v.timeRangeStart, stop: v.timeRangeStop)
  |> filter(fn: (r) => r._measurement == "iot-oven")
  |> filter(fn: (r) => r._field == "temperature")

tempS1 = temp |> filter(fn: (r) => r.sensor == "S1")
tempS2 = temp |> filter(fn: (r) => r.sensor == "S2")
              |> timeShift(duration: 15s, columns: ["_time"] )

temp_join = join(tables: {s1: tempS1, s2: tempS2}, on: ["_time"], method: "inner")

temp_join 
  |> map(fn: (r) => ({ r with _value: r._value_s1 - r._value_s2 }))  
  |> drop(columns: ["_measurement_s1", "_measurement_s2", "_start_s1", "_start_s2", "_stop_s1", "_stop_s2", "sensor_s1", "sensor_s2", "_field_s1", "_field_s2"])
```

**Note** 
> You are missing values!!!

#### Join on time exploiting windows
**Note** Use `aggregateWindow()` function.
[doc](https://v2.docs.influxdata.com/v2.0/reference/flux/stdlib/built-in/transformations/aggregates/aggregatewindow/)

```
temp = from(bucket: "training")
  |> range(start: v.timeRangeStart, stop: v.timeRangeStop)
  |> filter(fn: (r) => r._measurement == "iot-oven")
  |> filter(fn: (r) => r._field == "temperature")

tempS1 = temp 
          |> filter(fn: (r) => r.sensor == "S1")
          |> aggregateWindow(every: 60s, fn: mean)
        
tempS2 = temp 
          |> filter(fn: (r) => r.sensor == "S2")
          |> aggregateWindow(every: 60s, fn: mean)

temp_join = join(tables: {s1: tempS1, s2: tempS2}, on: ["_time"], method: "inner")

temp_join 
  |> map(fn: (r) => ({ r with _value: r._value_s1 - r._value_s2 }))  
  |> drop(columns: ["_measurement_s1", "_measurement_s2", "_start_s1", "_start_s2", "_stop_s1", "_stop_s2", "sensor_s1", "sensor_s2", "_field_s1", "_field_s2"])

```

OR

```
temp = from(bucket: "training")
  |> range(start: v.timeRangeStart, stop: v.timeRangeStop)
  |> filter(fn: (r) => r._measurement == "iot-oven")
  |> filter(fn: (r) => r._field == "temperature")
  |> aggregateWindow(every: 60s, fn: mean)
  
tempS1 = temp |> filter(fn: (r) => r.sensor == "S1")  
tempS2 = temp |> filter(fn: (r) => r.sensor == "S2")

temp_join = join(tables: {s1: tempS1, s2: tempS2}, on: ["_time"], method: "inner")

temp_join 
  |> map(fn: (r) => ({ r with _value: r._value_s1 - r._value_s2 }))  
  |> drop(columns: ["_measurement_s1", "_measurement_s2", "_start_s1", "_start_s2", "_stop_s1", "_stop_s2", "sensor_s1", "sensor_s2", "_field_s1", "_field_s2"])
```

### Extract the difference between the humidity levels of the base cooking area and the mozzarella melting area. Find if the differences are lower than 20% or greater than 30%

#### Join assuming a fixed delta (timeShift)
**Note** Use `timeShift()` function.
[doc](https://v2.docs.influxdata.com/v2.0/reference/flux/stdlib/built-in/transformations/timeshift/)

```
import "math"

hs = from(bucket: "training")
  |> range(start: v.timeRangeStart, stop: v.timeRangeStop)
  |> filter(fn: (r) => r._measurement == "iot-oven")
  |> filter(fn: (r) => r._field == "humidity")

hs1 = hs |> filter(fn: (r) => r.sensor == "S1")
hs2 = hs |> filter(fn: (r) => r.sensor == "S2")
              |> timeShift(duration: 15s, columns: ["_time"] )

h_join = join(tables: {s1: hs1, s2: hs2}, on: ["_time"], method: "inner")

h_join 
  |> map(fn: (r) => ({ r with _value: math.abs(x:(r._value_s1 - r._value_s2))}))  
  |> filter(fn: (r) => r._value < 20 or r._value > 30)
  |> drop(columns: ["_measurement_s1", "_measurement_s2", "_start_s1", "_start_s2", "_stop_s1", "_stop_s2", "sensor_s1", "sensor_s2", "_field_s1", "_field_s2"])
```
**Note** 
> You are missing values!!!

#### Join on time exploiting windows
**Note** Use `aggregateWindow()` function.
[doc](https://v2.docs.influxdata.com/v2.0/reference/flux/stdlib/built-in/transformations/aggregates/aggregatewindow/)

```
import "math"

hs = from(bucket: "training")
  |> range(start: v.timeRangeStart, stop: v.timeRangeStop)
  |> filter(fn: (r) => r._measurement == "iot-oven")
  |> filter(fn: (r) => r._field == "humidity")
  |> aggregateWindow(every: 60s, fn: mean)

hs1 = hs |> filter(fn: (r) => r.sensor == "S1")
hs2 = hs |> filter(fn: (r) => r.sensor == "S2")

h_join = join(tables: {s1: hs1, s2: hs2}, on: ["_time"], method: "inner")

h_join 
  |> map(fn: (r) => ({ r with _value: math.abs(x:(r._value_s1 - r._value_s2))}))  
  |> filter(fn: (r) => r._value < 20 or r._value > 30)
  |> drop(columns: ["_measurement_s1", "_measurement_s2", "_start_s1", "_start_s2", "_stop_s1", "_stop_s2", "sensor_s1", "sensor_s2", "_field_s1", "_field_s2"])
```

## Alerts and Task

### Task example

```
from(bucket: "training")
  |> range(start: v.timeRangeStart, stop: v.timeRangeStop)
  |> filter(fn: (r) => r["_measurement"] == "iot-oven")
  |> filter(fn: (r) => r["_field"] == "temperature")
  |> filter(fn: (r) => r["sensor"] == "S1")
  |> aggregateWindow(every: 30s, fn: mean) //downsample deck 03 slide 60
```
```
from(bucket: "training")
|> range(start: -30s)
|> filter(fn: (r) => (r._measurement == "iot-oven"))
|> filter(fn: (r) => (r._field == "temperature"))
|> filter(fn: (r) => (r.sensor == "S1"))
|> mean()
```
```
from(bucket: "training")
|> range(start: -30s)
|> filter(fn: (r) => (r._measurement == "iot-oven"))
|> filter(fn: (r) => (r._field == "temperature"))
|> mean()
|> map(fn: (r) => ({r with _time: r._stop}))
|> map(fn: (r) => ({r with _field: "AvgTemperatureEvery30s"}))
|> to(bucket: "training", org: "…@quantiaconsulting.com")
```

## Advanced Flux

### Time series enrichment

```
import "sql"

pizzas = sql.from(
  driverName: "postgres",
  dataSourceName: "postgresql://qcro:qc-readonly@qc-pg.c30roki0vo0h.eu-west-1.rds.amazonaws.com:5432/pizza-erp?sslmode=disable",
  query:"SELECT * 
         FROM oven 
         WHERE enteringtime/1000000000 >= extract(epoch from timestamp '2021-04-21T12:00:00') and
              enteringtime/1000000000 < extract(epoch from timestamp '2021-04-21T12:50:00')
        "
) 

obs = from(bucket: "training")
  |> range(start: v.timeRangeStart, stop: v.timeRangeStop)
  |> filter(fn: (r) => r._measurement == "iot-oven")
  |> filter(fn: (r) => r._field == "temperature")
  |> drop(columns: ["_measurement", "_start", "_stop"])

join(tables: {p: pizzas, o: obs}, on: ["sensor" ], method: "inner")
  |> filter(fn: (r) => uint(v: r._time) >= r.enteringtime and uint(v: r._time) < r.exitingtime)
  |> group(columns: ["pid", "kind"], mode:"by")
```
### Holt-Winters

#### Show real data
```
from(bucket: "training")
  |> range(start: v.timeRangeStart, stop: v.timeRangeStop)
  |> filter(fn: (r) => r._measurement == "fill_level")
  |> filter(fn: (r) => r._field == "value")
  |> filter(fn: (r) => r.tank == "B2")
```

#### Downsample the data
```
from(bucket: "training")
  |> range(start: v.timeRangeStart, stop: v.timeRangeStop)
  |> filter(fn: (r) => r._measurement == "fill_level")
  |> filter(fn: (r) => r._field == "value")
  |> filter(fn: (r) => r.tank == "B2")
  |> aggregateWindow(every: 1m, fn: first)  
```

#### Apply hot-winters on downsampled data
```
from(bucket: "training")
  |> range(start: v.timeRangeStart, stop: v.timeRangeStop)
  |> filter(fn: (r) => r._measurement == "fill_level")
  |> filter(fn: (r) => r._field == "value")
  |> filter(fn: (r) => r.tank == "B2")
  |> aggregateWindow(every: 1m, fn: first)  
  |> holtWinters(n: 10, seasonality: 8, interval: 1m, withFit: true)
```

**NOTE** use `withFit: false` to hide the fitted data

### z-score computation task
```
import "date"
import "math"

option v = {bucket: "", timeRangeStart: -15m, timeRangeStop: now()}
option task = {name: "Zscore of sensor observations", every: 5m}

movingAvg = from(bucket: "training")
	|> range(start: v.timeRangeStart, stop: v.timeRangeStop)
	|> aggregateWindow(every: 5m, fn: mean, createEmpty: false)
	|> filter(fn: (r) =>
		(r._stop != r._time))
	|> drop(columns: ["_start", "_stop", "host"])

movingStddev = from(bucket: "training")
	|> range(start: v.timeRangeStart, stop: v.timeRangeStop)
	|> aggregateWindow(every: 5m, fn: stddev, createEmpty: false)
	|> filter(fn: (r) =>
		(r._stop != r._time))
	|> drop(columns: ["_start", "_stop", "host"])

join1 = join(tables: {avg: movingAvg, stddev: movingStddev}, on: ["_field", "_measurement", "sensor"], method: "inner")
	|> filter(fn: (r) =>
		(r._time_avg == r._time_stddev))
	|> rename(columns: {_time_avg: "_time"})
	|> drop(columns: ["_time_stddev"])

allData = from(bucket: "training")
	|> range(start: v.timeRangeStart, stop: v.timeRangeStop)
	|> drop(columns: ["_start", "_stop", "host"])

join2 = join(tables: {all: allData, j: join1}, on: ["_field", "_measurement", "sensor"])
	|> filter(fn: (r) =>
		(uint(v: r._time_all) - uint(v: r._time_j) > 0))
	|> filter(fn: (r) =>
		(uint(v: r._time_all) - uint(v: r._time_j) <= 5 * 60 * 1000000000))
	|> rename(columns: {_time_all: "_time"})
	|> map(fn: (r) =>
		({r with _value: math.abs(x: (r._value - r._value_avg) / r._value_stddev)}))

join2
	|> to(bucket: "task-output", org: "emanuele.dellavalle@quantiaconsulting.com")
```
