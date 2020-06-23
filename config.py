import sys
from flask import Flask
from chatbot import create_bot, train, serious_train


# create bot
revolve_bot = create_bot()

# train bot
train(revolve_bot)
serious_train(revolve_bot)

# create server
app = Flask(__name__)

