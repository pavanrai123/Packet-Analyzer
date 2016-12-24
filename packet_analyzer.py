import binascii
from Tkinter import *
from scapy.all import *
load_contrib('mim')
root =Tk()
root.wm_title("Packet Analyzer")
text_box=Text(root)
text_box2=Text(root)

def getData():
    text_ws=text_box.get("1.0",'end-1c')
    text_ws=text_ws.replace("\n"," ")
    text_ws=text_ws.replace(" ","")

    a=binascii.unhexlify(text_ws)
    #b=binascii.hexlify(a)
    b=Ether(a)

    file1 = open('myfile.txt','w')
    old_stdout = sys.stdout
    sys.stdout = file1
    b.show()
    file1.close()
   
    file2 = open("myfile.txt")
    data = file2.read()
    file2.close()
    text_box2.insert(INSERT,data)
   

submit = Button(root, text ="Parse", command = getData)

class CCP(Text):
    def __init__(self, master, **kw):
        Text.__init__(self, master, **kw)
        self.bind('<Control-c>', self.copy)
        self.bind('<Control-x>', self.cut)
        self.bind('<Control-v>', self.paste)
       
    def copy(self, event=None):
        self.clipboard_clear()
        text = self.get("sel.first", "sel.last")
        self.clipboard_append(text)
   
    def cut(self, event):
        self.copy()
        self.delete("sel.first", "sel.last")

    def paste(self, event):
        text = self.selection_get(selection='CLIPBOARD')
        self.insert('insert', text)

#binascii.unhexlify('00021537A24400AEF352AAD108004500')
CCP(text_box)
CCP(text_box2)
text_box.pack()
submit.pack(side =BOTTOM)
text_box2.pack()
root.mainloop()

