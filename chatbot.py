import sys
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer, ChatterBotCorpusTrainer


def create_bot():
    return ChatBot(name='RevolveBot', read_only=False,
                   logic_adapters=['chatterbot.logic.MathematicalEvaluation', 'chatterbot.logic.BestMatch'])


def train(bot):                      
    small_talk = [
                    'hi there!',
                    'hi!',
                    'how do you do?',
                    'i\'m cool.',
                    'how are you?',
                    'I\'m doing okay, you?',
                    'i\'m ok',
                    'glad to hear that.',
                    'i\'m fine',
                    'glad to hear that.',
                    'i feel awesome',
                    'excellent, glad to hear that.',
                    'not so good',
                    'sorry to hear that.',
                    'Thank you',
                    'Goodbye',
                    'what\'s your name?',
                    'I\'m RevolveBot. ask me any question',
                    'I love ',
                    'I love her too!'                    
                  ]
    small_talk_trainer = ListTrainer(bot)    
    for item in (small_talk,):
        small_talk_trainer.train(item)


def serious_train(bot):
    corpus_trainer = ChatterBotCorpusTrainer(bot)
    corpus_trainer.train('chatterbot.corpus.english')
    