import re
import random


class OneTimePad():
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

    def startdenkripsi(self):
        input = self.input
        key = self.key
        input = re.sub("[^A-Za-z]","",input).upper()
        key = re.sub("[^A-Za-z]","",key).upper()
        if len(key) == len(input):
            for i in range(len(input)):
                key += key[i]
        else:
            key = ''
        self.input = input
        self.key = key
        return self

    def start(self):
        self.input = re.sub("[^A-Za-z]","",self.input).upper()
        key = OneTimePad.getKey(self)
        self.key = key
        return self

    def getKey(self):
        with open("key.txt", "r") as file:
            data = file.read()
        key = ''
        number = random.randrange(0, 1000, 1)
        for i in range(len(self.input)):
            key += data[number+i]
        return key

