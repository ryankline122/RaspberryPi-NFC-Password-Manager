from controllers.PN532Controller import PN532Controller
from controllers.GPIOController import GPIOController

import configparser

class App:
    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read("../config.ini")

        RED_PIN = int(self.config.get('LEDs', 'red'))
        GREEN_PIN = int(self.config.get('LEDs', 'green'))

        self.gpioController = GPIOController([RED_PIN, GREEN_PIN])
        self.nfcController = PN532Controller(
            GREEN_LED=GREEN_PIN, 
            RED_LED=RED_PIN,
            gpioController=self.gpioController
        )
    
    def run(self):
        try:
            self.nfcController.get_uid()
        except KeyboardInterrupt:
            self.gpioController.shutdown()
            print("Program terminated by user")


if __name__ == "__main__":
    app = App()
    app.run()