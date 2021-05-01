from tkinter import *
import json
import matplotlib.pyplot as plt
from functools import partial
import tkinter.font as font
import numpy as np

f = open("data/data.json", "r")
data = json.load(f)
f.close()

age = ['(0, 2)', '(4, 6)', '(8, 12)', '(15, 20)', '(25, 32)', '(38, 43)', '(48, 53)', '(60, 100)']
gender = ["KADIN", "ERKEK"]
aylar = ["Ocak", "Şubat", "Mart", "Nisan", "Mayıs", "Haziran","Temmuz","Ağustos","Eylül","Ekim","Kasım","Aralık"]
def Display(ay):

    x = data[ay]
    age_data, gender_data = x["age"],x["gender"]
    plt.subplot(1,2,1).set_title("Cinsiyet Dağılımı")
    plt.pie(gender_data, labels = gender_data, autopct="%1.1f%%")
    plt.legend(gender, title="Cinsiyet",loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))

    plt.subplot(1,2,2).set_title("Yaş Dağılımı")
    plt.pie(age_data, labels=age_data, autopct="%1.1f%%")
    plt.legend(age, title="Yas Araligi:",loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))
    mng = plt.get_current_fig_manager()
    mng.window.state("zoomed")
    plt.show()

def AylikAnalizForGender():
    gender_data=[[0]*12,[0]*12]
    
    for i in range(12):
        gender_data[0][i]=data[i]["gender"][0]
        gender_data[1][i]=data[i]["gender"][1]
    sub=plt.subplot(111)
    x=np.arange(len(aylar))
    sub.bar(x-0.1,gender_data[0],width=0.2)
    sub.bar(x+0.1,gender_data[1],width=0.2)
    sub.set_ylabel("Müşteri Sayısı")
    sub.set_title("Bir Yıl Boyunca Gelen Müşterilerin Cinsiyete Göre Dağılımı")
    sub.legend(gender,title="cinsiyet")
    sub.set_xticks(x)
    sub.set_xticklabels(aylar)
    mng = plt.get_current_fig_manager()
    mng.window.state("zoomed")
    plt.show()

def AylikAnalizForAge():
    age_data=[[0]*12,[0]*12,[0]*12,[0]*12,[0]*12,[0]*12,[0]*12,[0]*12]
    for i in range(12):
        for j in range(8):
            age_data[j][i]=data[i]["age"][j]
            
    sub=plt.subplot(111)
    x=np.arange(len(aylar))
    a=-0.35
    for i in range(8):
        sub.bar(x+a,age_data[i],width=0.1)
        a+=0.1
    sub.set_ylabel("Müşteri Sayısı")
    sub.set_title("Bir Yıl Boyunca Gelen Müşterilerin Yaşa Göre Dağılımı")
    sub.legend(age,title="yaş")
    sub.set_xticks(x)
    sub.set_xticklabels(aylar)
    mng = plt.get_current_fig_manager()
    mng.window.state("zoomed")
    plt.show()


def YilAnaliz():
    gender_data=[0]*2
    age_data=[0]*8
    for i in range(12):
        gender_data[0]+=data[i]["gender"][0]
        gender_data[1]+=data[i]["gender"][1]
        for j in range(8):
            age_data[j]+=data[i]["age"][j]
    plt.subplot(1,2,1).set_title("Toplam Cinsiyet Dağılımı")
    plt.pie(gender_data, labels = gender_data, autopct="%1.1f%%")
    plt.legend(gender, title="Cinsiyet",loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))

    plt.subplot(1,2,2).set_title("Toplam Yaş Dağılımı")
    plt.pie(age_data, labels=age_data, autopct="%1.1f%%")
    plt.legend(age, title="Yas Araligi:",loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))
    mng = plt.get_current_fig_manager()
    mng.window.state("zoomed")
    plt.show()
  
root = Tk()
root.configure(background='#282828')
root.title("MAGAZA MÜŞTERİ İSTATİSTİKLERİ")
root.state('zoomed')

#genişlik: 1536, yukseklik: 864
height = root.winfo_screenheight()
width = root.winfo_screenwidth()
button = []
offset = -1


Lbl=Label(root,text="Ay Giriniz: ",font=("calibre,20,normal")).grid(padx=600,pady=10)
Txt=StringVar()
giris=Entry(root,textvariable=Txt,font=("calibre,20,normal")).grid(padx=600,pady=10)


def VerileriGoster():
    T=Txt.get().lower()
    for i in range(12):
        if(T==aylar[i].lower()):
            Display(i)
            return

btn1=Button(root,text="Verileri Göster",width=20,height=2,command=VerileriGoster).grid(padx=600,pady=10)
btn2=Button(root,text="Yıllık Cinsiyet Dağılımı",width=20,height=2,command=AylikAnalizForGender).grid(padx=600,pady=(50,10))
btn3=Button(root,text="Yıllık Yaş Dağılımı",width=20,height=2,command=AylikAnalizForAge).grid(padx=600,pady=10)
btn4=Button(root,text="Yıllık Analiz",width=20,height=2,command=YilAnaliz).grid(padx=600,pady=50)


root.mainloop()
