from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer

chatbot = ChatBot(name='CBOT')

corpus_trainer = ChatterBotCorpusTrainer(chatbot)

corpus_trainer.train(
    "chatterbot.corpus.english.greetings",
    "chatterbot.corpus.english.conversations"
)

list_trainer = ListTrainer(chatbot)

with open("chatbotapp/custom_responses/custom_responses.yml") as f:
    list_trainer.train(f.read().splitlines())
