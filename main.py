from tkinter import *
from time import *

window = Tk()
window.title("Adion Food Center Receipt Generator")

window.config(bg="#D3D3D3")

main_frame = Frame(window, borderwidth=5)
main_frame.grid(row=3)


def update():
    time_string = strftime("%I:%M:%S %p")
    time_label.config(text=time_string)
    time_label.after(1000, update)


def costs():
    def parathes():
        global mon1
        one = int(entry1.get())
        mon1 = one * 10
        cost1 = Label(window, text=mon1, font=('sans serif', 15), bg="black", fg="red", relief=SUNKEN, borderwidth=5,
                      padx=15)
        cost1.grid(row=3, column=3)

    parathes()

    def mutter():
        global mon2
        one = int(entry2.get())
        mon2 = one * 150
        cost1 = Label(window, text=mon2, font=('sans serif', 15), bg="black", fg="red", relief=SUNKEN, borderwidth=5,
                      padx=15)
        cost1.grid(row=4, column=3)

    mutter()

    def water():
        global mon3
        one = int(entry3.get())
        mon3 = one * 200
        cost1 = Label(window, text=mon3, font=('sans serif', 15), bg="black", fg="red", relief=SUNKEN, borderwidth=5,
                      padx=15)
        cost1.grid(row=5, column=3)

    water()

    def cor():
        global mon4
        one = int(entry4.get())
        mon4 = one * 40
        cost1 = Label(window, text=mon4, font=('sans serif', 15), bg="black", fg="red", relief=SUNKEN, borderwidth=5,
                      padx=15)
        cost1.grid(row=6, column=3)

    cor()

    def gol():
        global mon5
        one = int(entry5.get())
        mon5 = one * 10
        cost1 = Label(window, text=mon5, font=('sans serif', 15), bg="black", fg="red", relief=SUNKEN, borderwidth=5,
                      padx=15)
        cost1.grid(row=7, column=3)

    gol()

    def idli():
        global mon6
        one = int(entry6.get())
        mon6 = one * 5
        cost1 = Label(window, text=mon6, font=('sans serif', 15), bg="black", fg="red", relief=SUNKEN, borderwidth=5,
                      padx=15)
        cost1.grid(row=8, column=3)

    idli()

    def sambhar():
        global mon7
        one = int(entry7.get())
        mon7 = one * 100
        cost1 = Label(window, text=mon7, font=('sans serif', 15), bg="black", fg="red", relief=SUNKEN, borderwidth=5,
                      padx=15)
        cost1.grid(row=9, column=3)

    sambhar()

    def dosa():
        global mon8
        one = int(entry8.get())
        mon8 = one * 185
        # if entry8.get == " ":
        #     mon1 = 0
        cost1 = Label(window, text=mon8, font=('sans serif', 15), bg="black", fg="red", relief=SUNKEN, borderwidth=5,
                      padx=15)
        cost1.grid(row=10, column=3)

    dosa()

    def nood():
        global mon9
        one = int(entry9.get())
        mon9 = one * 20
        # if entry8.get == " ":
        #     mon1 = 0
        cost1 = Label(window, text=mon9, font=('sans serif', 15), bg="black", fg="red", relief=SUNKEN, borderwidth=5,
                      padx=15)
        cost1.grid(row=11, column=3)

    nood()

    def vada():
        global mon10
        one = int(entry10.get())
        mon10 = one * 25
        # if entry8.get == " ":
        #     mon1 = 0
        cost1 = Label(window, text=mon10, font=('sans serif', 15), bg="black", fg="red", relief=SUNKEN, borderwidth=5,
                      padx=15)
        cost1.grid(row=12, column=3)

    vada()

    def coca():
        global mon11
        one = int(entry11.get())
        mon11 = one * 20
        cost1 = Label(window, text=mon11, font=('sans serif', 15), bg="black", fg="red", relief=SUNKEN, borderwidth=5,
                      padx=15)
        cost1.grid(row=13, column=3)

    coca()

    def pizza():
        global mon12
        one = int(entry12.get())
        mon12 = one * 500
        # if entry8.get == " ":
        #     mon1 = 0
        cost1 = Label(window, text=mon12, font=('sans serif', 15), bg="black", fg="red", relief=SUNKEN, borderwidth=5,
                      padx=15)
        cost1.grid(row=14, column=3)

    pizza()

    def burger():
        global mon13
        one = int(entry13.get())
        mon13 = one * 250
        # if entry8.get == " ":
        #     mon1 = 0
        cost1 = Label(window, text=mon13, font=('sans serif', 15), bg="black", fg="red", relief=SUNKEN, borderwidth=5,
                      padx=15)
        cost1.grid(row=15, column=3)

    burger()

    def do():
        global mon14
        one = int(entry14.get())
        mon14 = one * 30
        # if entry8.get == " ":
        #     mon1 = 0
        cost1 = Label(window, text=mon14, font=('sans serif', 15), bg="black", fg="red", relief=SUNKEN, borderwidth=5,
                      padx=15)
        cost1.grid(row=16, column=3)

    do()

    def chilli():
        global mon15
        one = int(entry15.get())
        mon15 = one * 200
        # if entry8.get == " ":
        #     mon1 = 0
        cost1 = Label(window, text=mon15, font=('sans serif', 15), bg="black", fg="red", relief=SUNKEN, borderwidth=5,
                      padx=15)
        cost1.grid(row=17, column=3)

    chilli()

    def french():
        global mon16
        one = int(entry16.get())
        mon16 = one * 100
        # if entry8.get == " ":
        #     mon1 = 0
        cost1 = Label(window, text=mon16, font=('sans serif', 15), bg="black", fg="red", relief=SUNKEN, borderwidth=5,
                      padx=15)
        cost1.grid(row=3, column=7)

    french()

    def tom():
        global mon17
        one = int(entry17.get())
        mon17 = one * 100
        # if entry8.get == " ":
        #     mon1 = 0
        cost1 = Label(window, text=mon17, font=('sans serif', 15), bg="black", fg="red", relief=SUNKEN, borderwidth=5,
                      padx=15)
        cost1.grid(row=4, column=7)

    tom()

    def hot():
        global mon18
        one = int(entry18.get())
        mon18 = one * 150
        # if entry8.get == " ":
        #     mon1 = 0
        cost1 = Label(window, text=mon18, font=('sans serif', 15), bg="black", fg="red", relief=SUNKEN, borderwidth=5,
                      padx=15)
        cost1.grid(row=5, column=7)

    hot()

    def corn():
        global mon19
        one = int(entry19.get())
        mon19 = one * 150
        # if entry8.get == " ":
        #     mon1 = 0
        cost1 = Label(window, text=mon19, font=('sans serif', 15), bg="black", fg="red", relief=SUNKEN, borderwidth=5,
                      padx=15)
        cost1.grid(row=6, column=7)

    corn()

    def pav():
        global mon20
        one = int(entry20.get())
        mon20 = one * 150
        # if entry8.get == " ":
        #     mon1 = 0
        cost1 = Label(window, text=mon20, font=('sans serif', 15), bg="black", fg="red", relief=SUNKEN, borderwidth=5,
                      padx=15)
        cost1.grid(row=7, column=7)

    pav()

    def manch():
        global mon21
        one = int(entry21.get())
        mon21 = one * 200
        # if entry8.get == " ":
        #     mon1 = 0
        cost1 = Label(window, text=mon21, font=('sans serif', 15), bg="black", fg="red", relief=SUNKEN, borderwidth=5,
                      padx=15)
        cost1.grid(row=8, column=7)

    manch()

    def mush():
        global mon22
        one = int(entry22.get())
        mon22 = one * 150
        # if entry8.get == " ":
        #     mon1 = 0
        cost1 = Label(window, text=mon22, font=('sans serif', 15), bg="black", fg="red", relief=SUNKEN, borderwidth=5,
                      padx=15)
        cost1.grid(row=9, column=7)

    mush()

    def papdi():
        global mon23
        one = int(entry23.get())
        mon23 = one * 60
        # if entry8.get == " ":
        #     mon1 = 0
        cost1 = Label(window, text=mon23, font=('sans serif', 15), bg="black", fg="red", relief=SUNKEN, borderwidth=5,
                      padx=15)
        cost1.grid(row=10, column=7)

    papdi()

    def fry():
        global mon24
        one = int(entry24.get())
        mon24 = one * 150
        # if entry8.get == " ":
        #     mon1 = 0
        cost1 = Label(window, text=mon24, font=('sans serif', 15), bg="black", fg="red", relief=SUNKEN, borderwidth=5,
                      padx=15)
        cost1.grid(row=11, column=7)

    fry()

    def orange():
        global mon25
        one = int(entry25.get())
        mon25 = one * 60
        # if entry8.get == " ":
        #     mon1 = 0
        cost1 = Label(window, text=mon25, font=('sans serif', 15), bg="black", fg="red", relief=SUNKEN, borderwidth=5,
                      padx=15)
        cost1.grid(row=12, column=7)

    orange()

    def litchi():
        global mon26
        one = int(entry26.get())
        mon26 = one * 60
        cost1 = Label(window, text=mon26, font=('sans serif', 15), bg="black", fg="red", relief=SUNKEN, borderwidth=5,
                      padx=15)
        cost1.grid(row=13, column=7)

    litchi()

    def mango():
        global mon27
        one = int(entry27.get())
        mon27 = one * 60
        # if entry8.get == " ":
        #     mon1 = 0
        cost1 = Label(window, text=mon27, font=('sans serif', 15), bg="black", fg="red", relief=SUNKEN, borderwidth=5,
                      padx=15)
        cost1.grid(row=14, column=7)

    mango()

    def but():
        global mon28
        one = int(entry28.get())
        mon28 = one * 15
        # if entry8.get == " ":
        #     mon1 = 0
        cost1 = Label(window, text=mon28, font=('sans serif', 15), bg="black", fg="red", relief=SUNKEN, borderwidth=5,
                      padx=15)
        cost1.grid(row=15, column=7)

    but()

    def chhola():
        global mon29
        one = int(entry29.get())
        mon29 = one * 175
        # if entry8.get == " ":
        #     mon1 = 0
        cost1 = Label(window, text=mon29, font=('sans serif', 15), bg="black", fg="red", relief=SUNKEN, borderwidth=5,
                      padx=15)
        cost1.grid(row=16, column=7)

    chhola()

    def dahi():
        global mon29
        one = int(entry29.get())
        mon29 = one * 175
        # if entry8.get == " ":
        #     mon1 = 0
        cost1 = Label(window, text=mon29, font=('sans serif', 15), bg="black", fg="red", relief=SUNKEN, borderwidth=5,
                      padx=15)
        cost1.grid(row=17, column=7)

    dahi()

    def bro():
        plus = mon1 + mon2 + mon3 + mon4 + mon5 + mon6 + mon7 + mon8 + mon9 + mon10 + mon11 + mon12 + mon13 + mon14 + mon15+mon16+mon17+mon18+mon19+mon20+mon21+mon22+mon23+mon24+mon25+mon26+mon27+mon28+mon29
        vu = Label(window, text=plus, font=("sans serif", 15), fg="purple")
        vu.grid(row=2, column=8)

    bro()


