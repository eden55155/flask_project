import os

dirs = []

print('/////////')
print(os.listdir('/'))
for dir in os.listdir('/var/jenkins_home/jobs/Project/builds'):
    if dir.isnumeric():
       dirs.append(dir)

buildNo = sorted(dirs)[-1]

file_obj = open(f"/var/jenkins_home/jobs/Project/builds/{buildNo}/log", "r")

file_data = file_obj.read()
lines = file_data.splitlines()

for line in lines:
    if 'Started by' in line:
     started =line
    if 'Date:' in line:
       date = line

finish = lines[-1]

print(started)
print(date)
print(finish)
