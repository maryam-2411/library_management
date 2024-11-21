from tkinter import *
from tkinter import messagebox
from mydb2 import Database

db = Database("c:/class/products_info.db")
root = Tk()
root.geometry('600x400')
root.title("مدیریت کتابخانه")
root.configure(bg="white")

#funcs=============================================================
def add():
    db.add(ent_name.get(),ent_psell.get(),ent_pbuy.get(),ent_number.get())
    clear()
    show()

def search():
    if not ent_name.get():
        messagebox.showerror("Error","Please enter the product name.")
    lst_info.delete(0,END)
    rec1= db.search(ent_name.get())  
    if not rec1 :
        messagebox.showinfo("NotFound","No item found")
        return
    for i in rec1:
        lst_info.insert(END,i)
        
def delete(): 
    index = lst_info.curselection()
    data = lst_info.get(index)
    result = data.split(",")
    res = messagebox.askyesno("Delete","Are you sure to delete?")
    if res == True:
        db.delete(result[0])
    clear()
    show()

def edit():
    global result
    db.edit(result[0],ent_name.get(),ent_psell.get(),ent_pbuy.get(),ent_number.get())
    clear()
    show()

def show():
    lst_info.delete(0,END)
    records = db.show()
    for rec in records:
        lst_info.insert(END,f'{rec[0]},{rec[1]},{rec[2]},{rec[3]},{rec[4]}')

def exit():
    res = messagebox.askyesno("Exit","Are you sure to exit?")
    if res == True:
        root.destroy()

def clear():
    ent_name.delete(0,END)
    ent_psell.delete(0,END)
    ent_pbuy.delete(0,END)
    ent_number.delete(0,END)
    ent_name.focus_set()

def select(event):
    global result
    index = lst_info.curselection()
    data = lst_info.get(index)
    result = data.split(",")
    ent_name.insert(0,result[1])
    ent_psell.insert(0,result[2])
    ent_pbuy.insert(0,result[3])
    ent_number.insert(0,result[4])

#lables and entries===========================================================
lbl_name = Label(root,text='نام کالا:',font="lotus 13 bold",fg="black",bg='white')
lbl_name.place(x=30,y=20)
ent_name = Entry(root,width=25)
ent_name.place(x=120,y=25)

lbl_psell = Label(root,text='قیمت فروش:',font="lotus 13 bold",fg="black",bg='white')
lbl_psell.place(x=30,y=50)
ent_psell = Entry(root,width=25)
ent_psell.place(x=120,y=55)

lbl_pbuy = Label(root,text='قیمت خرید:',font="lotus 13 bold",fg="black",bg='white')
lbl_pbuy.place(x=300,y=20)
ent_pbuy = Entry(root,width=25)
ent_pbuy.place(x=390,y=25)

lbl_number = Label(root,text='تعداد:',font="lotus 13 bold",fg="black",bg='white')
lbl_number.place(x=300,y=50)
ent_number = Entry(root,width=25)
ent_number.place(x=390,y=55)

#listbox and scrollbar=========================================================
lst_info = Listbox(root,width=50,height=12)
lst_info.place(x=50,y=120)
sb = Scrollbar(root)
sb.place(x=337,y=121,height=194)
sb.config(command=lst_info.yview)
lst_info.bind('<<ListboxSelect>>',select)
#buttons=======================================================================
btn_add = Button(root,text='اضافه کردن',font='lotus 12 bold',width=13,bg="green",command=add)
btn_add.place(x=400,y=120)
btn_search = Button(root,text="جستجوی کالا",font='lotus 12 bold',width=13,bg="blue",command=search)
btn_search.place(x=400,y=160)
btn_delete = Button(root,text="حذف کالا",font='lotus 12 bold',width=13,bg="yellow",command=delete)
btn_delete.place(x=400,y=200)
btn_edit = Button(root,text="ویرایش",font='lotus 12 bold',width=13,bg="violet",command=edit)
btn_edit.place(x=400,y=240)
btn_show = Button(root,text="نمایش",font='lotus 12 bold',width=13,bg="orange",command=show)
btn_show.place(x=400,y=280)
btn_exit = Button(root,text="بستن",font='lotus 12 bold',width=13,bg="red",command=exit)
btn_exit.place(x=400,y=320)

root.mainloop()