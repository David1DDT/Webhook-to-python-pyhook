
from discord_webhook import DiscordWebhook

# Replace with your webhook URL
webhook_url = 'https://discord.com/api/webhooks/1311359096947081216/8sGGkU67FyNGGYPCKH9M8xyzuVj-1EjVxFPcJjSSeNrCYmVWRcKQgL6HGsOKErELCmnw'
user = input("enter your user: ")
def webhook(mes):
# Create a webhook instance
    webhook = DiscordWebhook(url=webhook_url, content=mes,)

# Send the message
    response = webhook.execute()

    #

message = " "
while message != "user: " + user + "\n":
    message = "user: " + user + "\n" + input("enter the message: ")
    if message != "user: " + user + "\n":
        webhook(message)