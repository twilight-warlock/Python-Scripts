from time import sleep

host_temp = "hosts"
host_path = r"C:\Windows\System32\drivers\etc\hosts"
redirected = "127.0.0.1"
block_list = ["facebook.com", "www.facebook.com"]

while(True):
    with open(host_path,"r+") as f:
        content = f.read()
        for website in block_list:
            if website in content:
                pass
            else:
                f.write(redirected+" "+website+"\n")
    sleep(5)

# Next steps
# change file name to py to pyw
# Go to task scheduler
# Create a task
# Name: website blocker
# Tick the run with the highest priviledges
# Configure for: Choose OS
# Change tab to triggers
# Begin the task: At startup
# Change tab to actions and press on new
# Action : Start a program and choose this file with pyw extension
# Change tab to conditions
# Uncheck "Start the task only if the computer is on AC power"
# And the create
# Run the file and boom, can't access facebook anymore
    