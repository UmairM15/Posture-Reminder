import random
import subprocess
import time

PHRASE = "Fix your posture!"
LOW_TIME = 30
HIGH_TIME = 300

while True:
    waitTime = random.randint(LOW_TIME, HIGH_TIME)
    print(f"Waiting {waitTime} seconds...")
    time.sleep(waitTime)

    subprocess.run(
        [
            "powershell",
            "-ExecutionPolicy",
            "Bypass",
            "-Command",
            f"Add-Type -AssemblyName System.Speech; "
            f"(New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak('{PHRASE}')",
        ]
    )
