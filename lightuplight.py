import RPi.GPIO as GPIO
import time
import pywhatkit

LED_PIN = 23

#pywhatkit.sendwhatmsg("+353877997643" , "Hi", 14,27)
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN,GPIO.OUT)
#low is out
#high is in
while True:
	

	GPIO.output(LED_PIN,GPIO.HIGH)
	time.sleep(5)
	GPIO.output(LED_PIN,GPIO.LOW)
	time.sleep(5)


