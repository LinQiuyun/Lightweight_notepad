import tkinter as tk
import tkinter.font as tkFont
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import random
from tkinter import filedialog
from tkinter import font
import ctypes
from pathlib import Path
import os
import shutil
import pystray
from PIL import Image
from pystray import MenuItem, Menu
import threading
import windnd
from tkinter.ttk import Separator
from tkinter import messagebox
p = os.path.dirname(__file__)
a_path = os.path.join(p, "a")
b_path = os.path.join(p, "b")
c_path = os.path.join(p,"c")
d_path = os.path.join(p,"d")
e_path = os.path.join(p,"e")
f_path = os.path.join(p,"f")
icon_path = os.path.join(p, "aaa.ico")

def save(theme):
    with open(b_path, 'w') as file:
        file.write(theme)
    with open(c_path, 'w') as file:
        file.write(str(v))
    with open(d_path,"w")as f:
        f.write(str(v2))
    with open(e_path,"w")as f:
        f.write(str(v2))
    with open(f_path,"w")as f:
        f.write(str(v2))

def load_theme():
    try:
        with open(b_path, 'r') as file:
            return file.read().strip()
    except FileNotFoundError:
        return None

def load():
    try:
        with open(c_path, 'r') as f:
            return f.read()
    except FileNotFoundError:
        pass

def load2():
    try:
        with open(d_path, 'r') as f:
            return f.read()
    except FileNotFoundError:
        pass

def load3():
    try:
        with open(e_path, 'r') as f:
            return f.read()
    except FileNotFoundError:
        pass

def load4():
    try:
        with open(f_path, 'r') as f:
            return f.read()
    except FileNotFoundError:
        pass

v = int(load() or 0)
v2 = int(load2() or 1)
v3 = int(load3() or 0)
v4 = int(load4() or 0)

def s():
    global v
    v = v + 1
def s2():
    global v2
    v2 = v2+1
def s3():
    global v3
    v3 = v3+1
def s4():
    global v4
    v4 = v4+1

def root_window():
    global theme_cbo
    window = ttk.Toplevel()
    def bao_chun(): 
        global v2,v3,v4
        p1=v2%2
        p2=v3%2
        p3=v4%2
        if p1+p2+p3==1:
            save(theme_cbo.get())    
        else:
            messagebox.showerror("错误", message="不支持多字体或无字体选择",parent=window)
    window.title("轻量记事本-设置")
    window.iconbitmap(icon_path)
    window.resizable()
    window_Button_two = ttk.Button(
        window, text="返回", bootstyle="outline", command=window.destroy)
    window_Button_two.grid(column=4,row=0,padx=10,pady=10)
    window_Button = ttk.Button(
        window, text="保存当前设置", bootstyle="outline", command=bao_chun)
    window_Button.grid(column=3,row=0,padx=10,pady=10)
    consider_var = ttk.IntVar()
    if v % 2 == 1:
        consider_var.set(1)
    else:
        consider_var.set(0)
    consider_checkbutton = ttk.Checkbutton(
        window, text="是否关联上一次保存的文件", variable=consider_var, command=s, bootstyle="round-toggle")
    consider_checkbutton.grid(column=1,row=3,padx=10,pady=10)
    style = ttk.Style()
    theme_names = style.theme_names()

    lbl = ttk.Label(window, text="选择主题:")
    lbl.grid(column=0,row=0,padx=10,pady=10,ipadx=5)
    lb2 = ttk.Label(window, text="选择字体:")
    lb2.grid(column=0,row=1,padx=10,pady=10,ipadx=5)
    lb3 = ttk.Label(window, text="各项设置:")
    lb3.grid(column=0,row=3,padx=10,pady=10,ipadx=5)
    sep = Separator(window)
    sep.grid(column=0, row=2,pady=50)
    theme_cbo = ttk.Combobox(master=window, values=theme_names)
    theme_cbo.grid(column=1,row=0,padx=10,pady=10)
    theme_cbo.current(theme_names.index(style.theme_use()))
    theme_cbo.bind('<<ComboboxSelected>>', change_theme)
    consider_var_2 = ttk.IntVar()
    if v2 % 2 == 1:
        consider_var_2.set(1)
    else:
        consider_var_2.set(0)
    consider_checkbutton2 = ttk.Checkbutton(window, text="宋体", variable=consider_var_2, command=s2, bootstyle="round-toggle")
    consider_checkbutton2.grid(column=1,row=1,padx=10,pady=10)

    consider_var_3 = ttk.IntVar()
    if v3 % 2 == 1:
        consider_var_3.set(1)
    else:
        consider_var_3.set(0)
    consider_checkbutton3 = ttk.Checkbutton(window, text="等线", variable=consider_var_3, command=s3, bootstyle="round-toggle")
    consider_checkbutton3.grid(column=2,row=1,padx=10,pady=10)

    consider_var_4 = ttk.IntVar()
    if v4 % 2 == 1:
        consider_var_4.set(1)
    else:
        consider_var_4.set(0)
    consider_checkbutton4 = ttk.Checkbutton(window, text="黑体", variable=consider_var_4, command=s4, bootstyle="round-toggle")
    consider_checkbutton4.grid(column=3,row=1,padx=10,pady=10)
    window.grid_rowconfigure(1, weight=1)
    window.grid_columnconfigure(0, weight=1)
    window.mainloop()

