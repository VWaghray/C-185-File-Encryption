from tkinter import *
from tkinter import filedialog as fd
import hashlib

root=Tk()
root.geometry("250x190")
root.configure(bg="brown")

def apply_md5():
    text_file = fd.askopenfilename(title="Text file", filetypes=(("Text Files", "*.txt"),))
    print(text_file)
    text_file = open(name, 'r')
    paragraph = text_file.read()
    file_result = hashlib.md5(paragraph.encode())
    file_hexd = file_result.hexdigest()
    md5_file = open("md5.txt","w")
    md5_file.write(file_hexd)
    print("MD5 function")
    
    
def apply_sha256():
    text_file1 = fd.askopenfilename(title="Text file", filetypes=(("Text Files", "*.txt"),))
    print(text_file1)
    text_file1 = open(name, 'r')
    paragraph1 = text_file1.read()
    file_result1 = hashlib.sha256(paragraph1.encode())
    file_hexd1 = file_result1.hexdigest()
    sha256_file = open("sha256.txt","w")
    sha256_file.write(file_hexd1)
    print("MD5 function")
    print("SHA function")   
    
    
btn=Button(root, text="Apply MD5",command=apply_md5,bg="green",fg="brown",relief=SUNKEN)
btn.place(relx=0.3,rely=0.5, anchor=CENTER)
btn1=Button(root, text="Apply SHA256",command=apply_sha256,bg="green",fg="brown",relief=SUNKEN)
btn1.place(relx=0.7,rely=0.5, anchor=CENTER)
root.mainloop()