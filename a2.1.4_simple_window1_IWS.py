##############################################################################
#   a113_TR_simple_window1.py
#   Example soulution: Change its size to 200 by 100 pixels.
##############################################################################
import tkinter as tk

def test_my_button():
    frame_auth.tkraise()

# main window
root = tk.Tk()
root.wm_geometry("250x170")
root.title("Authorization")

# create empty frame
frame_login = tk.Frame(root)

frame_login.grid(row=0,column=0,sticky='news')

lbl_username = tk.Label(frame_login, text='Username',font=("Courier", 20))
lbl_username.pack()

ent_username = tk.Entry(frame_login, bd=2)
ent_username.pack()

lbl_password = tk.Label(frame_login, text='Password', anchor='center',font=("Courier", 20))
lbl_password.pack()

ent_password = tk.Entry(frame_login, bd=2,show='*')
ent_password.pack()

btn_login = tk.Button(frame_login, text='Login',command=test_my_button)
btn_login.pack()

frame_auth = tk.Frame(root)

frame_auth.grid(row=0,column=0,sticky='news')

frame_login.tkraise()
root.mainloop()