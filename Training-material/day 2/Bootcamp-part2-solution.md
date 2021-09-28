# Flux Training - Virtual - SF 2020 - Bootcamp

## Authors

```
Marco Balduini - marco.balduini@quantiaconsulting.com
Emanuele Della Valle - emanuele.dellavalle@quantiaconsulting.com
Riccardo Tommasini - riccarco.tommasini@quantiaconsulting.com
```
## BC2 -  City Water Tank dashboard queries (part 2)

Needed input files:

* valve-state-lp.txt

### Level difference every minute
```
actualMeanLevel = from(bucket: "training")
  |> range(start: v.timeRangeStart, stop: v.timeRangeStop)
  |> filter(fn: (r) => r._measurement == "fill_level")
  |> filter(fn: (r) => r._field == "value")
  |> filter(fn: (r) => r.tank == "city_water")
  |> aggregateWindow(every: 1m, fn: mean, createEmpty: false)
  
  
preMeanLevel = actualMeanLevel
  |> timeShift(duration: -1m)

join(
  tables: {pre:preMeanLevel, actual:actualMeanLevel},
  on: ["_time"]
) |> map(fn: (r) => ({
    _time: r._time,
    _value:  r._value_pre - r._value_actual
    }))
```

### Open valve(s)
```
from(bucket: "training")
  |> range(start: v.timeRangeStart, stop: v.timeRangeStop)
  |> filter(fn: (r) => r._measurement == "valve_state")
  |> filter(fn: (r) => r._field == "value")
  |> last()
  |> map(fn: (r) => ({
      r with
      _value:
      if r._value == true then 1
      else 0
    }))  
  |> group()  
  |> sum(column: "_value")  
```

### Fill Level of Tanks
```
from(bucket: "training")
  |> range(start: v.timeRangeStart, stop: v.timeRangeStop)
  |> filter(fn: (r) => r._measurement == "fill_level")
  |> filter(fn: (r) => r._field == "value")
  |> filter(fn: (r) => r.tank != "city_water") 
  |> aggregateWindow(every: 1m, fn: mean, createEmpty: false)
  |> pivot(rowKey: ["_time"], columnKey: ["tank"], valueColumn: "_value")
  |> map(fn: (r) => ({ r with _value : r.A1 + r.A2 + r.B1 + r.B2 }))
```

### Total Flow Rate
```
from(bucket: "training")
  |> range(start: v.timeRangeStart, stop: v.timeRangeStop)
  |> filter(fn: (r) => r._measurement == "flow_rate")
  |> filter(fn: (r) => r._field == "value")
  |> last()  
  |> group()
  |> sum(column: "_value")
```

### Current Status of Valve V1
```
from(bucket: "training")
  |> range(start: v.timeRangeStart, stop: v.timeRangeStop)
  |> filter(fn: (r) => r._measurement == "valve_state")
  |> filter(fn: (r) => r._field == "value")
  |> filter(fn: (r) => r.valve == "V1")
  |> last()
  |> map(fn: (r) => ({
      r with
      _value:
      if r._value == true then 1
      else 0
    }))
```

### Current Status of Valve V2
```
from(bucket: "training")
  |> range(start: v.timeRangeStart, stop: v.timeRangeStop)
  |> filter(fn: (r) => r._measurement == "valve_state")
  |> filter(fn: (r) => r._field == "value")
  |> filter(fn: (r) => r.valve == "V2")
  |> last()
  |> map(fn: (r) => ({
      r with
      _value:
      if r._value == true then 1
      else 0
    }))
```

### Current Status of Valve V3
```
from(bucket: "training")
  |> range(start: v.timeRangeStart, stop: v.timeRangeStop)
  |> filter(fn: (r) => r._measurement == "valve_state")
  |> filter(fn: (r) => r._field == "value")
  |> filter(fn: (r) => r.valve == "V3")
  |> last()
  |> map(fn: (r) => ({
      r with
      _value:
      if r._value == true then 1
      else 0
    }))
```

### Current Status of Valve V4
```
from(bucket: "training")
  |> range(start: v.timeRangeStart, stop: v.timeRangeStop)
  |> filter(fn: (r) => r._measurement == "valve_state")
  |> filter(fn: (r) => r._field == "value")
  |> filter(fn: (r) => r.valve == "V1")
  |> last()
  |> map(fn: (r) => ({
      r with
      _value:
      if r._value == true then 1
      else 0
    }))
```