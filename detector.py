import pyautogui

class Detector():
    def __init__(self, path, url):
        self.path = path
        self.webhook_url = url

    def capture(self):
        image = pyautogui.screenshot()
        image.save(str(self.path))

