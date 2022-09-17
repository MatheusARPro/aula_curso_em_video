from playsound import playsound
from time import sleep


for c in range(10, -1, -1):
    print(c)
    sleep(0.5)
playsound('ex046.mp3')
