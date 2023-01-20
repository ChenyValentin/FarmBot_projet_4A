import time
from modifiedLibrary.farmbot import Farmbot, FarmbotToken
import threading

# Variables à remplacer
mail = "clement_dormois@etu.u-bourgogne.fr"
password = "FARMBOTCLEMENTVAL"


class MyHandler:
    def __init__(self, bot):
        # Maintain a flag that lets us know if the bot is
        # ready for more commands.
        self.busy = True
        self.bot = bot

    def on_connect(self, bot, mqtt_client):
        self.bot.read_status()

    def on_change(self, bot, state):
        is_busy = state['informational_settings']['busy']
        if is_busy != self.busy:
            if is_busy:
                print("Device is busy")
            else:
                print("Device is idle")
        self.busy = is_busy

    def on_log(self, _bot, log):
        print("LOG: " + log['message'])

    def on_response(self, _bot, _response):
        pass

    def on_error(self, _bot, response):
        print("ERROR: " + response.id)
        print("Reason(s) for failure: " + str(response.errors))


if __name__ == '__main__':
    raw_token = FarmbotToken.download_token(mail,
                                            password,
                                            "https://my.farm.bot")
    bot = Farmbot(raw_token)
    handler = MyHandler(bot)
    threading.Thread(target=bot.connect, name="foo", args=[handler]).start()

instructions = ["bot.move_absolute(x=400, y=600, z=-20)",
                "bot.take_photo()", "bot.go_to_home()", "bot.save_photo()"]

for cmd in instructions:
    while handler.busy:
        pass
    print(cmd)
    eval(cmd)
    time.sleep(2)
