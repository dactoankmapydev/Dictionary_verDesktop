# -*- encoding: utf-8 -*-

import requests
#import queuelib
from tkinter import*
from bs4 import BeautifulSoup
from tkinter import scrolledtext

app = Tk()
app.resizable(0, 0)
app.geometry("599x225")
app.title(u"TRA TỪ ANH - VIỆT - ANH   ")
app.configure(bg="light blue")

def search():
    req = requests.get(
        "http://dict.laban.vn/find?type=&query=" + str(keyWord.get()))
    textPlain = req.text
    parse = BeautifulSoup(textPlain, "html.parser")
    data = parse.find_all("li", {"class": "slide_content", "rel": "0"})
    for item in data:
        words = item.find_all(
            "div", {
                "id": "content_selectable", "class": "content"})[0].text
        meaningText.configure(state='normal')
        meaningText.delete(1.0, END)
        meaningText.insert(INSERT, words)
        meaningText.configure(state='disabled')


def hideText(click):
    if  wordText.get() == u"Nhập từ và nhấn Enter để tra ":
        wordText.delete(0, "end")
        wordText.insert(0, '')

keyWord = StringVar()
meaning = StringVar()

wordText = Entry(
    app,
    width=57,
    textvariable=keyWord,
    font=(
        'Verdana',
        11),
    fg='red',
    justify='center')
wordText.grid(row=0, column=1, padx=3, pady=4)

wordText.insert(0, u"Nhập từ và nhấn Enter để tra ")
wordText.bind('<FocusIn>', hideText)
wordText.bind("<Return>", (lambda event: search()))

button_search = Button(
    app,
    text='',
    bg='light green',
    fg='white',
    command=(
        lambda: search()))
button_search.grid(row=1, column=1)

meaningText = scrolledtext.ScrolledText(
    app,
    state='disabled',
    width=57,
    wrap=WORD,
    height=10,
    font=(
        'Verdana',
        11),
    fg="blue")
meaningText.grid(row=1, column=1, padx=3, pady=3, columnspan=2, sticky="WE")

app.mainloop()
