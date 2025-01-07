import sys, time

def typewriter(message):
    for char in message:
        sys.stdout.write(char)
        sys.stdout.flush()  
        time.sleep(0.01)

