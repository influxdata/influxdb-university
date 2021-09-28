import datetime
import time
import pytz
import os

try:
    #e.g. python actualize-ts.py 2021-09-14 12:00 GMT
    new_dt = datetime.datetime.strptime(sys.argv[1], '%Y-%m-%d %H:%M %Z')
except:
    new_dt = datetime.datetime.combine(
        datetime.date.today(), 
        datetime.time(12, 0),
        pytz.UTC)

new_dt_ms = int(new_dt.timestamp()*1000000000)

input_basepath='original-data/'
output_basepath='actualized-data/'

for filename in os.listdir(input_basepath):

    if filename.endswith('txt'):

        fr = open(input_basepath + filename, 'r') 
        lines = fr.readlines()

        first_line=lines[0].strip()
        time_to_add=new_dt_ms-int(first_line[first_line.rfind(" ") + 1:])

        new_lines = []

        for line in lines: 
            old_line = line.strip()
            new_ts = int(old_line[old_line.rfind(" ") + 1:]) + time_to_add
            new_lines.append(old_line[:old_line.rfind(" ") + 1]+str(new_ts)+"\n")

        fr.close()

        fr = open(output_basepath + filename, "w")
        fr.writelines(new_lines)
        fr.close()

        print("{} actualized rows written to {} file. Now data starts at {}.".format(len(new_lines),output_basepath + filename, new_dt))
    else:
        print("{} can't be processed".format(filename))