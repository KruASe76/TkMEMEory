from tkinter import *
import random, time

win=Tk()
win.geometry('489x501')
win.title('МЕМори')
win.resizable(False, False)

switch=False
FLOP, TICK=PhotoImage(file='images/bicycle_standard_red_flop.png'), PhotoImage(file='images/tick.png')
coord_list1, coord_list, btn_list=[], [], []
img_list=[PhotoImage(file='images/meme1.png'), PhotoImage(file='images/meme2.png'), PhotoImage(file='images/meme3.png'), PhotoImage(file='images/meme4.png'), PhotoImage(file='images/meme5.png'), PhotoImage(file='images/meme6.png'), PhotoImage(file='images/meme7.png'), PhotoImage(file='images/meme8.png'), PhotoImage(file='images/meme9.png'), PhotoImage(file='images/meme10.png')]*2

def check_win():
    for i in btn_list:
        if i['bg']!='#eeeeee':
            break
    else:
        time.sleep(1)
        exit()

def check():
    global switch, last_widget, current_widget, btn_list
    if True:
        if current_widget['image']==last_widget['image'] and current_widget['text']!=last_widget['text']:
            current_widget['bg'], last_widget['bg']='#fffffe', '#fffffe'
            check_win()
        else:
            for i in btn_list:
                if i['bg']=='#ffffff':
                    i['image']=FLOP
        try:
            last_widget['text'].replace('     ', '')
            last_widget['text']=int(last_widget['text'])
        except AttributeError:
            btn_list=[]

def tap(event):
    global switch, last_widget, current_widget
    if event.widget['bg']=='#ffffff' and str(event.widget['text']).isdigit():
        if switch:
            event.widget['image']=img_list[event.widget['text']]
            current_widget=event.widget
            win.after(300, check)
        else:
            event.widget['image']=img_list[event.widget['text']]
            event.widget['text']=str(event.widget['text'])
            event.widget['text']+=' '*5
            last_widget=event.widget

        switch=not switch

for i in range(5):
    for j in range(4):
        coord_list1.append((i, j))

for i in range(20):
    a=random.choice(coord_list1)
    coord_list.append(a)
    coord_list1.remove(a)

    btn=Button(win, width=84, height=112, text=i, image=FLOP, bg='#ffffff')
    btn.bind('<Button-1>', tap)
    btn_list.append(btn)

for i in range(len(btn_list)):
    btn_list[i].place(x=coord_list[i][0]*100, y=coord_list[i][1]*128)

win.mainloop()
