from tkinter import *
import pickle
import random

beyaz = "#FFFFFF"
koyu_pembemsi = "#EF4F2C"
koyu_tema =  "#373A3E"
pembemsi = "#f3503d"

arkaplan = koyu_tema
yazi = beyaz
btnrnk = pembemsi
actvbtn = koyu_pembemsi

root = Tk()
root.title("Edebiyat Sınavına")
root.configure(bg=arkaplan)
root.geometry("300x300")

wn = Toplevel()
wn.configure(bg=arkaplan)
wn.withdraw()

eslesme = {'oğuz atay': ['beyaz mantolu adam'], 'mustafa kutlu': ['yoksulluk içimizde'], 'rasim özdenören': ['çözülme'], 'ferit edgü': ['koşucu'], 'necip fazıl': ['kaldırımlar'], 'cahit sıtkı': ['gün eksilmesin penceremden'], 'sedat umran': ['devin uyanışı'], 'nazım hikmet': ['kerem gibi'], 'atilla ilhan': ['rinna-rinnan-nay'], 'arif nihat': ['bayrak'], 'bekir sıtkı': ['kışlada bahar'], 'orhan veli': ['galata köprüsü'], 'melih cevdet': ['rahatı kaçan ağıç'], 'edip cansever': ['gelmiş bulundum'], 'turgut uyar': ['çokluk senindir'], 'sezai karakoç': ['sürgün ülkeden başkentler başkentine'], 'erdem bayazıt': ['birazdan gün doğacak'], 'ismet özel': ['aynı adam'], 'haydar ergülen': ['sis'], 'hüseyin atlansoy': ['metropol insanları'], 'aşık veysel': ['kara toprak'], 'abdulrahim karakoç': ['unutursun'], 'kaşgarlı mahmut': ['divanu lugatuturk']}
try:
	with open("yazarlar_dict.pickle", "rb") as f:
		eslesme = pickle.load(f)
except:
	with open("yazarlar_dict.pickle", "wb") as f:
		pickle.dump(eslesme,f)

def add_f():
    def on_closing():
        wn.withdraw()

    wn.protocol("WM_DELETE_WINDOW", on_closing)
    wn.deiconify()

add_b = Button(root, text="Ekle", command=add_f,font= ("Arial",12,"bold"), bg=btnrnk, foreground=yazi, activebackground= actvbtn, activeforeground=yazi)

def esles_f():
	yazar = yzr_ekle.get()
	eser = esr_ekle.get()
	if yazar != "":
		if eser != "":
			if yazar not in eslesme.keys():
				eslesme[f"{yazar}"] = [eser]
			elif eser not in eslesme.values():
				eslesme[f"{yazar}"] += [eser]
			with open("yazarlar_dict.pickle", "wb") as f:
				pickle.dump(eslesme, f)
			dictonlab.config(text=eslesme)
	yzr_ekle.delete(0,"end")
	esr_ekle.delete(0,"end")

yzr_ekle = Entry(wn,font= ("Arial",12,"bold"))
esr_ekle = Entry(wn,font= ("Arial",12,"bold"))
dictonlab = Label(wn, text=f"{eslesme}",font= ("Arial",12,"bold"), bg=arkaplan, foreground=yazi)
esles_b = Button(wn, text="Eşleştir", command=esles_f,font= ("Arial",12,"bold"), bg=btnrnk, foreground=yazi, activebackground= actvbtn, activeforeground=yazi)
ne1 = Label(wn, text="Yazar:",font= ("Arial",12,"bold"), bg=arkaplan, foreground=yazi)
ne2 = Label(wn, text="Eser:",font= ("Arial",12,"bold"), bg=arkaplan, foreground=yazi)

sor_lab = Label(root, text="",font= ("Arial",12,"bold"), bg=arkaplan, foreground=yazi)

def play_f():
	if eslesme:
		sor_lab.config(text=random.choice(random.choice(list(eslesme.values()))))
	if not pridiction.winfo_viewable():
		pridiction.grid(row=4, column=0)


play = Button(root, text="Oyna", command=play_f,font= ("Arial",12,"bold"), bg=btnrnk, foreground=yazi, activebackground= actvbtn, activeforeground=yazi)
pridiction = Entry(root,font= ("Arial",12,"bold"))
istrue_l = Label(root, text="Oyna tıkla",font= ("Arial",12,"bold"), bg=arkaplan, foreground=yazi)


def istrue_f(pt):
	for k, v in eslesme.items():
		if sor_lab["text"] in v:
			if k == pt:
				play_f()
				istrue_l.config(text="Doğru bildin")
				break
			else:
				istrue_l.config(text=f"Bilemedin\ndoğru cevap: ({k}) olmalıydı")
				break

	pridiction.delete(0,"end")


pridiction.bind("<Return>", (lambda event: istrue_f(pridiction.get())))

add_b.grid(row=0, column=0)
play.grid(row=1, column=0)
sor_lab.grid(row=2, column=0)
istrue_l.grid(row=3, column=0)

ne1.grid(row=0, column=0)
ne2.grid(row=1, column=0)
yzr_ekle.grid(row=0, column=1)
esr_ekle.grid(row=1, column=1)
#dictonlab.grid(row=3, column=0)
esles_b.grid(row=4, column=0)

root.mainloop()
print(eslesme)
