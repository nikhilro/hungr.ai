import RPi.GPIO as GPIO
from time import sleep
import thread
import socket
import struct
import threading

BTN = 18
YELLOW = 0
GREEN = 1
ORANGE = 2
TCP_IP = '169.254.211.112'
TCP_PORT = 25565
BUFFER_SIZE = 4
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
data = [False,False,False,False]

def servo_thread(thread_name,servo_id):
	while True:
		if(data[servo_id]):
			print(thread_name+ str(data))			
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
		sleep(0.6)
		self.setAngle(120)
		sleep(0.6)
		

	def stop(self):
		self.pwm.stop()


if __name__ == '__main__':		# Program start from here
        print("Client launched")
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((TCP_IP, TCP_PORT))
	GPIO.setup(BTN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
	y = Servo(17)
	g = Servo(22)
	o = Servo(23)
	print("Servo's initialized")
	servo_arr = [y, g, o]
	try:
		thread.start_new_thread(servo_thread, ("t-yellow", YELLOW))
		thread.start_new_thread(servo_thread, ("t-green",GREEN))
		thread.start_new_thread(servo_thread, ("t-orange",ORANGE))
		while True:
			rec_data = s.recv(BUFFER_SIZE)
    			data = list(struct.unpack('????',rec_data))
    		#	print("received data:", rec_data)
		#	print(threading.activeCount())
	except KeyboardInterrupt:	# When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
		servo_arr[YELLOW].stop()
		servo_arr[GREEN].stop()
		servo_arr[ORGANGE].stop()
		cleanup_stop_thread()
		s.close()
		GPIO.cleanup()
		quit()
