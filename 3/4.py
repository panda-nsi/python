import time

print("Faite CTRL + C pour stopper le programme")

try:
    while True:
        time.sleep(1.0)
        print("Heure courante:", time.strftime('%H:%M:%S'))
except:
    print("Programme stoppé !")