label1 = Label(window, text="Welcome to Adion Food Center Receipts", font=("sans serif", 30), fg="#00ff00", bg="black",
               borderwidth=20)
label1.grid(row=0, column=0, columnspan=11)

time_label = Label(window, font=("sans-serif", 25), bg="#D3D3D3", fg="#00ff00")
time_label.grid(row=1, column=0, columnspan=11)
update()

money = Label(window, text="Cost👇", font=('sans serif', 15))
money.grid(row=2, column=1)

label = Label(window, text="Amount👇", font=('sans serif', 15))
label.grid(row=2, column=2)

label2 = Label(window, text="Total👇", font=('sans serif', 15))
label2.grid(row=2, column=3)

money = Label(window, text="Cost👇", font=('sans serif', 15))
money.grid(row=2, column=5)

label = Label(window, text="Amount👇", font=('sans serif', 15))
label.grid(row=2, column=6)

label2 = Label(window, text="Total👇", font=('sans serif', 15))
label2.grid(row=2, column=7)

label3 = Label(window, text="Parathes:", font=('sans serif', 15), bg="blue", fg="gold", relief=GROOVE, borderwidth=5)
label3.grid(row=3, column=0)
money1 = Label(window, text="₹10/pc", font=('sans serif', 15), bg="violet", fg="turquoise", relief=GROOVE,
               borderwidth=5)
