import random
import subprocess
import time

# Customization
# *Time is measured in seconds
PHRASE = "Fix your Posture!"
LOW_TIME = 30
HIGH_TIME = 300

# Silence loop
while True:
    waitTime = random.randint(30, 300)
    print(waitTime)
    time.sleep(waitTime)
    subprocess.run(["say", PHRASE])
