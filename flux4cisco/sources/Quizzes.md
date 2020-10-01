## Quiz 1

What is the relation between a time series to a measurement? `(1:1, 1:N, N:1, or N:N)` **1:1**

What is the relation between a time series to a tag? `(1:1, 1:N, N:1, or N:N)`**1:N**

What is the relation between a time series to a field name? `(1:1, 1:N, N:1, or N:N)` **1:N**

What is the relation between a field name to a field value? `(1:1, 1:N, N:1, or N:N)` **N:N**

What is the relation between a time series to a timestamp? `(1:1, 1:N, N:1, or N:N)` **1:N**

What is the relation between a <measurement,tag,field name,timestamp> to a value? `(1:1, 1:N, N:1, or N:N)` **1:1**

## Quiz 2

### Questions
```
1. What’s a Bucket?
2. What’s the Pipe-forward operator |>  for?
3. What’s a Table in Flux?
4. What’s a Group Key in Flux?
```

### Answers

```
A. List of columns for which every row in a table has the same value 
B. A named data source with retention policy 
C. Chains operations
D. A part of a result
```

**[1:B, 2:C, 3:D, 4:A]**

## Quiz 3

You can omit the range clause – `(True of False)` **F**

Filtering can change the number of tables in the result – `(True of False)` **T** (empty tables)

Shaping always changes the number of tables in the result – `(True of False)` **F**

Processing can change the number of tables in the result –  `(True of False)` **F**

AggregateWindow function is just a process step – `(True of False)` **F**

AggregateWindow function eases the downsampling task – `(True of False)` **T**

The parameter createEmpty of the aggregateWindow function can change the number of tables in the result – `(True of False)` **T** 


## Quiz 4

In a functional programming language, map() applies a function to each element of a collection – `(True of False)` **T**

In Flux, map() always adds a column to each table – `(True of False)` **F**

map() using the with clause can add a column to each table – `(True of False)` **T**

You can pass a custom functions only to a map() – `(True of False)` **F**

In a pipe-forwardable custom function with a parameter `(t=<-), t` represents input tables that the function applies to – `(True of False)` **T**

## Quiz 5

Which synchronization method shall you use before joining? `none | timeShift | aggregateWindow`

* one timeseries is regular, but the other is not - **aggregateWindow**

* two timeseries are regular, have the same rate, but metrics occur at a different time - **timeShift**

* two timeseries are regular, have the same rate, and metrics occur at the same time - **none**

* two timeseries are irregular - **aggregateWindow**

* two timeseries are regular, but metrics don't occur at the same time and rate - **aggregateWindow**
