import random
import time

import paramiko

# Create an ssh client to connect to the server
ssh = paramiko.SSHClient()
# Create an ssh whitelist
know_host = paramiko.AutoAddPolicy()
# Load the whitelist we created
ssh.set_missing_host_key_policy(know_host)

for i in range(600):
    # Connect to the server
    ssh.connect(
        hostname="106.15.64.74",
        port=22,
        username="your username",  # replace it with your username
        password="your password"  # replace it with your password
    )

    # invoke the shell
    shell = ssh.invoke_shell()
    shell.settimeout(1)
    print("No." + str(i) + " logged in.")

    # Have some sleep if you want
    sleep_time = random.uniform(3, 10)
    print("Sleep for " + str(sleep_time) + " seconds.")
    time.sleep(sleep_time)

    # Logout
    shell.send("exit")
    print("exited.")

    # Close the connection
    ssh.close()
