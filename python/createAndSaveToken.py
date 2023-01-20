from modifiedLibrary.farmbot import Farmbot, FarmbotToken

# Variables à remplir :
mail = ""
password = ""

# Télécharement du token d'identification
token = FarmbotToken.download_token(mail,
                                    password,
                                    "https://my.farm.bot")
fichierToken = open("token", 'wb')
fichierToken.write(token)
fichierToken.close()
