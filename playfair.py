import re
# key = "JALAN GANESHA SEPULUH"
# input = "temui ibu nanti malam"

class Playfair():
    def __init__(self, master, pageManager):
        self.master = master
        self.origin = pageManager
    
    def start(self):
        key = self.key
        input = self.input
        key = re.sub("[^A-Za-z]","",key).upper().replace("J","")
        if key != '':
            keyfinal = key[0]
            for i in range(len(key)):
                x = key[i]
                j = 0
                while x != "" and j < len(keyfinal):
                    if key[i] == keyfinal[j]:
                        x = ""
                    j += 1
                keyfinal += x
            
            abjad = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
            for i in range(25):
                x = abjad[i]
                j = 0
                while x != "" and j < len(keyfinal):
                    if abjad[i] == keyfinal[j]:
                        x = ""
                    j += 1
                keyfinal += x

            k = 0
            self.matrix = [['' for i in range(5) ] for j in range(5)]

            for i in range(5):
                for j in range(5):
                    self.matrix[i][j] = keyfinal[k]
                    k+=1
            # int(self.matrix)

            input = re.sub("[^A-Za-z]","",input).upper().replace("J","I")
            self.inputfinal = input[0]
            # Jangan sampai ada pasangan huruf yang sama. Jika ada, sisipkan x di tengahnya
            for i in input[1:]:
                # jika self.inputfinal berada pada suku kata ganjil, dicek apakah suku kata berikutnya sama dengan suku kata terakhir dari self.inputfinal
                if len(self.inputfinal)%2 != 0:
                    if i == self.inputfinal[-1]:
                        self.inputfinal += "X"+i
                    else:
                        self.inputfinal += i
                #jika self.inputfinal berada suku kata genap, tidak perlu dicek huruf berikutnya.
                else:
                    self.inputfinal += i
            # Jika jumlah huruf ganjil,tambahkan huruf x di akhir
            if len(self.inputfinal)%2 != 0:
                self.inputfinal += "X"
            
            return self
        else:
            self.Info = 'Pesan tidak dapat diproses, tidak ada key yang dimasukkan.'

    def position(char,matrix):
        for i in range(5):
            for j in range(5):
                if(matrix[i][j]==char):
                    return [i, j]
        

    # enkripsi
    def enkripsi(self):
        output =''
        for i in range(len(self.inputfinal)-1):
            if (i%2)== 0:
                index_1 = Playfair.position(self.inputfinal[i],self.matrix)
                index_2 = Playfair.position(self.inputfinal[i+1],self.matrix)

                if(index_1[0]==index_2[0]):
                    result= self.matrix[index_1[0]][(index_1[1]+1)%5]+self.matrix[index_2[0]][(index_2[1]+1)%5]
                elif(index_1[1]==index_2[1]):
                    result= self.matrix[(index_1[0]+1)%5][index_1[1]]+self.matrix[(index_2[0]+1)%5][index_2[1]]
                else:
                    result= self.matrix[index_1[0]][index_2[1]]+self.matrix[index_2[0]][index_1[1]]
                output+=result
        return output
        
        

    # dekripsi
    def dekripsi(self):
        # self.inputfinal = output
        output =''
        for i in range(len(self.inputfinal)-1):
            if (i%2)== 0:
                index_1 = Playfair.position(self.inputfinal[i],self.matrix)
                index_2 = Playfair.position(self.inputfinal[i+1],self.matrix)

                if(index_1[0]==index_2[0]):
                    result= self.matrix[index_1[0]][(index_1[1]-1)%5]+self.matrix[index_2[0]][(index_2[1]-1)%5]
                elif(index_1[1]==index_2[1]):
                    result= self.matrix[(index_1[0]-1)%5][index_1[1]]+self.matrix[(index_2[0]-1)%5][index_2[1]]
                else:
                    result= self.matrix[index_1[0]][index_2[1]]+self.matrix[index_2[0]][index_1[1]]
                output+=result

        return output






