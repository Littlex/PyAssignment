import subprocess
import time

commands = [
    'sleep 3',
    'ls -l /',
    'find /',
    'sleep 4',
    'find /usr',
    'date',
    'sleep 5',
    'uptime'
]

elapsed_time = []

for cmd in commands:
    start = time.time() 
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True, stderr=subprocess.STDOUT)
    p.communicate()
    if (p.poll() == 0):  # using poll() to check if commands finish and terminate properly.
      end = time.time()
      elapsed_time.append(end - start)
      
# round the time number into 2 decimals     
elapsed_time = [round(elem, 2) for elem in elapsed_time]

#print the report 
print("total elapsed time: %s"%round(sum(elapsed_time),2))
print("average time: %s"%round((sum(elapsed_time)/len(commands)),2))
print("command \"%s\""%commands[elapsed_time.index(max(elapsed_time))], \
"has maximum execution time: %s"%max(elapsed_time))
print("command \"%s\""%commands[elapsed_time.index(min(elapsed_time))],\
"has minimum execution time: %s"%min(elapsed_time))

