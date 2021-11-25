from tkinter import *
from tkinter import ttk
from zemberekProcess import *

class TextNormalization():
    def __init__(self, parent):
        self.parent = parent
        self.parent.title("Turkish Text Normalization")

        self.anaCerceve = ttk.Frame(self.parent, padding=(3,3,12,12))
        self.anaCerceve.grid(row=0, column=0, sticky=(N,S,E,W))

        self.ebeveyn = self.anaCerceve

        self.tepeCerceve_style = ttk.Style()
        self.tepeCerceve_style.configure('My.TFrame', background='#8393a3')
        self.tepeCerceve = ttk.Frame(self.ebeveyn, padding=(3,3,12,12))

        self.tepeCerceve.pack(side=TOP, fill=X)

        CSPAN = 5
        ttk.Label(self.tepeCerceve, text = " Arama").grid(row=0, column=0, sticky=W+E, ipadx=4, ipady=2)
        self.aramaVar = StringVar()
        self.arama = ttk.Entry(self.tepeCerceve, textvariable=self.aramaVar)
        self.arama.grid(row=0, column=1, sticky=W+E+S+N, ipadx=4, ipady=2, columnspan=CSPAN)
        self.arama.bind("<Return>", self.aramaYap)

        self.a0 = Button(self.tepeCerceve, text=" Ara ", command=self.aramaYap)
        self.a0.grid(row=0, column=CSPAN+1)
        self.a1 = Button(self.tepeCerceve, text= " Ara Sil ", command=self.aramaSil)
        self.a1.grid(row=0, column=CSPAN+2)

        for i in range(CSPAN):
            self.tepeCerceve.grid_columnconfigure(1, minsize=50, weight=1)
        self.tepeCerceve.grid_rowconfigure(0, minsize=20, weight=1)

        self.cerceve2 = Frame(self.ebeveyn)
        self.cerceve2.pack(side=TOP, fill=X, ipady=2)

        style = ttk.Style()
        style.configure('TButton', borderwidth=1, relief="groove")
        style.configure('Normal.TButton', foreground="black")
        style.configure('Red.TButton', foreground="red")
        self.b0 = Button(self.cerceve2, text="Temizle ", command=self.temizle)
        self.b1 = Button(self.cerceve2, text="Düzelt", command=self.zemberek)

        self.b0.pack(side=LEFT);
        self.b1.pack(side=LEFT);

        self.cerceve4 = ttk.Frame(self.ebeveyn)
        self.cerceve4.pack(fill=BOTH, expand=1)

        self.girdiKutusu = Text(self.cerceve4, height=60)
        self.girdiKutusu.config(wrap=WORD)

        self.vscroll = ttk.Scrollbar(self.girdiKutusu, orient=VERTICAL, command=self.girdiKutusu.yview)
        self.girdiKutusu['yscroll'] = self.vscroll.set
        self.vscroll.pack(side=RIGHT, fill=Y)
        self.girdiKutusu.pack(fill=BOTH, expand=1)

        self.girdiKutusu.insert(END, "")

        self.yanCerceve = ttk.Frame(self.parent, padding=(3,3,12,12))
        self.yanCerceve.grid(row=1, column=0, sticky=(N,S,E,W))

        self.ciktiKutusu = Text(self.yanCerceve, height=60, width=60)
        self.ciktiKutusu.pack(fill=BOTH, expand=1)
        self.ciktiKutusu.config(wrap=WORD, width=60)

        self.vscroll2 = ttk.Scrollbar(self.ciktiKutusu, orient=VERTICAL,
                                      command=self.ciktiKutusu.yview)
        self.ciktiKutusu['yscroll'] = self.vscroll2.set
        self.vscroll2.pack(side=RIGHT, fill=Y)
        self.ciktiKutusu.insert(END, "")

        self.parent.grid_columnconfigure(0, minsize=400, weight=1)
        self.parent.grid_rowconfigure(0, minsize=200, weight=1)
        self.parent.grid_rowconfigure(1, minsize=200, weight=1)

    def zemberek(self):
        self.duzeltmismetin = zemberek_duzeltme_islemleri(self.girdiKutusu.get("1.0", END))
        self.ciktiKutusu.insert("end", self.duzeltmismetin)
        self.ciktiKutusu.insert("end", "\n")

    def temizle(self):
        self.girdiKutusu.delete("1.0", END)
        self.ciktiKutusu.delete("1.0", END)

    def aramaSil(self):
        self.aramaVar.set('')
        self.girdiKutusu.tag_remove('bulundu', '1.0', END)

    def aramaYap(self):
        self.aranacak = self.aramaVar.get()
        self.metin = self.girdiKutusu.get("1.0", END)
        self.girdiKutusu.tag_remove('bulundu', '1.0', END)

        if self.aranacak:
            endeks = '1.0'
            while 1:
                endeks = self.girdiKutusu.search(self.aranacak, endeks, nocase=1, stopindex=END)
                if not endeks: break
                sonendeks = f"{endeks}+{len(self.aranacak)}c"
                print(sonendeks)
                self.girdiKutusu.tag_add('bulundu', endeks, sonendeks)
                endeks = sonendeks
            self.girdiKutusu.tag_config('bulundu', foreground='red')
        self.arama.focus_set( )

def main():
    root = Tk()
    zemberek_baslat()
    TextNormalization(root)
    root.mainloop()
    zemberek_kapat()

if __name__ == "__main__":
    main()