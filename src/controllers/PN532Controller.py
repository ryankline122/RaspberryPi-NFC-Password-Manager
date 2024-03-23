from includes.pn532 import *

class PN532Controller:
    def __init__(self, GREEN_LED, RED_LED, gpioController):
        self.GREEN_LED = GREEN_LED
        self.RED_LED = RED_LED
        self.gpc = gpioController

        try:
            self.pn532_spi = PN532_SPI(debug=False, reset=20, cs=4)

            ic, ver, rev, support = self.pn532_spi.get_firmware_version()
            print('Found PN532 with firmware version: {0}.{1}'.format(ver, rev))

            # Configure PN532 to communicate with MiFare cards
            self.pn532_spi.SAM_configuration()
        except Exception as e:
            print(e)
    
    def get_uid(self):
        print('Waiting for RFID/NFC card...')
        while True:
            uid = self.pn532_spi.read_passive_target(timeout=0.5)
            print('.', end="")

            if uid is None:
                self.set_led(self.RED_LED, 1)
                self.set_led(self.GREEN_LED, 0)
                continue

            print('Found card with UID:', uid.hex())
            self.set_led(self.RED_LED, 0)
            self.set_led(self.GREEN_LED, 1)

    def set_led(self, led, state):
        self.gpc.set_pin(led, state)