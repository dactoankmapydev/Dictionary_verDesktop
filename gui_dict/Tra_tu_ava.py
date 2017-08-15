# -*- encoding: utf-8 -*-

import requests
import queuelib
from Tkinter import*
from bs4 import BeautifulSoup
from tkinter import scrolledtext


app = Tk()
app.resizable(0, 0)
app.geometry("599x225")
app.title(u"TRA TỪ ANH - VIỆT - ANH   ")
app.configure(bg="light blue")


def tratu():
    source_code = requests.get(
        "http://dict.laban.vn/find?type=&query=" + str(word.get().encode('utf-8')))
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, "html.parser")
    data = soup.find_all("li", {"class": "slide_content ", "rel": "0"})
    for item in data:
        words = item.find_all(
            "div", {
                "id": "content_selectable", "class": "content"})[0].text
        txtMeaning.configure(state='normal')
        txtMeaning.delete(1.0, END)
        txtMeaning.insert(INSERT, words)
        txtMeaning.configure(state='disabled')


def text_hide(click):
    if txtWord.get() == u"Nhập từ và nhấn Enter để tra ":
        txtWord.delete(0, "end")
        txtWord.insert(0, '')


word = StringVar()
meaning = StringVar()

txtWord = Entry(
    app,
    width=57,
    textvariable=word,
    font=(
        'Verdana',
        11),
    fg='red',
    justify='center')
txtWord.grid(row=0, column=1, padx=3, pady=4)

txtWord.insert(0, u"Nhập từ và nhấn Enter để tra ")
txtWord.bind('<FocusIn>', text_hide)

txtWord.bind("<Return>", (lambda event: tratu()))

nut_tratu = Button(
    app,
    text='',
    bg='light green',
    fg='white',
    command=(
        lambda: tratu()))
nut_tratu.grid(row=1, column=1)

txtMeaning = scrolledtext.ScrolledText(
    app,
    state='disabled',
    width=57,
    wrap=WORD,
    height=10,
    font=(
        'Verdana',
        11),
    fg="blue")
txtMeaning.grid(row=1, column=1, padx=3, pady=3, columnspan=2, sticky="WE")

app.mainloop()