money1.grid(row=3, column=1)
entry1 = Entry(window, font=("sans serif", 13), borderwidth=5)
entry1.grid(row=3, column=2)

label4 = Label(window, text="Mutter Panneer:", font=('sans serif', 15), bg="blue", fg="gold", relief=GROOVE,
               borderwidth=5)
label4.grid(row=4, column=0)
money2 = Label(window, text="₹150/plate", font=('sans serif', 15), bg="violet", fg="turquoise", relief=GROOVE,
               borderwidth=5)
money2.grid(row=4, column=1)
entry2 = Entry(window, font=("sans serif", 13), borderwidth=5)
entry2.grid(row=4, column=2)

label5 = Label(window, text="Momo:", font=('sans serif', 15), bg="blue", fg="gold", relief=GROOVE, borderwidth=5)
label5.grid(row=5, column=0)
money3 = Label(window, text="₹200/plate", font=('sans serif', 15), bg="violet", fg="turquoise", relief=GROOVE,
               borderwidth=5)
money3.grid(row=5, column=1)
entry3 = Entry(window, font=("sans serif", 13), borderwidth=5)
entry3.grid(row=5, column=2)

label6 = Label(window, text="Cornetto:", font=('sans serif', 15), bg="blue", fg="gold", relief=GROOVE, borderwidth=5)
label6.grid(row=6, column=0)
money4 = Label(window, text="₹40/pc", font=('sans serif', 15), bg="violet", fg="turquoise", relief=GROOVE,
               borderwidth=5)
