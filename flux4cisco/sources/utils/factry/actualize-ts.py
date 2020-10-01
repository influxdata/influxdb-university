import csv

basepath = ''

filepath = 'valve-state-lp.txt'
outputfilepath = 'act/valve-state-lp.txt'

fr = open(basepath + filepath, 'r') 
lines = fr.readlines()

time_to_add=25419600000000000
new_lines = []

for line in lines: 
    old_line = line.strip()
    new_ts = int(old_line[old_line.rfind(" ") + 1:]) + time_to_add
    new_lines.append(old_line[:old_line.rfind(" ") + 1]+str(new_ts)+"\n")

fr.close()

fr = open(basepath + outputfilepath, "w")
fr.writelines(new_lines)
fr.close()

print("{} actualized rows written to {} file".format(len(new_lines),outputfilepath))
