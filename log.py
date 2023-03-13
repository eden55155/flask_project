import os
import glob

check = max(glob.glob('/var/jenkins_home/jobs/Project/builds/*'),key=os.path.getctime)

check_file = os.path.exists('successlog.txt')
file_obj = open(f"{check}/log", "r")
file_data = file_obj.read()
lines = file_data.splitlines()
started = ''
date = ''
for line in lines:
    if 'Started by' in line:
        started = line
    if 'Date:' in line:
        date = line

finish = lines[-1]

if check_file:
    file = open("successlog.txt", "a")
    file.write(started)
    file.write(date)
    file.write(finish)
    file.write(' ')
else:
    file = open("successlog.txt", "w")
    file.write(f"{started} \n {date} \n {finish}")