money4.grid(row=6, column=1)
entry4 = Entry(window, font=("sans serif", 13), borderwidth=5)
entry4.grid(row=6, column=2)

label7 = Label(window, text="Gol Gappa:", font=('sans serif', 15), bg="blue", fg="gold", relief=GROOVE, borderwidth=5)
label7.grid(row=7, column=0)
money5 = Label(window, text="₹10/5pc", font=('sans serif', 15), bg="violet", fg="turquoise", relief=GROOVE,
               borderwidth=5)
money5.grid(row=7, column=1)
entry5 = Entry(window, font=("sans serif", 13), borderwidth=5)
entry5.grid(row=7, column=2)

label8 = Label(window, text="Idli:", font=('sans serif', 15), bg="blue", fg="gold", relief=GROOVE, borderwidth=5)
label8.grid(row=8, column=0)
money6 = Label(window, text="₹5/pc", font=('sans serif', 15), bg="violet", fg="turquoise", relief=GROOVE, borderwidth=5)
money6.grid(row=8, column=1)
entry6 = Entry(window, font=("sans serif", 13), borderwidth=5)
entry6.grid(row=8, column=2)

label9 = Label(window, text="Sambhar:", font=('sans serif', 15), bg="blue", fg="gold", relief=GROOVE, borderwidth=5)
label9.grid(row=9, column=0)
money7 = Label(window, text="₹100/bowl", font=('sans serif', 15), bg="violet", fg="turquoise", relief=GROOVE,
               borderwidth=5)
money7.grid(row=9, column=1)
entry7 = Entry(window, font=("sans serif", 13), borderwidth=5)
entry7.grid(row=9, column=2)

