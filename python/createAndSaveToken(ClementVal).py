from modifiedLibrary.farmbot import Farmbot, FarmbotToken

# Télécharement du token d'identification
token = FarmbotToken.download_token("clement_dormois@etu.u-bourgogne.fr",
                                        "FARMBOTCLEMENTVAL",
                                        "https://my.farm.bot")
fichierToken = open("token", 'wb')
fichierToken.write(token)
fichierToken.close()