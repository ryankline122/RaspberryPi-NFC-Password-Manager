import RPi.GPIO as GPIO

class GPIOController:
    def __init__(self, output_pins):
        self.output_pins = output_pins

        # Set the GPIO mode
        GPIO.setmode(GPIO.BCM)

        for pin in self.output_pins:
            GPIO.setup(pin, GPIO.OUT)
        
    def set_pin(self, pin, state):
        GPIO.output(pin, state)

    def shutdown(self):
        GPIO.cleanup()