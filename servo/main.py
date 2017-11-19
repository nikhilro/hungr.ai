import RPi.GPIO as GPIO
from time import sleep
import thread
import socket
import struct

BTN = 18
YELLOW = 0
GREEN = 1
ORANGE = 2
TCP_IP = '127.0.0.1'
TCP_PORT = 25565
BUFFER_SIZE = 4
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)


def servo_thread(servo_id):
	while True:
            data = s.recv(BUFFER_SIZE)
            data = struct.unpack('????',data)
            print("received data:", data)
		if(data[servo_id]):
			servo_arr[servo_id].move()
			data[servo_id] = False


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
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((TCP_IP, TCP_PORT))
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
