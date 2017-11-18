import RPi.GPIO as GPIO
from time import sleep

BTN = 18
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)


class Servo():
	def __init__(self, PIN):
		GPIO.setup(PIN, GPIO.OUT)
		self.pwm = GPIO.PWM(PIN, 50)
		self.pwm.start(7.5)

	def setAngle(self, angle):
		set_angle = 0.053*angle + 2.2
		self.pwm.ChangeDutyCycle(set_angle)

	def move(self, angle):
		self.setAngle(0)
		sleep(0.75)
		self.setAngle(120)

	def stop(self):
		self.pwm.stop()


def move(n):
	if(n == 'B'):
		servoB.move()
	elif(n == 'G'):
		servoG.move()
	elif(n == 'O'):
		servoO.move()


def loop():
	print("program running")
	while True:
		btnState = GPIO.input(BTN)
		if btnState == 0:
			print("button press")
			move('B')
			move('G')
			move('O')
			sleep(0.75)


if __name__ == '__main__':		# Program start from here
	GPIO.setup(BTN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
	servoB = Servo(17)
	servoG = Servo(22)
	servoO = Servo(23)
	try:
		loop()
	except KeyboardInterrupt:	# When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
		servoB.stop()
		servoG.stop()
		servoO.stop()
		GPIO.cleanup()
