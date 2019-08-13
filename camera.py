from picamera import PiCamera
from time import sleep

NUM_PICTURES = 10

camera = PiCamera()

sleep(10)  
camera.start_preview()
for i in range(NUM_PICTURES):
    sleep(5)
    camera.capture('/home/pi/Desktop/image' + str(i) + '.jpg')
camera.stop_preview()