label10 = Label(window, text="Dosa:", font=('sans serif', 15), bg="blue", fg="gold", relief=GROOVE, borderwidth=5)
label10.grid(row=10, column=0)
money8 = Label(window, text="₹185/plate", font=('sans serif', 15), bg="violet", fg="turquoise", relief=GROOVE,
               borderwidth=5)
money8.grid(row=10, column=1)
entry8 = Entry(window, font=("sans serif", 13), borderwidth=5)
entry8.grid(row=10, column=2)

label11 = Label(window, text="Noodles:", font=('sans serif', 15), bg="blue", fg="gold", relief=GROOVE, borderwidth=5)
label11.grid(row=11, column=0)
money9 = Label(window, text="₹20/plate", font=('sans serif', 15), bg="violet", fg="turquoise", relief=GROOVE,
               borderwidth=5)
money9.grid(row=11, column=1)
entry9 = Entry(window, font=("sans serif", 13), borderwidth=5)
entry9.grid(row=11, column=2)

label12 = Label(window, text="Vada Pav:", font=('sans serif', 15), bg="blue", fg="gold", relief=GROOVE, borderwidth=5)
label12.grid(row=12, column=0)
money10 = Label(window, text="₹25/pc", font=('sans serif', 15), bg="violet", fg="turquoise", relief=GROOVE,
                borderwidth=5)
money10.grid(row=12, column=1)
entry10 = Entry(window, font=("sans serif", 13), borderwidth=5)
entry10.grid(row=12, column=2)

label13 = Label(window, text="Coke:", font=('sans serif', 15), bg="blue", fg="gold", relief=GROOVE, borderwidth=5)
label13.grid(row=13, column=0)
money11 = Label(window, text="₹20/bottle", font=('sans serif', 15), bg="violet", fg="turquoise", relief=GROOVE,
                borderwidth=5)
money11.grid(row=13, column=1)
entry11 = Entry(window, font=("sans serif", 13), borderwidth=5)
entry11.grid(row=13, column=2)

label14 = Label(window, text="Pizza:", font=('sans serif', 15), bg="blue", fg="gold", relief=GROOVE, borderwidth=5)
label14.grid(row=14, column=0)
money12 = Label(window, text="₹500/pc", font=('sans serif', 15), bg="violet", fg="turquoise", relief=GROOVE,
                borderwidth=5)
money12.grid(row=14, column=1)
entry12 = Entry(window, font=("sans serif", 13), borderwidth=5)
entry12.grid(row=14, column=2)

label15 = Label(window, text="Burger:", font=('sans serif', 15), bg="blue", fg="gold", relief=GROOVE, borderwidth=5)
label15.grid(row=15, column=0)
money13 = Label(window, text="₹250/pc", font=('sans serif', 15), bg="violet", fg="turquoise", relief=GROOVE,
                borderwidth=5)
money13.grid(row=15, column=1)
entry13 = Entry(window, font=("sans serif", 13), borderwidth=5)
entry13.grid(row=15, column=2)

label16 = Label(window, text="Panneer Do Pyaza:", font=('sans serif', 15), bg="blue", fg="gold", relief=GROOVE,
                borderwidth=5)
label16.grid(row=16, column=0)
money14 = Label(window, text="₹30/plate", font=('sans serif', 15), bg="violet", fg="turquoise", relief=GROOVE,
                borderwidth=5)
money14.grid(row=16, column=1)
entry14 = Entry(window, font=("sans serif", 13), borderwidth=5)
entry14.grid(row=16, column=2)

label17 = Label(window, text="Chilli Panneer:", font=('sans serif', 15), bg="blue", fg="gold", relief=GROOVE,
                borderwidth=5)
label17.grid(row=17, column=0)
money15 = Label(window, text="₹200/plate", font=('sans serif', 15), bg="violet", fg="turquoise", relief=GROOVE,
                borderwidth=5)
money15.grid(row=17, column=1)
entry15 = Entry(window, font=("sans serif", 13), borderwidth=5)
entry15.grid(row=17, column=2)

