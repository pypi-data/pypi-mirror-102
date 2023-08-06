from discord_webhooks import DiscordWebhooks

        
class RayDis:

    def __init__(self, url):
        self.webhook = DiscordWebhooks(url)

    def header(self, title, description):

        self.webhook.set_content(title=title,description=description ,color=242424)
    
    def body(self, msg_title, value):
        self.webhook.add_field(name=msg_title,value=value)

    def footer(self, text):
        self.webhook.set_footer(text=text)

    def send(self):
        self.webhook.send()

    