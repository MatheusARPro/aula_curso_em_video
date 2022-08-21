from playsound import playsound
from time import sleep


for c in range(10, 0, -1):
    print(c)
    sleep(1)
playsound('ex046.mp3')
