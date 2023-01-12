from farmbot import Farmbot, FarmbotToken

# Télécharement du token d'identification
token = FarmbotToken.download_token("clement_dormois@etu.u-bourgogne.fr",
                                        "FARMBOTCLEMENTVAL",
                                        "https://my.farm.bot")
fichierToken = open("token", 'wb')
fichierToken.write(token)
fichierToken.close()
# Créer une instance de Farmbot
bot = Farmbot(token)

class MyHandler:
    # The `on_connect` event is called whenever the device
    # connects to the MQTT server. You can place initialization
    # logic here.
    #
    # The callback is passed a FarmBot instance, plus an MQTT
    # client object (see Paho MQTT docs to learn more).
    def on_connect(self, bot, mqtt_client):
        # Once the bot is connected, we can send RPC commands.
        # Every RPC command returns a unique, random request
        # ID. Later on, we can use this ID to track our commands
        # as they succeed/fail (via `on_response` / `on_error`
        # callbacks):

        request_id1 = bot.move_absolute(x=10, y=20, z=30)


        request_id2 = bot.send_message("Hello, world!")


    def on_change(self, bot, state):
        pos = state["location_data"]["position"]
        xyz = (pos["x"], pos["y"], pos["z"])


    # The `on_log` event fires every time a new log is created.
    # The callback receives a FarmBot instance, plus a JSON
    # log object. The most useful piece of information is the
    # `message` attribute, though other attributes do exist.
    def on_log(self, bot, log):
        print("New message from FarmBot: " + log['message'])

    # When a response succeeds, the `on_response` callback
    # fires. This callback is passed a FarmBot object, as well
    # as a `response` object. The most important part of the
    # `response` is `response.id`. This `id` will match the
    # original request ID, which is useful for cross-checking
    # pending operations.
    def on_response(self, bot, response):
        print("ID of successful request: " + response.id)

    # If an RPC request fails (example: stalled motors, firmware
    # timeout, etc..), the `on_error` callback is called.
    # The callback receives a FarmBot object, plus an
    # ErrorResponse object.
    def on_error(self, bot, response):
        # Remember the unique ID that was returned when we
        # called `move_absolute()` earlier? We can cross-check
        # the ID by calling `response.id`:
        print("ID of failed request: " + response.id)
        # We can also retrieve a list of error message(s) by
        # calling response.errors:
        print("Reason(s) for failure: " + str(response.errors))


# Now that we have a handler class to use, let's create an
# instance of that handler and `connect()` it to the FarmBot:
handler = MyHandler()

# Once `connect` is called, execution of all other code will
# be pause until an event occurs, such as logs, errors,
# status updates, etc..
# If you need to run other code while `connect()` is running,
# consider using tools like system threads or processes.
# See: `example_threads.py` for inspiration.
bot.connect(handler)
print("This line will not execute. `connect()` is a blocking call.")