file_obj = open("log", "r")

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
