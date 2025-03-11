class Camera:
    def capture(self):
        print("Capturing photo.")

class Phone:
    def call(self):
        print("Making a call.")

class Smartphone(Camera, Phone):
    def browse(self):
        print("Browsing the internet.")



s = Smartphone()
s.capture()  
s.call()     
s.browse()
