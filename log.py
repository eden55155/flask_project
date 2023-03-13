import os

dirs = []
for dir in os.listdir('/var/jenkins_home/jobs/Project/builds'):
    if dir.isnumeric():
       dirs.append(dir)

buildNo = sorted(dirs)[-1]

check_file = os.path.exists('successlog.csv')
file_obj = open(f"/var/jenkins_home/jobs/Project/builds/{buildNo}/log", "r")
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
    file = open("successlog.csv", "a")
    file.write(started)
    file.write(date)
    file.write(finish)
else:
    file = open("successlog.csv", "w")
    file.write(f"{started} \n")
    file.write(f"{date} \n")
    file.write(f"{finish} \n")
