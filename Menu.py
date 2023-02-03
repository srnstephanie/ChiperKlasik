import tkinter as tk
from tkinter import *
from tkinter import scrolledtext, ttk, filedialog
import vigenere, playfair, onetimepad, extendedvigenere
import pathlib
import os

class MenuPage(ttk.LabelFrame):

    def __init__(self, master, pageManager):
        super().__init__(master)
        self.master = master
        self.origin = pageManager
        self.pack()
        self.Menu()

    def Menu(self):
        # title
        self.isFile = False
        self.intro = Label(self, text = 'Cipher Klasik', font = "Helvetica 10 bold", justify=CENTER)
        self.intro.grid(sticky="n", row = 0, columnspan = 1, pady = 2, padx = 5)
        # choise
        self.choise = Frame(self)
        self.radio = IntVar()
        choise1 = ttk.Radiobutton(self.choise,variable=self.radio, value=1, text = "Vigenere Chiper", command=lambda:self.change_frame(0)).grid(sticky="w", row=1, column = 0, pady = 2, padx = 5)
        choise2 = ttk.Radiobutton(self.choise,variable=self.radio, value=2, text = "Extended Vigenere Chipher", command=lambda:self.change_frame(0)).grid(sticky="w", row=1, column = 1, pady = 2, padx = 5)
        choise3 = ttk.Radiobutton(self.choise,variable=self.radio, value=3, text = "Playfair Chipher",command=lambda:self.change_frame(0)).grid(sticky="w", row=1, column = 2, pady = 2, padx = 5)
        # choise4 = ttk.Radiobutton(self.choise,variable=self.radio, value=4, text = "Enigma Chipher").grid(sticky="w", row=1, column = 3, pady = 2, padx = 5)
        choise5 = ttk.Radiobutton(self.choise,variable=self.radio, value=5, text = "Onetime Pad",command=lambda:self.change_frame(0)).grid(sticky="w", row=1, column = 3, pady = 2, padx = 5)
        self.choise.grid(row = 1, columnspan = 3, sticky = "n", pady = 2)
        self.Frames = {}
        self.Frames[1] = Frame(self)
        self.Frames[1].grid(row = 2, sticky = "w", pady = 2)
        self.Framess()
        self.Frames[1].tkraise()
        self.intro = Label(self, text = 'Stephanie Hutagalung-18220001', font = "Helvetica 8", justify=CENTER)
        self.intro.grid(sticky="e", row = 3, columnspan = 1, pady = 2, padx = 5)
        

    def Framess(self):
        self.Frames[1] = Frame(self)
        # this will create a label widget 
        self.Frames[1].l1 = Label(self.Frames[1], text = "Input")
        self.Frames[1].l2 = Label(self.Frames[1], text = "Key")
        self.Frames[1].l3 = Label(self.Frames[1], text = "Mode")
        self.Frames[1].l4 = Label(self.Frames[1], text = "Output Type")
        self.Frames[1].l5 = Label(self.Frames[1], text = "Output")
        self.Frames[1].l1.grid(row = 2, column = 0, sticky = "w", pady = 2)
        self.Frames[1].l2.grid(row = 3, column = 0, sticky = "w", pady = 2)
        self.Frames[1].l3.grid(row = 4, column = 0, sticky = "w", pady = 2)
        self.Frames[1].l4.grid(row = 5, column = 0, sticky = "w", pady = 2)
        self.Frames[1].l5.grid(row = 7, column = 0, sticky = "w", pady = 2)
        # this will arrange entry widgets
        self.Frames[1].e1 = scrolledtext.ScrolledText(self.Frames[1], wrap=tk.WORD,
                                            width=80, height=4,
                                            font=("Times New Roman", 10))

        self.Frames[1].e2 = scrolledtext.ScrolledText(self.Frames[1], wrap=tk.WORD,
                                            width=80, height=4,
                                            font=("Times New Roman", 10))
        self.Frames[1].e3 = LabelFrame(self.Frames[1])
        self.Frames[1].radioe3 = IntVar()
        ttk.Radiobutton(self.Frames[1].e3, text="Encrypt", variable=self.Frames[1].radioe3, value=1).grid(sticky="w", row = 1, column = 0)
        ttk.Radiobutton(self.Frames[1].e3, text="Decrypt", variable=self.Frames[1].radioe3, value=2).grid(sticky="w", row = 1, column = 1)
    
        self.Frames[1].e4 = LabelFrame(self.Frames[1])
        self.Frames[1].radioe4 = IntVar()
        ttk.Radiobutton(self.Frames[1].e4, text="without space", variable=self.Frames[1].radioe4, value=1).grid(sticky="w", row = 0, column = 0)
        ttk.Radiobutton(self.Frames[1].e4, text="5-huruf", variable=self.Frames[1].radioe4, value=2).grid(sticky="w", row = 0, column = 1)

        self.Frames[1].e5 = scrolledtext.ScrolledText(self.Frames[1], wrap=tk.WORD,
                                            width=80, height=4,
                                            font=("Times New Roman", 10))
        self.Frames[1].e1.grid(sticky="w", row = 2, column = 1, pady = 2)
        self.Frames[1].e2.grid(sticky="w", row = 3, column = 1, pady = 2)
        self.Frames[1].e3.grid(sticky="w", row = 4, column = 1, pady = 2)
        self.Frames[1].e4.grid(sticky="w", row = 5, column = 1, pady = 2)
        self.Frames[1].e5.grid(sticky="w", row = 7, column = 1, pady = 2)
        self.Frames[1].b1 = Button(self.Frames[1],text="Add file", command=lambda number = 1:self.open_text(number))
        self.Frames[1].b2 = Button(self.Frames[1],text="Save file", command=lambda number = 1:self.save_text(number))
        self.Frames[1].b3 = Button(self.Frames[1], width=10, text = "Run", command =lambda number = 1:self.run(number))
        self.Frames[1].b4 = Button(self.Frames[1], width=10,text = "Reset", command=lambda number = 1:self.reset(number))
        self.Frames[1].b1.grid(row=2, column = 2, pady = 2, padx = 5)
        self.Frames[1].b2.grid(sticky="w", row=7, column = 2, pady = 2, padx = 5)
        self.Frames[1].b3.grid(sticky="n", row=6, columnspan = 3, pady = 2, padx = 5)
        self.Frames[1].b4.grid(sticky="n", row=8, columnspan = 3, pady = 2, padx = 5)
        self.Frames[1].grid(row = 2, sticky = "w", pady = 2)


    def change_frame(self, number):
        if number == 0:
            self.Frames[1].tkraise()
        else:
            pass
            
    def startPage(self):
        self.mainloop()

    def open_text(self, number):

        self.filename = filedialog.askopenfilename(
            title='Open a file',
            initialdir='/'
            )
        
        if self.radio.get() != 2:
            if os.path.splitext(self.filename) == 'txt':
                read = open(self.filename)
                fileinput = read.read()
                self.Frames[number].e1.delete('0.0', tk.END)
                self.Frames[number].e1.insert(tk.END, fileinput)
            else:
                self.Frames[number].e5.delete('0.0', tk.END)
                self.Frames[number].e5.insert(tk.END, 'file tidak dapat diproses')
        else: 
            self.isFile = True
            self.Frames[number].e1.delete('0.0', tk.END)
            self.Frames[number].e1.insert(tk.END, 'Tekan run untuk memproses file')

    def save_text(self, number):
        try:
            filetypes = (
                ('text files', '*.txt'),
                ('All files', '*.*')
            )

            save = filedialog.asksaveasfile(
                mode='w',
                title='Save file',
                initialdir='/',
                filetypes=filetypes,
                defaultextension=".txt")
            output = ''
            output = self.Frames[number].e5.get("1.0", "end-1c")
            save.write(output)
            save.close 
        except:
            FALSE


    def run(self, number):
        try:
            self.input = self.Frames[number].e1.get("1.0", "end-1c")
            self.key = self.Frames[number].e2.get("1.0", "end-1c")
            self.mode = self.Frames[number].radioe3.get()
            self.outputtype = self.Frames[number].radioe4.get()
            self.typeoutput = self.Frames[number].e5
            self.keyy = self.Frames[number].e2
            if self.key != '' or self.radio.get() == 5:
                # vigenere
                if self.radio.get() == 1:
                    vigenere.Vigenere.start(self)
                    self.output =''
                    if self.mode == 1:
                        self.output = vigenere.Vigenere.enkripsi(self)
                    elif self.mode == 2:
                        self.output = vigenere.Vigenere.dekripsi(self)
                    self.outputspasi()
                # extended vigenere
                elif self.radio.get() == 2:    
                    self.output =''
                    if self.mode == 1:
                        self.output = extendedvigenere.Extendedvigenere.enkripsi(self)
                    elif self.mode == 2:
                        self.output = extendedvigenere.Extendedvigenere.dekripsi(self)
                    if self.isFile == FALSE :
                        self.outputspasi()
                # playfair
                elif self.radio.get() == 3:
                    self.output =''
                    playfair.Playfair.start(self)
                    if self.mode == 1:
                        self.output = playfair.Playfair.enkripsi(self)
                    elif self.mode == 2:
                        self.output = playfair.Playfair.dekripsi(self)
                    self.outputspasi()
                # onetimepad
                elif self.radio.get() == 5:
                    self.output =''
                    if self.mode == 1:
                        onetimepad.OneTimePad.start(self)
                        self.output = onetimepad.OneTimePad.enkripsi(self)
                        self.keyy.delete('0.0', tk.END)
                        self.keyy.insert(tk.END, self.key)
                    elif self.mode == 2:
                        onetimepad.OneTimePad.startdenkripsi(self)
                        if self.key == '':
                            self.output = 'Pesan tidak dapat diproses, key tidak sesuai.'
                        else:
                            self.output = onetimepad.OneTimePad.dekripsi(self)
                    self.outputspasi()
            else:
                self.output = 'Pesan tidak dapat diproses, silakan masukkan key.'
            self.typeoutput.delete('0.0', tk.END)
            self.typeoutput.insert(tk.END, self.output)
            self.isFile = FALSE
        except:
            FALSE

    def outputspasi(self):
        output_spasi = ''
        if self.outputtype == 1:
            output_spasi = self.output
        else:
            for i in range(len(self.output)):
                if i>0 and i%5==0:
                    output_spasi +=" " + self.output[i]
                else:
                    output_spasi += self.output[i]
        self.output = output_spasi
        return self.output
    
    def reset(self, number):
        self.Frames[number].e1.delete('0.0', tk.END)
        self.Frames[number].e2.delete('0.0', tk.END)
        self.Frames[number].e5.delete('0.0', tk.END)