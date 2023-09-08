import os

BOT_TOKEN = os.environ.get("BOT_TOKEN", "6058774175:AAGZSP1R__rNvSeOAHoYrV6CIYbfEIF1db0")
SUDO = int(os.environ.get("SUDO", "6610195550"))
HEROKU = os.environ.get("HEROKU", "jeiekeoek")
APP_URL = "https://"+ HEROKU +".herokuapp.com/" + BOT_TOKEN
