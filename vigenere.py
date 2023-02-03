import re

class Vigenere():
    def __init__(self, master, pageManager):
        self.master = master
        self.origin = pageManager

    # enkripsi
    def enkripsi(self):
        output = ""
        for i in range(len(self.input)):
            output += chr((ord(self.input[i])-ord("A")+ord(self.key[i])-ord("A"))%26 + ord("A"))
        return output

    # dekripsi
    def dekripsi(self):
        output = ""
        for i in range(len(self.input)):
            output += chr((ord(self.input[i])-ord(self.key[i]))%26 + ord("A"))
        return output
    
    def start(self):
        input = self.input
        key = self.key
        input = re.sub("[^A-Za-z]","",input).upper()
        key = re.sub("[^A-Za-z]","",key).upper()
        for i in range(len(input)):
            key += key[i]
        self.input = input
        self.key = key
        return self



