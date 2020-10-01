# Flux Training Agenda
#### Cisco - Virtual

## Day 1

### Slot 0 (30 min) [14:00-14:30] [8:00-8:30]

* Set up
* Who is who
* Use cases: what, when, how, pros, cons, ...
* Expectations

### Slot 1 (30 mins) [14:30-15:00] [8:30-9:00]

* Motivation 
	* Data-driven decision making 
	* Inspiring examples 
	* paradigmatic shift from historical analysis to reactive decision making

* Time series 
 * Example of time series
 * Primary use cases
 * Three real world examples from Factry
 * What is a time-series database (tsdb)?

* Influxdb 2.0 
   * What is InfluxDB/InfluxData?
   * Improvements from the past
	* Demo Factry + Cloud 2.0 UI presentation

### BREAK FOR Q&A (10 mins)

### Slot 2 (40 mins) [15:10-15:50] [9:10-9:50]

* Data Ingestion 
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

### BREAK FOR Q&A (10 mins)

### Slot 3 (50 mins) [16:00-16:50] [10:00-10:50]

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

### BREAK FOR Q&A (10 mins)

### Slot 4 (10 mins) [17:00-18:00] [11:00-12:00]

####  Bootcamp part I
* Implement a part of the City Water Tank dashboard using Factry data 
	* Case briefing
	* Work individually on dashboard creation a cell at a time
	* Coaching by the instructors 

## Day 2

### Slot 5 (20 mins) [14:00-14:20] [8:00-8:20]

* Group discussion on Bootcamp part I and feedbacks from the instructors

### Slot 6 (20 mins) [14:20-14:40] [8:20-8:40]
* Data Analysis (cont.)
	* Advanced Functions
		* map
	* Custom functions 

### BREAK FOR Q&A (10 mins)

### Slot 7 (40 mins) [14:50-15:30] [8:50-9:30]

* Data Analysis (cont.)
	* Joining Time Series
		* On time assuming synchronised data
		* On time approximating assuming a fixed delta (timeShift)
		* On time approximating assuming a maximum error (trucateTimeColumn)
		* On time exploiting windows
	
### BREAK FOR Q&A (10 mins)

### Slot 8 (50 mins) [15:40-16:30] [9:40-10:30]

####  Bootcamp part II
* Hands-on: complete the implementation of the City Water Tank dashboard using Factry data
	* Work individually on dashboard creation a cell at a time
	* Coaching by the instructors 
	* Group discussion and feedback from the instructors
	
### BREAK FOR Q&A (10 mins)
	
### Slot 9 (30 mins) [16:40-17:10] [10:40-11:10]

* Simple Alerts
	* What is an alert?
	* How to set up an alert
	* Demo: Sensor temperature out of range
* Tasks
	* What is a Task?
	* Demo: Tasks common use cases - Check the number of peaks in a temperature series

### BREAK FOR Q&A (10 mins)

### Slot 10 (40 mins) [17:20-18:00] [11:20-12:00]

* Anomaly detection
	* Demo: Anomaly detection using Linear Pizza Oven data 
* Time Series Forecasting
* Time Series Enrichment

### Q&A
 