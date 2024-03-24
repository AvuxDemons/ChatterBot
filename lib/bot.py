from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer, ChatterBotCorpusTrainer

class CustomChatBot:

    # Constructor
    def __init__(self, name='Avux'):
        self.chatbot = ChatBot(name) # Bikin bot dari lib chatterbot
    
    # Fungsi Training
    def train(self, conversations):
        trainer = ListTrainer(self.chatbot) # Bikin alat training
        trainer.train(conversations) # Training Percakapan ( Array )
        trainer.export_for_training("./exports/training_data.json")
        return "Training completed."
    
    # Fungsi Training (Basic)
    def train_default(self):
        trainer = ChatterBotCorpusTrainer(self.chatbot) # Bikin alat training
        trainer.train("chatterbot.corpus.indonesia") # Training berdasarkan template
        return "Training completed."

    # Fungsi Chat
    def chat(self, user_input):
        return self.chatbot.get_response(user_input) # Mencari jawaban berdasarkan pertanyaan user
