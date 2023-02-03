import re
class Extendedvigenere():
    def __init__(self, master, pageManager):
        self.master = master
        self.origin = pageManager
    def enkripsi(self):
        if self.isFile :
            f = open(self.filename, 'rb')
            fileData = bytearray(f.read())
            key = self.key
            key = re.sub("[^A-Za-z]","",key).upper()
            for i in range(len(fileData)):
                key += key[i]
            self.key = key
            for idx, plainText in enumerate(fileData):
                fileData[idx] = (plainText + ord(key[idx])) % 256
            f.close()
            f = open(self.filename, 'wb')
            f.write(fileData)
            f.close()
            self.output =  'file berhasil dienkripsi'
        else:
            Extendedvigenere.start(self)
            self.output = ""
            for i in range(len(self.input)):
                self.output += chr((ord(self.input[i])+ord(self.key[i]))%256 )
        return self.output

    def dekripsi(self):
        if self.isFile :
            f = open(self.filename, 'rb')
            fileData = bytearray(f.read())
            key = self.key
            key = re.sub("[^A-Za-z]","",key).upper()
            for i in range(len(fileData)):
                key += key[i]
            self.key = key
            for idx, plainText in enumerate(fileData):
                fileData[idx] = (plainText - ord(key[idx])) % 256
            f.close()
            f = open(self.filename, 'wb')
            f.write(fileData)
            f.close()
            self.output = 'file berhasil di dekripsi'
        else:
            Extendedvigenere.start(self)
            self.output = ""
            for i in range(len(self.input)):
                self.output += chr((ord(self.input[i])-ord(self.key[i]))%256 )
            # self.output()
        return self.output
    
    def start(self):
        input = self.input
        key = self.key
        key = re.sub("[^A-Za-z]","",key).upper()
        for i in range(len(input)):
            key += key[i]
        self.input = input
        self.key = key
        
        return self



