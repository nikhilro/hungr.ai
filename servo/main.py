import RPi.GPIO as GPIO
import PIL
import picamera
from time import sleep

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
BTN = 22

class Servo():
	def __init__(self, PIN):
		GPIO.setup(PIN, GPIO.OUT)
		self.pwm = GPIO.PWM(PIN, 50)
		self.pwm.start(7.5)
		self.angle = 0

	def setAngle(self, angle):
		set_angle = 0.053*angle + 2.2
		self.pwm.ChangeDutyCycle(set_angle)
		self.angle = set_angle

	def adjustAngle(self, angle):
		self.setAngle(self.angle + angle)

	def stop(self):
		self.pwm.stop()

def setup():
	servo1 = Servo(17)
	GPIO.setup(BTN, GPIO.IN, pull_up_down=GPIO.PUD_UP)


def loop():
	flag = True
	while True:
		btnState = GPIO.input(BTN)
		if btnState == 0:
			if flag:
				servo1.setAngle(0)
			else:
				servo1.setAngle(180)
			flag = not flag


if __name__ == '__main__':		# Program start from here
	try:
		loop()
	except KeyboardInterrupt:	# When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
		servo1.stop()
		GPIO.cleanup()
