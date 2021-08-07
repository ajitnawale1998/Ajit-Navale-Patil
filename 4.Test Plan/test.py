'''from tkinter import *
from tkinterhtml import HtmlFrame
from six.moves import urllib
root=Tk()
root.geometry("600x500+350+400")
frame = HtmlFrame(root, horizontal_scrollbar="auto")

#frame.set_content("<html></html>")
frame.set_content(urllib.request.urlopen("http://www.journaldev.com/33306/pandas-read_excel-reading-excel-file-in-python").read().decode())
root.mainloop()
from tkinter import *
import webbrowser

def callback(url):
    webbrowser.open_new(url)

root = Tk()
link1 = Label(root, text="Google Hyperlink", fg="blue", cursor="hand2")
link1.pack()
link1.bind("<Button-1>", lambda e: callback("http://www.google.com"))

link2 = Label(root, text="Ecosia Hyperlink", fg="blue", cursor="hand2")
link2.pack()
link2.bind("<Button-1>", lambda e: callback("http://www.ecosia.org"))

root.mainloop()
'''

from tkinter import*
from tkinter.ttk import*
import webbrowser
import functools
after_prediction_page1=Tk()
after_prediction_page1.geometry("600x500+300+250")

def link_redirecting(value):
    text1="The soil is "+value
    Label(after_prediction_page1,font=('Boulder',20,'italic'),text=text1).place(x=75,y=100)
    def callback(url):
        webbrowser.open_new(url)
    if value == "Laterite Soil":
        list1=['rice',"cashew","rubber","tea","coffee"]
            
        link1=Label(after_prediction_page1,text="Rice",cursor="hand2")
        link1.place(x=60,y=250)
        link1.bind("<Button-1>", lambda e: callback("http://www.google.com"))

        link2 = Label(after_prediction_page1, text="Cashew", cursor="hand2")
        link2.place(x=60,y=280)
        link2.bind("<Button-1>", lambda e: callback("http://www.ecosia.org"))

        link3 = Label(after_prediction_page1, text="Rubber", cursor="hand2")
        link3.place(x=60,y=310)
        link3.bind("<Button-1>", lambda e: callback("http://www.ecosia.org"))


        link4 = Label(after_prediction_page1, text="Tea", cursor="hand2")
        link4.place(x=60,y=340)
        link4.bind("<Button-1>", lambda e: callback("http://www.ecosia.org"))

        link5 = Label(after_prediction_page1, text="Coffee", cursor="hand2")
        link5.place(x=60,y=370)
        link5.bind("<Button-1>", lambda e: callback("http://www.ecosia.org"))
