import RPi.GPIO as GPIO
import time

def toggle_pin(pin_num):
    GPIO.output(pin_num, GPIO.HIGH)
    print(f"Pin {pin_num} turned on")
    time.sleep(1)  # Wait for 1 second

    # Turn the pin off
    GPIO.output(pin_num, GPIO.LOW)
    print(f"Pin {pin_num} turned off")
    time.sleep(1)  # Wait for 1 second


if __name__ == "__main__":
    RED_PIN = 17
    GREEN_PIN = 27

    # Set the GPIO mode
    GPIO.setmode(GPIO.BCM)

    GPIO.setup(RED_PIN, GPIO.OUT)
    GPIO.setup(GREEN_PIN, GPIO.OUT)

    try:
        while True:
            toggle_pin(RED_PIN)
            toggle_pin(GREEN_PIN)
    except KeyboardInterrupt:
        # Clean up the GPIO pins before exiting
        GPIO.cleanup()
        print("Program terminated by user")