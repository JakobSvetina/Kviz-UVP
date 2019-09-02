import tkinter as tk
from PIL import Image, ImageTk

class Kviz(tk.Tk):

    total = 0
    
    def __init__(self):
        tk.Tk.__init__(self)

        Kviz.total = tk.IntVar()

        vse_strani = tk.Frame(self)
        vse_strani.pack(side = "top", fill = "both", expand = True)

        self.stran = {}
        for F in (Zacetna_stran, Izbira_tezavnosti, Prvo_vprasanje, Drugo_vprasanje, Tretje_vprasanje, Cetrto_vprasanje, Peto_vprasanje, Konec_igre, Zmaga, Prvo_vprasanje_tezka, Drugo_vprasanje_tezka, Tretje_vprasanje_tezka, Cetrto_vprasanje_tezka, Peto_vprasanje_tezka):
            ime_strani = F.__name__
            frame = F(parent = vse_strani, controller = self)
            self.stran[ime_strani] = frame

            frame.grid(row = 0, column = 0, sticky = "nsew")

        self.pokazi_stran("Zacetna_stran")

    def pokazi_stran(self, ime_strani):
        frame = self.stran[ime_strani]
        frame.tkraise()

class Zacetna_stran(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        load = Image.open("zacetek.jpg")
        render = ImageTk.PhotoImage(load)
        img = tk.Label(self, image=render)
        img.image = render
        img.place(x = 200, y = 0)
     
        gumb = tk.Button(self, text = "Začetek", command = lambda: controller.pokazi_stran("Izbira_tezavnosti"))
        gumb.place(x = 300, y = 50)

class Izbira_tezavnosti(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        
        naslov = tk.Label(self, text = 'Izbira težavnosti', font = ("Helvetica", 20))
        naslov.pack()
        button = tk.Button(self, text = "Lahka (dovoljeni 2 napaki)", command = lambda: controller.pokazi_stran("Prvo_vprasanje"), font = ("Helvetica", 12))
        button.pack()
        button2 = tk.Button(self, text = "Težka (dovoljenih 0 napak)", command = lambda: controller.pokazi_stran("Prvo_vprasanje_tezka"), font = ("Helvetica", 12))
        button2.pack()

############LAHKA IGRA

class Prvo_vprasanje(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        total = Kviz.total

        vprasanje = tk.Label(self, text = "Znanje je:", font = ("Helvetica", 20))
        vprasanje.pack()
        odgovor1 = tk.Button(self, command = lambda: [counter(), preveri_napake()], text = 'Moč', font = ("Helvetica", 12))
        odgovor1.pack()
        odgovor2 = tk.Button(self, command = lambda: controller.pokazi_stran("Drugo_vprasanje"), text = 'Noč', font = ("Helvetica", 12))
        odgovor2.pack()
        stevec_napak = tk.Label(self, text = 'Število napak = ' + str(Kviz.total.get()), font = ("Helvetica", 10))
        stevec_napak.pack()

        def counter():
            Kviz.total.set(Kviz.total.get() + 1)
            stevec_napak.config(text = 'Število napak = ' + str(Kviz.total.get()))

        def preveri_napake():
            if total.get() > 2:
                controller.pokazi_stran("Konec_igre")

class Drugo_vprasanje(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        total = Kviz.total

        vprasanje = tk.Label(self, text = "Koliko je 7 krat 8?", font = ("Helvetica", 20))
        vprasanje.pack()
        odgovor1 = tk.Button(self, command = lambda: controller.pokazi_stran("Tretje_vprasanje"), text = '42', font = ("Helvetica", 12))
        odgovor1.pack()
        odgovor2 = tk.Button(self, command = lambda: [counter(), preveri_napake()], text = '48', font = ("Helvetica", 12))
        odgovor2.pack()
        self.stevec_napak = tk.Label(self, text = 'Število napak = ' + str(Kviz.total.get()), font = ("Helvetica", 10))
        self.stevec_napak.pack()

        self.osvezi_stevec()

        def counter():
            Kviz.total.set(Kviz.total.get() + 1)
            self.stevec_napak.config(text = 'Število napak = ' + str(Kviz.total.get()))

        def preveri_napake():
            if total.get() > 2:
                controller.pokazi_stran("Konec_igre")

    def osvezi_stevec(self):
        if Kviz.total.get() > -1:
            self.stevec_napak.config(text = 'Število napak = ' + str(Kviz.total.get()))
            self.stevec_napak.after(500, self.osvezi_stevec)
        
class Tretje_vprasanje(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        total = Kviz.total

        vprasanje = tk.Label(self, text = "Kako govori Smrtež?", font = ("Helvetica", 20))
        vprasanje.pack()
        odgovor1 = tk.Button(self, command = lambda: controller.pokazi_stran("Cetrto_vprasanje"), text = 'Z VELIKIMI TISKANIMI ČRKAMI', font = ("Helvetica", 12))
        odgovor1.pack()
        odgovor2 = tk.Button(self, command = lambda: [counter(), preveri_napake()], text = 'Smrtež ne govori', font = ("Helvetica", 12))
        odgovor2.pack()
        self.stevec_napak = tk.Label(self, text = 'Število napak = ' + str(Kviz.total.get()), font = ("Helvetica", 10))
        self.stevec_napak.pack()

        self.osvezi_stevec()
        
        def counter():
            Kviz.total.set(Kviz.total.get() + 1)
            self.stevec_napak.config(text = 'Število napak = ' + str(Kviz.total.get()))

        def preveri_napake():
            if total.get() > 2:
                controller.pokazi_stran("Konec_igre")

    def osvezi_stevec(self):
        if Kviz.total.get() > -1:
            self.stevec_napak.config(text = 'Število napak = ' + str(Kviz.total.get()))
            self.stevec_napak.after(500, self.osvezi_stevec)
        
class Cetrto_vprasanje(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        total = Kviz.total

        vprasanje = tk.Label(self, text = "Katera je temeljna merska enota vesolja?", font = ("Helvetica", 20))
        vprasanje.pack()
        odgovor1 = tk.Button(self, command = lambda: [counter(), preveri_napake()], text = 'Parsek', font = ("Helvetica", 12))
        odgovor1.pack()
        odgovor2 = tk.Button(self, command = lambda: controller.pokazi_stran("Peto_vprasanje"), text = 'Jard', font = ("Helvetica", 12))
        odgovor2.pack()
        self.stevec_napak = tk.Label(self, text = 'Število napak = ' + str(Kviz.total.get()), font = ("Helvetica", 10))
        self.stevec_napak.pack()

        self.osvezi_stevec()
        
        def counter():
            Kviz.total.set(Kviz.total.get() + 1)
            self.stevec_napak.config(text = 'Število napak = ' + str(Kviz.total.get()))

        def preveri_napake():
            if total.get() > 2:
                controller.pokazi_stran("Konec_igre")

    def osvezi_stevec(self):
        if Kviz.total.get() > -1:
            self.stevec_napak.config(text = 'Število napak = ' + str(Kviz.total.get()))
            self.stevec_napak.after(500, self.osvezi_stevec)
        
class Peto_vprasanje(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        total = Kviz.total

        vprasanje = tk.Label(self, text = "Ali lahko zaupamo ljudem, ki živijo v visokih stolpih?", font = ("Helvetica", 20))
        vprasanje.pack()
        odgovor1 = tk.Button(self, command = lambda: [counter(), preveri_napake()], text = 'DA', font = ("Helvetica", 12))
        odgovor1.pack()        
        odgovor2 = tk.Button(self, command = lambda: controller.pokazi_stran("Zmaga"), text = 'NE', font = ("Helvetica", 12))
        odgovor2.pack()
        self.stevec_napak = tk.Label(self, text = 'Število napak = ' + str(Kviz.total.get()), font=("Helvetica", 10))
        self.stevec_napak.pack()

        self.osvezi_stevec()
        
        def counter():
            Kviz.total.set(Kviz.total.get() + 1)
            self.stevec_napak.config(text = 'Število napak = ' + str(Kviz.total.get()))

        def preveri_napake():
            if total.get() > 2:
                controller.pokazi_stran("Konec_igre")

    def osvezi_stevec(self):
        if Kviz.total.get() > -1:
            self.stevec_napak.config(text = 'Število napak = ' + str(Kviz.total.get()))
            self.stevec_napak.after(500, self.osvezi_stevec)             

############TEŽKA IGRA
        
class Prvo_vprasanje_tezka(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        vprasanje = tk.Label(self, text = "Znanje je:", font = ("Helvetica", 20))
        vprasanje.pack()
        odgovor1 = tk.Button(self, command = lambda: controller.pokazi_stran("Zacetna_stran"), text = 'Moč', font = ("Helvetica", 12))
        odgovor1.pack()
        odgovor2 = tk.Button(self, command = lambda: controller.pokazi_stran("Drugo_vprasanje_tezka"), text = 'Noč', font = ("Helvetica", 12))
        odgovor2.pack()

class Drugo_vprasanje_tezka(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        vprasanje = tk.Label(self, text = "Koliko je 7 krat 8?", font = ("Helvetica", 20))
        vprasanje.pack()
        odgovor1 = tk.Button(self, command = lambda: controller.pokazi_stran("Tretje_vprasanje_tezka"), text = '42', font = ("Helvetica", 12))
        odgovor1.pack()
        odgovor2 = tk.Button(self, command = lambda: controller.pokazi_stran("Zacetna_stran"), text = '48', font = ("Helvetica", 12))
        odgovor2.pack()

class Tretje_vprasanje_tezka(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        vprasanje = tk.Label(self, text = "Kako govori Smrtež?", font = ("Helvetica", 20))
        vprasanje.pack()
        odgovor1 = tk.Button(self, command = lambda: controller.pokazi_stran("Cetrto_vprasanje_tezka"), text = 'Z VELIKIMI TISKANIMI ČRKAMI', font = ("Helvetica", 12))
        odgovor1.pack()
        odgovor2 = tk.Button(self, command = lambda: controller.pokazi_stran("Zacetna_stran"), text = 'Smrtež ne govori', font = ("Helvetica", 12))
        odgovor2.pack()

class Cetrto_vprasanje_tezka(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        vprasanje = tk.Label(self, text = "Katera je temeljna merska enota vesolja?", font = ("Helvetica", 20))
        vprasanje.pack()
        odgovor1 = tk.Button(self, command = lambda: controller.pokazi_stran("Zacetna_stran"), text = 'Parsek', font = ("Helvetica", 12))
        odgovor1.pack()
        odgovor2 = tk.Button(self, command = lambda: controller.pokazi_stran("Peto_vprasanje_tezka"), text = 'Jard', font = ("Helvetica", 12))
        odgovor2.pack()

class Peto_vprasanje_tezka(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        vprasanje = tk.Label(self, text = "Ali lahko zaupamo ljudem, ki živijo v visokih stolpih?", font = ("Helvetica", 20))
        vprasanje.pack()
        odgovor1 = tk.Button(self, command = lambda: controller.pokazi_stran("Zacetna_stran"), text = 'DA', font = ("Helvetica", 12))
        odgovor1.pack()
        odgovor2 = tk.Button(self, command = lambda: controller.pokazi_stran("Zmaga"), text = 'NE', font = ("Helvetica", 12))
        odgovor2.pack()

############KONEC IGRE

class Konec_igre(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        konec = tk.Label(self, text = "Konec igre", font = ("Helvetica", 20))
        konec.pack()        
        
class Zmaga(tk.Frame):
    
    def __init__(self, parent, controller):    
        tk.Frame.__init__(self, parent)
        self.controller = controller

        load = Image.open("zmaga.jpg")
        render = ImageTk.PhotoImage(load)
        img = tk.Label(self, image=render)
        img.image = render
        img.place(x = 250, y = 0)

if __name__ == "__main__":
    kviz = Kviz()
    kviz.title("KVIZ")
    kviz.mainloop()
