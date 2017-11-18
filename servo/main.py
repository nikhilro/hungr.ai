import RPi.GPIO as GPIO
import PIL
import picamera
import io
from time import sleep

BTN = 18

stream = io.BytesIO()
with picamera.PiCamera() as camera:
    camera.resolution = (640, 640)
    camera.start_recording(stream, format='h264', quality=23)
    camera.wait_recording(15)
    camera.stop_recording()

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

	def move(self, angle):
		self.setAngle(0)
		sleep(1)
		self.setAngle(120)

def move(n):
	if(n == 1):
		servoY.move()
	else if(n == 2):
		servoB.move()
	else if(n == 3):
		servoG.move()
	else:
		servoO.move()


def setup():
	GPIO.setwarnings(False)
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(BTN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
	servoY = Servo(17)
	servoB = Servo(27)
	servoG = Servo(22)
	servoO = Servo(23)
	

def destroy():
	servoY.stop()
	servoB.stop()
	servoG.stop()
	servoO.stop()
	GPIO.cleanup()

def loop():
	flag = True
	print("program running")
	while True:
		btnState = GPIO.input(BTN)
		if btnState == 0:
			print("button press")
			move(1)	


if __name__ == '__main__':		# Program start from here
	try:
		setup()
		loop()
	except KeyboardInterrupt:	# When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
		destroy()
