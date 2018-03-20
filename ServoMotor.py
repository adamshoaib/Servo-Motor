import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setup(29,GPIO.IN)
servoPin = 18
GPIO.setup(servoPin, GPIO.OUT)
pwm=GPIO.PWM(servoPin,50)
pwm.start(7)
while True:
    i=GPIO.input(29)
    if(i==0):
        print("inttrupt",i)
        DC = (1./18.)*(360)+2
        pwm.ChangeDutyCycle(DC)
        time.sleep(3)
    elif(i==1):
        print("nointurrept",i)
        DC = (1./18.)*(110)+2
        pwm.ChangeDutyCycle(DC)
        time.sleep(0.1)
pwm.stop()        
GPIO.cleanup()        