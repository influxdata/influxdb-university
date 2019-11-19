import csv

basepath = "/Users/baldo/Google Drive (marco.balduini@quantiaconsulting.com)/Clienti/influxData/fluxTrain01/Materiale Training (sorgenti)/resources/data/factry/"

#name,tags,time,pump,tank,value
#pump_speed,,1546300800000000000,I1,city_water,0

filepath = 'pump_speed-filtered.csv'
outputfilepath = 'pump-speed-lp.txt'

timeToAdd = 25920000000000000

of=open(basepath + outputfilepath, "a+")

with open(basepath + filepath) as csv_file:
  csv_reader = csv.reader(csv_file, delimiter=',')
  line_count = 0
  for row in csv_reader:
    if line_count > 0:
      nl = row[0] + ",tank=" + row[4] + ",pump=" + row[3] + " value=" + row[5] + " " + str(int(row[2]) + timeToAdd) + "\n"
      print(nl)
      of.write(nl)
    line_count += 1