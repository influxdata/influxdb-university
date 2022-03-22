# Flux 101 Training - Bootcamp

## Authors

```
Marco Balduini - marco.balduini@quantiaconsulting.com
Emanuele Della Valle - emanuele.dellavalle@quantiaconsulting.com
Riccardo Tommasini - riccarco.tommasini@quantiaconsulting.com
```

## BC1 -  City Water Tank dashboard queries (part 1)

Needed input files:

* fill-level-lp.txt
* flow-rate-lp.txt
* pump-speed-lp.txt

### The fill level of the city water tank

```
from(bucket: "training")
  |> range(start: v.timeRangeStart, stop: v.timeRangeStop)
  |> filter(fn: (r) => r._measurement == "fill_level")
  |> filter(fn: (r) => r._field == "value")
  |> filter(fn: (r) => r.tank == "city_water")
```

### The speed of the pump that refills the city water tank

```
from(bucket: "training")
  |> range(start: v.timeRangeStart, stop: v.timeRangeStop)
  |> filter(fn: (r) => r._measurement == "pump_speed")
  |> filter(fn: (r) => r._field == "value")
```

### The fill level of each tank down sampled to 1 min

```
from(bucket: "training")
  |> range(start: v.timeRangeStart, stop: v.timeRangeStop)
  |> filter(fn: (r) => r._measurement == "fill_level")
  |> filter(fn: (r) => r._field == "value")
  |> filter(fn: (r) => r.tank == "A1")
  |> aggregateWindow(every: 1m, fn: mean, createEmpty: false)
```
```
from(bucket: "training")
  |> range(start: v.timeRangeStart, stop: v.timeRangeStop)
  |> filter(fn: (r) => r._measurement == "fill_level")
  |> filter(fn: (r) => r._field == "value")
  |> filter(fn: (r) => r.tank == "A2")  
  |> aggregateWindow(every: 1m, fn: mean, createEmpty: false)
```
```
from(bucket: "training")
  |> range(start: v.timeRangeStart, stop: v.timeRangeStop)
  |> filter(fn: (r) => r._measurement == "fill_level")
  |> filter(fn: (r) => r._field == "value")
  |> filter(fn: (r) => r.tank == "B1")
  |> aggregateWindow(every: 1m, fn: mean, createEmpty: false)
```
```
from(bucket: "training")
  |> range(start: v.timeRangeStart, stop: v.timeRangeStop)
  |> filter(fn: (r) => r._measurement == "fill_level")
  |> filter(fn: (r) => r._field == "value")
  |> filter(fn: (r) => r.tank == "B2")
  |> aggregateWindow(every: 1m, fn: mean, createEmpty: false)
```

### The flow rate of each valve

```
from(bucket: "training")
  |> range(start: v.timeRangeStart, stop: v.timeRangeStop)
  |> filter(fn: (r) => r._measurement == "flow_rate")
  |> filter(fn: (r) => r._field == "value")
  |> filter(fn: (r) => r.valve == "V1")
  |> last()
```
```
from(bucket: "training")
  |> range(start: v.timeRangeStart, stop: v.timeRangeStop)
  |> filter(fn: (r) => r._measurement == "flow_rate")
  |> filter(fn: (r) => r._field == "value")
  |> filter(fn: (r) => r.valve == "V2")
  |> last()
```
```
from(bucket: "training")
  |> range(start: v.timeRangeStart, stop: v.timeRangeStop)
  |> filter(fn: (r) => r._measurement == "flow_rate")
  |> filter(fn: (r) => r._field == "value")
  |> filter(fn: (r) => r.valve == "V3")
  |> last()
```
```
from(bucket: "training")
  |> range(start: v.timeRangeStart, stop: v.timeRangeStop)
  |> filter(fn: (r) => r._measurement == "flow_rate")
  |> filter(fn: (r) => r._field == "value")
  |> filter(fn: (r) => r.valve == "V4")
  |> last()
```