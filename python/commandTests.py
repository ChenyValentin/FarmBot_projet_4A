from modifiedLibrary.farmbot import Farmbot, FarmbotToken
import threading

class MyHandler:
    def __init__(self, bot):
        # Store "Z", "Q", "S", "D" in a queue
        self.queue = []
        # Maintain a flag that lets us know if the bot is
        # ready for more commands.
        self.busy = True
        self.bot = bot

    def add_job(self, user_input):
        if user_input[:3] == 'bot' :
            self.queue.append(user_input)
            self.bot.read_status()
        elif len(user_input) == 1 :
            d = user_input.capitalize()
            if d in ["Z", "Q", "S", "D"]:
                self.queue.append(d)
                self.bot.read_status()

    def try_next_job(self):
        if (len(self.queue) > 0) and (not self.busy):
            command = self.queue.pop(0)
            if len(command) > 1 :
                try :
                    return eval(user_input)
                except :
                    print('Bad command')
            self.busy = True
            if command == "Z":
                return self.bot.move_relative(100, 0, 0)
            if command == "Q":
                return self.bot.move_relative(0, -100, 0)
            if command == "S":
                return self.bot.move_relative(-100, 0, 0)
            if command == "D":
                return self.bot.move_relative(0, 100, 0)
    
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
        self.try_next_job()

    def on_log(self, _bot, log):
        print("LOG: " + log['message'])

    def on_response(self, _bot, _response):
        pass

    def on_error(self, _bot, response):
        print("ERROR: " + response.id)
        print("Reason(s) for failure: " + str(response.errors))


if __name__ == '__main__':
    raw_token = FarmbotToken.download_token("clement_dormois@etu.u-bourgogne.fr",
                                        "FARMBOTCLEMENTVAL",
                                        "https://my.farm.bot")
    bot = Farmbot(raw_token)
    handler = MyHandler(bot)
    threading.Thread(target=bot.connect, name="foo", args=[handler]).start()

while(True):
    user_input = input("> ")
    handler.add_job(user_input)
    handler.try_next_job()


# Envoyer une instruction LUA au Farmbot
bot.send_message({"kind": "send_message", "args": {"message": "lua.print('Hello, World!')"}})
