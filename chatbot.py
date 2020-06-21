from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

revolve_bot = ChatBot(name='RevolveBot', read_only=True,
                      logic_adapters=['chatterbot.logic.MathematicalEvaluation', 'chatterbot.logic.BestMatch'])
                      
small_talk = [
               'Hi',
               'Hello',
               'How are you?'
               'How are you doing?'
               'What’s up?'
               'Good day',
               'Tell me something',
               'I’ll do that now',
               'Hello',
               'Thank you',
               'Goodbye',
               'How can you help me?',
               'Hi, my name is RevolveBot',
               'Happy birthday!',
               'I have a question',
              ]
small_talk_trainer = ListTrainer(revolve_bot)    
for item in (small_talk,):
    small_talk_trainer.train(item)
    
              