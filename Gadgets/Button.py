import RPi.GPIO as GPIO
import time

ButtonPin = 16
GPIO.setmode(GPIO.BCM)
GPIO.setup(ButtonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

print("Press button")

try:
    while True:
        if GPIO.input(ButtonPin) == GPIO.LOW:  # Button pressed
            print("Button pressed!")
            while GPIO.input(ButtonPin) == GPIO.LOW:
                time.sleep(0.01)  # Wait until button is released
            time.sleep(0.1)  # Debounce delay
        time.sleep(0.01)  # Polling delay

except KeyboardInterrupt:
    print("Program exited")

finally:
    GPIO.cleanup()
