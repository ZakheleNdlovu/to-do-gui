import tkinter
import time
file='file.txt'
list_ = []

main = tkinter.Tk()
main.geometry('300x450')
main.resizable(False,False)
main.configure(bg='gray')
main.title('To do list')

def clock():
    now = time.strftime('%a   %H : %M : %S  ')
    date.config(text=now)
    date.after(200,clock)

def add():
    global list_
    value = list.get(0, 'end')
    item = add_entry.get()
    list.insert('end',item)
    list_.append(item)
    add_entry.delete(0,'end')
    if value == '':
        with open(file, 'w') as f:
            f.write(f'{item}\n')

    else:
        with open(file, 'a') as f:
            f.write(f'{item}\n')


def load():
    global list_
    with open(file, 'r') as f:
        data = f.readlines()
        for i in data:
            list.insert('end', i )


def delete():
    global list_
    value = list.get(0,'end')
    list.delete('active')
    a = list.get(0,'end')
    a = '-'.join(a)
    a = a.split('-')
    if value == '':
        with open(file,'w') as f:
            f.write(''.join(a))
    else:
        with open(file,'w') as f:
            f.write(''.join(a))



label = tkinter.Label(main, text='TO DO', font=('rog fonts',25,'bold'),width=10)
label.pack(side='top',pady=9)

date = tkinter.Label(main, font=('rog fonts',15,'bold'))
date.pack(pady=9)
clock()

frame2= tkinter.Frame(main,width=280,height=30,bg='grey')
frame2.pack()


add_entry = tkinter.Entry(frame2, font=('Alef',12), width=25)
add_entry.pack(pady=9, side='left')

label = tkinter.Button(frame2, text='ADD',bg='black',fg='white',font=('Alef',9), command=add)
label.pack(side='right')

frame = tkinter.Frame(main,width=250,height=150,bg='grey')
frame.pack(pady=10)

list = tkinter.Listbox(frame,font=('Alef',12),width=26,height=8,cursor='hand2')
list.pack(side='left', fill='both',padx=2)
scrollbar = tkinter.Scrollbar(frame)
scrollbar.pack(side='right', fill='both')

list.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=list.yview)

delete_button = tkinter.Button(main, text='DELETE', font=('ink free',10,'bold'),width=20, command=delete)
delete_button.pack(pady=1)



load()
main.mainloop()