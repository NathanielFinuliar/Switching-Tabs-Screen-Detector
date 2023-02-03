import pyautogui, socket
from discord_webhook import DiscordWebhook, DiscordEmbed

class Detector():
    def __init__(self, path, url):
        self.path = path
        self.webhook_url = url

    def capture(self):
        image = pyautogui.screenshot()
        image.save(str(self.path))
    
    def webhook_Event(self):
        hostname = socket.gethostname()
        webhook = DiscordWebhook(url=self.webhook_url)
