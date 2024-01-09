import time
import sys
from adafruit_servokit import ServoKit

pca = ServoKit(channels=16)
def init():
    pca.servo[0].angle = 50
    pca.servo[1].angle = 50
    pca.servo[5].angle = 50
    pca.servo[6].angle = 50
    pca.servo[14].angle = 50
   
    sys.exit()

init()