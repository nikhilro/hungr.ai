import RPi.GPIO as GPIO
from time import sleep
import thread

BTN = 18
YELLOW = 0
GREEN = 1
ORANGE = 2
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

def servo_thread(servo_id):
	while True:
		if(socket_arr[servo_id]):
			servo_arr[servo_id].move()
			socket_arr[servo_id] = False


class Servo():
	def __init__(self, PIN):
		GPIO.setup(PIN, GPIO.OUT)
		self.pwm = GPIO.PWM(PIN, 50)
		self.pwm.start(7.5)

	def setAngle(self, angle):
		set_angle = 0.053*angle + 2.2
		self.pwm.ChangeDutyCycle(set_angle)

	def move(self):
		self.setAngle(0)
		sleep(0.75)
		self.setAngle(120)

	def stop(self):
		self.pwm.stop()


if __name__ == '__main__':		# Program start from here
	GPIO.setup(BTN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
	y = Servo(17)
	g = Servo(22)
	o = Servo(23)
	servo_arr = [y, g, o]
	try:
		thread.start_new_thread(servo_thread, YELLOW)
		thread.start_new_thread(servo_thread, GREEN)
		thread.start_new_thread(servo_thread, ORANGE)
	except KeyboardInterrupt:	# When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
		servo_arr[YELLOW].stop()
		servo_arr[GREEN].stop()
		servo_arr[ORGANGE].stop()
		GPIO.cleanup()