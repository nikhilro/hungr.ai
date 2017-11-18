import RPi.GPIO as GPIO
import PIL
import picamera
from time import sleep

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
	GPIO.setwarnings(False)
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(BTN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
	servo1 = Servo(17)

def destroy():
	servo1.stop()
	GPIO.cleanup()

def loop():
	flag = True
	print("program running")
	while True:
		btnState = GPIO.input(BTN)
		if btnState == 0:
			print("button press")
			if flag:
				servo1.setAngle(0)
			else:
				servo1.setAngle(180)
			flag = not flag


if __name__ == '__main__':		# Program start from here
	setup()
	try:
		loop()
	except KeyboardInterrupt:	# When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
		destroy()
