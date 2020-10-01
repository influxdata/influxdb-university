#Flux training Agenda

## AM

### Slot 1 (45 mins)

* Motivation (15 mins)
	* Data-driven decision making 
	* Inspiring examples 
	* paradigmatic shift from historical analysis to reactive decision making

* Time series (15 mins)
 * example of time series
 * primary use cases
 * three real world examples from Factry
 * What is a time-series database (tsdb)?

* Influxdb 2.0 (15 mins)
   * What is InfluxDB/InfluxData?
   * Improvements from the past
	* Demo Factry + Cloud 2.0 UI presentation

### BREAK (10 mins)

### Slot 2 (45 mins)

* Data Ingestion (40 mins)
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

### BREAK (10 mins)

### Slot 3 (45 mins)

* Data Analysis
	* Flux query model basics and syntax
		* Table (th + demo)
		* Row processing (th + hands-on + demo)
			* Window (th + hands-on + demo)
				* Landmark 
					* range()
			* Filter by tag
			* Filter by value 
			* Functions (th + hands-on + demo)
				* Built-in 
					* mean()
					* last()
			* Window (th + hands-on + demo)
				* Sliding 
					* Aggregate Window

### LUNCH BREAK

## PM

### Slot 4 (45 mins)

* Set up Telegraf agent for system's metrics
* Data Analysis (cont.)
	* Advanced Functions
		* map
	* Custom functions (th + hands-on + demo) 
	* Join (th + hands-on + demo)
		* On time assuming synchronised data
		* On time approximating assuming a fixed delta (timeShift)
		* On time approximating assuming a maximum error (trucateTimeColumn)
		* On time exploiting windows

### BREAK (15 mins)

### Slot 5 (60 mins)

* Hands-on: implement the City Water Tank dashboard using Factry data
	* Case briefing
	* Work individually on dashboard creation a cell at a time
	* Individual discussion with instructors
	* Group discussion and feedback from the instructors
	
### BREAK (15 mins)

### Slot 6 (60 mins)

* Simple Alerts (th + demo + hands-on)
	* What is an alert?
	* How to set up an alert
	* Demo: CPU user usage above a threshold
	* Hands-on: Free Memory below a threshold
* Tasks (th + demo)
	* What is a Task?
	* Tasks common use cases
		* Downsampling data
		* Cleaning data
		* Enriching Data 
	* Anomaly detection 
		* Short intro on anomaly detection
		* A simple technique to find Anomalies (comparing long-term mean vs short-term mean)
		*
* Combining a Task with an Alert for anomaly detection (DEMO)

### BREAK (15 mins)

### Slot 7 (30 mins)

####Everything you've always wanted to know about Flux
##### SQL Connection
##### Pivoting
##### Histogram
##### Holt-Winters




 