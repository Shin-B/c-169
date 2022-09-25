from tkinter import *
from tkinter import ttk, messagebox



root = Tk()
root.geometry("900x600")
root.title("project 169")

gui=["Label","Button","Dropdown"]

dd=ttk.Combobox(root, state="readonly", values=gui)
dd.pack()

class CreateElements:
    def __init__(self):
        print("This is CreateElements class")
    
    def createLabel(self):
        label = Label(root,text ="A new Label is been created using class", fg="red")
        label.pack()
    
    def createButton(self):
        btn = Button(root, text =" Button ",command = self.message)
        btn.pack(padx=20, pady=10)
        
    def message(self):
        messagebox.showinfo("showinfo", "you clicked the button created using class")
        
    def createdropdown(self):
        numbers=[1,2,3,4,5,6,7,8,9,10]
        dd1=ttk.Combobox(root, state="readonly", values=numbers)
        dd1.pack()
        
    def choose(self):
        global dd
        select=dd.get()
        if(select=="Label"):
            self.createLabel()
        elif(select=="Button"):
            self.createButton()
        elif(select=="Dropdown"):
            self.createdropdown()

obj_of_CreateElements = CreateElements()

btn = Button(root,text = "click to create label and button element", command = obj_of_CreateElements.choose)
btn.pack(padx=20,pady=10)


root.mainloop()