#from chatterbot import ChatBot 
#from chatterbot.trainers import ListTrainer 
##from chatterbot.trainers import ChatterBotCorpusTrainer
#import sys
#sys.path.append('C:/Users/uros/Desktop/chatbot-udes')
#import torch
#from pytorch_chatbot import ChatBot
# Creating ChatBot Instance

#from load_model import load_model
#import torch


class ChatBot():
    def __init__(self, name):
        
        #self.checkpoint = torch.hub.load_state_dict_from_url(' https://onedrive.live.com/download?cid=7ECD9E8283ECE3E4&resid=7ECD9E8283ECE3E4%211959&authkey=AK0EzNNvg3GAcsE', map_location=torch.device('cpu'))

        self.name = name

    def get_response(self, input_text):
        return input_text

"""
class ChatBot1: 
    def __init__(self, name):
        self.name = name
        self.voc, self.encoder, self.decoder = load_model()
        self.searcher = GreedySearchDecoder(self.encoder, self.decoder)

    def get_response(self, input_text):
        return evaluateInput(self.encoder,self.decoder,
                             self.searcher,self.voc, input_text)
"""

chatbot = ChatBot('uros bot')