label18 = Label(window, text="French Fries:", font=('sans serif', 15), bg="blue", fg="gold", relief=GROOVE,
                borderwidth=5)
label18.grid(row=3, column=4)
money16 = Label(window, text="₹100/plate", font=('sans serif', 15), bg="violet", fg="turquoise", relief=GROOVE,
                borderwidth=5)
money16.grid(row=3, column=5)
entry16 = Entry(window, font=("sans serif", 13), borderwidth=5)
entry16.grid(row=3, column=6)

label20 = Label(window, text="Tomato Soup:", font=('sans serif', 15), bg="blue", fg="gold", relief=GROOVE,
                borderwidth=5)
label20.grid(row=4, column=4)
money17 = Label(window, text="₹150/bowl", font=('sans serif', 15), bg="violet", fg="turquoise", relief=GROOVE,
                borderwidth=5)
money17.grid(row=4, column=5)
entry17 = Entry(window, font=("sans serif", 13), borderwidth=5)
entry17.grid(row=4, column=6)

label21 = Label(window, text="Hot N Sour:", font=('sans serif', 15), bg="blue", fg="gold", relief=GROOVE,
                borderwidth=5)
label21.grid(row=5, column=4)
money18 = Label(window, text="₹150/bowl", font=('sans serif', 15), bg="violet", fg="turquoise", relief=GROOVE,
                borderwidth=5)
money18.grid(row=5, column=5)
entry18 = Entry(window, font=("sans serif", 13), borderwidth=5)
entry18.grid(row=5, column=6)

label22 = Label(window, text="Corn Soup:", font=('sans serif', 15), bg="blue", fg="gold", relief=GROOVE,
                borderwidth=5)
label22.grid(row=6, column=4)
money19 = Label(window, text="₹150/bowl", font=('sans serif', 15), bg="violet", fg="turquoise", relief=GROOVE,
                borderwidth=5)
money19.grid(row=6, column=5)
entry19 = Entry(window, font=("sans serif", 13), borderwidth=5)
entry19.grid(row=6, column=6)

label23 = Label(window, text="Pav Bhaji:", font=('sans serif', 15), bg="blue", fg="gold", relief=GROOVE,
                borderwidth=5)
label23.grid(row=7, column=4)
money20 = Label(window, text="₹150/plate", font=('sans serif', 15), bg="violet", fg="turquoise", relief=GROOVE,
                borderwidth=5)
money20.grid(row=7, column=5)
entry20 = Entry(window, font=("sans serif", 13), borderwidth=5)
entry20.grid(row=7, column=6)

label24 = Label(window, text="Chilli Manchurian:", font=('sans serif', 15), bg="blue", fg="gold", relief=GROOVE,
                borderwidth=5)
label24.grid(row=8, column=4)
money21 = Label(window, text="₹200/bowl", font=('sans serif', 15), bg="violet", fg="turquoise", relief=GROOVE,
                borderwidth=5)
money21.grid(row=8, column=5)
entry21 = Entry(window, font=("sans serif", 13), borderwidth=5)
entry21.grid(row=8, column=6)

label25 = Label(window, text="Mushroom Soup:", font=('sans serif', 15), bg="blue", fg="gold", relief=GROOVE,
                borderwidth=5)
label25.grid(row=9, column=4)
money22 = Label(window, text="₹150/bowl", font=('sans serif', 15), bg="violet", fg="turquoise", relief=GROOVE,
                borderwidth=5)
money22.grid(row=9, column=5)
entry22 = Entry(window, font=("sans serif", 13), borderwidth=5)
entry22.grid(row=9, column=6)

label26 = Label(window, text="Papdi Chaat:", font=('sans serif', 15), bg="blue", fg="gold", relief=GROOVE,
                borderwidth=5)
label26.grid(row=10, column=4)
money23 = Label(window, text="₹60/plate", font=('sans serif', 15), bg="violet", fg="turquoise", relief=GROOVE,
                borderwidth=5)
