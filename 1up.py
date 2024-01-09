import time
import sys
from adafruit_servokit import ServoKit




pca = ServoKit(channels=16)

pca.continuous_servo[5].throttle = 1
time.sleep(0.5)
pca.continuous_servo[5].throttle = 0
pca.deinit_channels()
sys.exit()