def change_theme(event):
    theme_cbo_value = theme_cbo.get()
    style.theme_use(theme_cbo_value)
    theme_cbo.selection_clear()

def quit_window(icon: pystray.Icon):
    icon.stop()
    root.destroy()
def show_window():
    root.deiconify()
def on_exit():
    root.withdraw()
menu = (MenuItem('显示', show_window, default=True), Menu.SEPARATOR, MenuItem('退出', quit_window))
image = Image.open(icon_path)
icon = pystray.Icon("icon", image, "轻量记事本", menu)



root = tk.Tk()
root.title("轻量记事本")
root.geometry()
root.iconbitmap(icon_path)
font_style1 = tkFont.Font(family="宋体", size=12)
font_style2 = tkFont.Font(family="等线", size=12)
font_style3 = tkFont.Font(family="黑体", size=12)
font_style = None
if v2 % 2 == 1:
    font_style = font_style1
elif v3 % 2 == 1:
    font_style = font_style2
elif v4 % 2 == 1:
    font_style = font_style3
ctypes.windll.shcore.SetProcessDpiAwareness(1)
ScaleFactor = ctypes.windll.shcore.GetScaleFactorForDevice(0)
root.tk.call('tk', 'scaling', ScaleFactor / 75)
style = ttk.Style()
current_theme = load_theme()
if current_theme in style.theme_names():
    style.theme_use(current_theme)
def 前_下拉框事件():
        if 下拉框.get() == "保存":
            save_2()
        if 下拉框.get() == "设置":
            root_window()
def 下拉框事件(event):
        x, y = event.x_root, event.y_root
        if 下拉框.winfo_rootx() < x < 下拉框.winfo_rootx() + 下拉框.winfo_width() and \
                下拉框.winfo_rooty() < y < 下拉框.winfo_rooty() + 下拉框.winfo_height():
            前_下拉框事件()
下拉菜单组 = ["保存", "设置"]
下拉框 = ttk.Combobox(root, values=下拉菜单组, state="readonly")
下拉框.grid(row=0, column=0, sticky="e")
下拉框.bind("<Button-3>", 下拉框事件)
下拉框.set("保存")
scrollbar = ttk.Scrollbar(root, style="TScrollbar", bootstyle="round")
scrollbar.grid(row=1, column=1, sticky="ns")
text_widget = tk.Text(root, wrap="word",
                          yscrollcommand=scrollbar.set, font=font_style)
text_widget.grid(row=1, column=0, sticky="nsew")
def a(event):
     deleted_text.append(text_widget.get('1.0', tk.END))
     text_widget.delete('1.0', tk.END)
deleted_text = []
def b():
    if deleted_text:
        deleted_content = deleted_text.pop()
        text_widget.insert(tk.END, deleted_content)
root.bind("<Shift_L> ", a)
root.bind("<Control_L>", lambda event: b())
scrollbar.config(command=text_widget.yview)
root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(0, weight=1)


try:
    if v % 2 == 1:
        text_widget.delete('1.0', tk.END)
        with open(a_path, 'r',encoding='utf-8') as f:
            data = f.read()
            text_widget.insert(tk.END, data)
except:
    pass

def save_2():
        file_path = filedialog.asksaveasfilename(parent=root, defaultextension=".txt", filetypes=[
            ("Text files", "*.txt"), ("All files", "*.*")])
        
        with open(a_path, 'w',encoding='utf-8') as f:
             lines = text_widget.get("1.0","end")
             f.writelines(lines)

        if file_path:
            shutil.copy(a_path, file_path)

def i(files):
     msg = '\n'.join((item.decode('gbk') for item in files))
     with open(msg, 'r',encoding='utf-8') as f:
          data = f.read()
          text_widget.insert(tk.END, data)

windnd.hook_dropfiles(root,func=i)
root.protocol('WM_DELETE_WINDOW', on_exit)
threading.Thread(target=icon.run, daemon=True).start()
root.mainloop()