money23.grid(row=10, column=5)
entry23 = Entry(window, font=("sans serif", 13), borderwidth=5)
entry23.grid(row=10, column=6)

label26 = Label(window, text="Fried Rice:", font=('sans serif', 15), bg="blue", fg="gold", relief=GROOVE,
                borderwidth=5)
label26.grid(row=11, column=4)
money24 = Label(window, text="₹200/plate", font=('sans serif', 15), bg="violet", fg="turquoise", relief=GROOVE,
                borderwidth=5)
money24.grid(row=11, column=5)
entry24 = Entry(window, font=("sans serif", 13), borderwidth=5)
entry24.grid(row=11, column=6)

label27 = Label(window, text="Orange Juice:", font=('sans serif', 15), bg="blue", fg="gold", relief=GROOVE,
                borderwidth=5)
label27.grid(row=12, column=4)
money25 = Label(window, text="₹60/glass", font=('sans serif', 15), bg="violet", fg="turquoise", relief=GROOVE,
                borderwidth=5)
money25.grid(row=12, column=5)
entry25 = Entry(window, font=("sans serif", 13), borderwidth=5)
entry25.grid(row=12, column=6)

label28 = Label(window, text="Litchi Juice:", font=('sans serif', 15), bg="blue", fg="gold", relief=GROOVE,
                borderwidth=5)
label28.grid(row=13, column=4)
money26 = Label(window, text="₹60/glass", font=('sans serif', 15), bg="violet", fg="turquoise", relief=GROOVE,
                borderwidth=5)
money26.grid(row=13, column=5)
entry26 = Entry(window, font=("sans serif", 13), borderwidth=5)
entry26.grid(row=13, column=6)

label29 = Label(window, text="Mango Juice:", font=('sans serif', 15), bg="blue", fg="gold", relief=GROOVE,
                borderwidth=5)
label29.grid(row=14, column=4)
money27 = Label(window, text="₹60/glass", font=('sans serif', 15), bg="violet", fg="turquoise", relief=GROOVE,
                borderwidth=5)
money27.grid(row=14, column=5)
entry27 = Entry(window, font=("sans serif", 13), borderwidth=5)
entry27.grid(row=14, column=6)

label30 = Label(window, text="Butter Naan:", font=('sans serif', 15), bg="blue", fg="gold", relief=GROOVE,
                borderwidth=5)
label30.grid(row=15, column=4)
money28 = Label(window, text="₹15/pc", font=('sans serif', 15), bg="violet", fg="turquoise", relief=GROOVE,
                borderwidth=5)
money28.grid(row=15, column=5)
entry28 = Entry(window, font=("sans serif", 13), borderwidth=5)
entry28.grid(row=15, column=6)

label31 = Label(window, text="Chhola Bhatura:", font=('sans serif', 15), bg="blue", fg="gold", relief=GROOVE,
                borderwidth=5)
label31.grid(row=16, column=4)
money29 = Label(window, text="₹175/plate", font=('sans serif', 15), bg="violet", fg="turquoise", relief=GROOVE,
                borderwidth=5)
money29.grid(row=16, column=5)
entry29 = Entry(window, font=("sans serif", 13), borderwidth=5)
entry29.grid(row=16, column=6)

label31 = Label(window, text="Dahi Vada:", font=('sans serif', 15), bg="blue", fg="gold", relief=GROOVE,
                borderwidth=5)
label31.grid(row=17, column=4)
money29 = Label(window, text="₹75/plate", font=('sans serif', 15), bg="violet", fg="turquoise", relief=GROOVE,
                borderwidth=5)
money29.grid(row=17, column=5)
entry29 = Entry(window, font=("sans serif", 13), borderwidth=5)
entry29.grid(row=17, column=6)

btn = Button(window, text="Calculate", font=('sans serif', 25), borderwidth=10, pady=200, fg="#00ff00", bg="black",
             activeforeground="#00ff00", activebackground="black", command=costs)
btn.grid(row=3, rowspan=17, column=8, columnspan=11)

window.mainloop()