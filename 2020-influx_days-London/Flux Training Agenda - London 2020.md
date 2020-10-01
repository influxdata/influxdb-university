# Flux Training Agenda
####InfluxDays 2020 - London

## Day 1

### Slot -1 (30 min) [8:30-9:00] 

* Set up

### Slot 0 (30 min) [9:00-9:30]

* Who is who
* Use cases: what, when, how, pros, cons, ...
* Expectations

### Slot 1 (30 mins) [9:30-10:00]

* Motivation (12 mins)
	* Data-driven decision making 
	* Inspiring examples 
	* paradigmatic shift from historical analysis to reactive decision making

* Time series (12 mins)
 * example of time series
 * primary use cases
 * three real world examples from Factry
 * What is a time-series database (tsdb)?

* Influxdb 2.0 (6 mins)
   * What is InfluxDB/InfluxData?
   * Improvements from the past
	* Demo Factry + Cloud 2.0 UI presentation

### BREAK FOR Q&A (10 mins)

### Slot 2 (35 mins) [10:10-10:45]

* Data Ingestion (30 mins)
	* Generic data analytics pipeline
	* Conceptual View (Data Models)
		* Time series semantics
		* Bucket semantics
	* Logical View (Implementations)
	* Physical View (Syntaxes) 
		* Line Protocol
		* ... 
	* Use Case: Continuous Linear Pizza Oven
		* Pictorial presentation of the case
		* Demo: modelling of the temperature for both the sensors
		* Exercise: modelling the temperature and humidity measurements of the two sensors
		* Solution presentation & discussion  
		* Loading data in InfluxDB 2.0
		* Run your first query (5 mins) 

### BREAK FOR Q&A (15 mins)

### Slot 3 (50 mins) [11:00-11:50]

* Data Analysis
	* Flux query model basics and syntax
		* Table
		* Row processing
			* Window 
				* Landmark 
					* range()
			* Filter by tag & value
			* Functions
				* Built-in 
					* mean()
					* last()
			* Window
				* Sliding 
					* Aggregate Window

### Slot 4a (10 mins) [11:50-12:00]

####  BC part 1 - Home-work presentation
* Implement a part of the City Water Tank dashboard using Factry data 
	* Case briefing

## Day 2

### Slot 4b (30 mins) [8:30-9:00]

* Individual presentation of the BC part 1 solution
* Group discussion and feedback from the instructors

### BREAK FOR Q&A (10 mins)

### Slot 5 (45 mins) [9:10-9:55]

* Data Analysis (cont.)
	* Advanced Functions
		* map
	* Custom functions 
* Join
	* On time assuming synchronised data
	* On time approximating assuming a fixed delta (timeShift)
	* On time approximating assuming a maximum error (trucateTimeColumn)
	* On time exploiting windows
	
### BREAK FOR Q&A (10 mins)

### Slot 6 (45 mins) [10:05-10:50]

####  BC part 2
* Hands-on: complete the implementation of the City Water Tank dashboard using Factry data
	* Work individually on dashboard creation a cell at a time
	* Group discussion and feedback from the instructors
	
### BREAK FOR Q&A (10 mins)
	
### Slot 7 (20 mins) [11:00-11:20]

* Simple Alerts
	* What is an alert?
	* How to set up an alert
	* Demo: Sensor temperature out of range
* Tasks
	* What is a Task?
	* Demo: Tasks common use cases - Check the number of peaks in a temperature series

### Slot 8 (30 mins) [11:20-11:50]

* Anomaly detection
	* Demo: Anomaly detection using Linear Pizza Oven data 
* Time Series Forecasting
* Time Series Enrichment

### Q&A









 