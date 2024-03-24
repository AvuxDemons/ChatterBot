from chatterbot import ChatBot, corpus
from chatterbot.trainers import ListTrainer, ChatterBotCorpusTrainer

class CustomChatBot:
    def __init__(self, name='Avux'):
        self.chatbot = ChatBot(name)

    def train(self, conversations):
        trainer = ListTrainer(self.chatbot)
        trainer.train(conversations)
        trainer.export_for_training("./exports/training_data.json")
        return "Training completed."
    
    def train_default(self):
        trainer = ChatterBotCorpusTrainer(self.chatbot)
        trainer.train("chatterbot.corpus.indonesia")
        return "Training completed."

    def chat(self, user_input):
        return self.chatbot.get_response(user_input)
