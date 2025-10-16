import tkinter as tk
from tkinter import ttk, messagebox
import threading
from fortune_generator import generate_fortune
from render_html import render_to_html
import webbrowser
import datetime


def run_gui():
    root = tk.Tk()
    root.title('AI Fortune')
    root.geometry('480x260')

    frm = ttk.Frame(root, padding=12)
    frm.pack(fill='both', expand=True)

    ttk.Label(frm, text='Enter birth date (YYYY-MM-DD):').grid(row=0, column=0, sticky='w')
    date_var = tk.StringVar()
    entry = ttk.Entry(frm, textvariable=date_var)
    entry.grid(row=1, column=0, sticky='we', pady=6)

    theme_var = tk.StringVar(value='china')
    ttk.Label(frm, text='Theme:').grid(row=2, column=0, sticky='w')
    theme_cb = ttk.Combobox(frm, textvariable=theme_var, values=['china', 'minimal'], state='readonly')
    theme_cb.grid(row=3, column=0, sticky='we')

    def on_generate():
        s = date_var.get().strip()
        try:
            dt = datetime.datetime.strptime(s, '%Y-%m-%d').date()
        except Exception:
            messagebox.showerror('Error', 'Date format should be YYYY-MM-DD')
            return
        f = generate_fortune(dt)
        out = render_to_html(f, theme=theme_var.get())
        webbrowser.open('file://' + out)

    btn = ttk.Button(frm, text='生成并打开 HTML', command=on_generate)
    btn.grid(row=4, column=0, pady=12)

    for i in range(1):
        frm.columnconfigure(i, weight=1)

    root.mainloop()
