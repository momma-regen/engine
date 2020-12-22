import json
import os.path
from os import path
from tkinter import *
import tkinter.filedialog as filedialog
import tkinter.messagebox as messagebox
from engine.FileHandler import FileHandler
from engine.File import File
from engine.Img import Img
from PIL import ImageTk

class FileGUI:
    window = None
    current_file = None
    file_lines = []
    loaded_images = []
    
    def __init__(self):
        self.window = Tk()
        self.window.title("File GUI")
        self.current_file = StringVar()
        
        self.window.grid_columnconfigure(0, weight=1)
        
        self.json_frame = Frame()
        self.json_label = Label(master=self.json_frame, text="JSON")
        self.json_text = Text(master=self.json_frame)
        self.json_label.grid(column=0, row=0)
        self.json_text.grid(column=0, row=1)
        self.json_frame.grid(column=0, row=0, sticky="ew")
        
        self.separator1 = Frame(height=2, bd=1, relief=SUNKEN)
        self.separator1.grid(column=0, row=1, sticky="ew")
        
        self.file_frame = Frame()
        self.file_label = Label(master=self.file_frame, text="File To Add")
        self.file_text = Entry(master=self.file_frame, state=DISABLED, textvariable=str(self.current_file))
        self.file_button = Button(master=self.file_frame, text="Browse", command=self.file_pop)
        self.ok_button = Button(master=self.file_frame, text="Add", command=self.file_load)
        self.file_label.grid(column=0, row=0)
        self.file_text.grid(column=1, row=0, sticky="ew")
        self.file_button.grid(column=2, row=0, sticky="e")
        self.ok_button.grid(column=3, row=0, sticky="e")
        self.file_frame.grid(column=0, row=2, sticky="ew")
        
        self.separator2 = Frame(height=2, bd=1, relief=SUNKEN)
        self.separator2.grid(column=0, row=3, sticky="ew")
        
        self.loaded_frame = Frame(height=2, bd=1, relief=SUNKEN)
        self.loaded_frame.grid(column=0, row=4, sticky="ew")
        
        self.separator3 = Frame(height=2, bd=1, relief=SUNKEN)
        self.separator2.grid(column=0, row=5, sticky="ew")
        
        self.save_frame = Frame()
        self.save_button = Button(master=self.save_frame, text="Save", command=self.save)
        self.load_button = Button(master=self.save_frame, text="Load", command=self.load)
        self.save_button.grid(column=0, row=0, sticky="e")
        self.load_button.grid(column=1, row=0, sticky="e")
        self.save_frame.grid(column=0, row=6, sticky="ew")
        
        self.window.mainloop()
        
    def file_pop(self):
        self.window.withdraw()
        try: self.current_file.set(filedialog.askopenfile(mode="rb", title="Choose a file").name)
        except: pass
        self.window.update()
        self.window.deiconify()
        
    def file_load(self):
        if str(self.current_file.get()) == "": return
        indx = len(self.file_lines)
        file_line = Label(master=self.loaded_frame, text=self.file_text.get())
        file_view = Button(master=self.loaded_frame, text="View", command=lambda: self.view_image(indx))
        file_erase = Button(master=self.loaded_frame, text="Remove", command=lambda: self.delete_lines(indx))
        file_line.grid(column=0, row=indx)
        file_view.grid(column=1, row=indx)
        file_erase.grid(column=2, row=indx)
        self.file_lines.append((file_line, file_view, file_erase))
        self.current_file.set("")
        
    def view_image(self, indx, needs_loading = True):
        if needs_loading: img = Img(open(self.file_lines[indx][0].cget("text"), "rb").read())
        else: img = self.loaded_images[indx]
            
        base = Toplevel()
        base.title(self.file_lines[indx][0].cget("text") if needs_loading else f"Image{str(indx+1)}"
        img = ImageTk.PhotoImage(img.display())
        label = Label(base, image=img)
        label.image = img
        label.pack(side = "bottom", fill = "both", expand = "yes")
        
    def delete_lines(self, indx, delete_loaded = False):
        print(indx)
        self.file_lines[indx][0].destroy()
        self.file_lines[indx][1].destroy()
        self.file_lines[indx][2].destroy()
        try:
            if not delete_loaded: self.loaded_images[indx] = None
        except: pass
        self.file_lines[indx] = None
        
    def save(self):
        succ = True
        error = "Unknown Error"
        self.window.withdraw()
        ft=[("Data", "*.dat")]
        try:
            file = File()
            file._filepath = filedialog.asksaveasfile(filetypes=ft, defaultextension=ft).name
            try: file._data = json.loads(self.json_text.get("1.0", END))
            except: file._data = {}
            
            file._images = []
            stopped_at = 0
            for i in range(len(self.file_lines)):
                if self.file_lines[i] == None: continue
                filename = str(self.file_lines[i][0].cget("text"))
                img = self.loaded_images[i] if i < len(self.loaded_images) else Img(open(filename, "rb").read()) if path.exists(filename) else None
                if img: file._images.append(img)
                self.delete_lines(i, i < len(self.loaded_images))
                
            FileHandler().save(file, True)
            succ = path.exists(file._filepath)
        except Exception as e: 
            print(str(e))
            error = str(e)
            succ = False
        
        self.window.update()
        self.window.deiconify()
        if succ: 
            messagebox.showinfo("Success", "File saved successfully")
            self.file_lines = []
            self.current_file.set("")
            self.json_text.delete("1.0", END)
        else: messagebox.showerror("Error", error)
            
    def load(self):
        self.file_pop()
        load_file = self.current_file.get()
        self.current_file.set("")
        self.window.update()
        file = FileHandler().load(load_file)
        self.json_text.delete("1.0", END)
        self.json_text.insert("1.0", json.dumps(file._data))
        self.loaded_images = file._images
        del file
        func = []
        for image in self.loaded_images: self.load_image(image)
            
    def load_image(self, image):
        indx = self.loaded_images.index(image)
        file_line = Label(master=self.loaded_frame, text=f"Image{str(indx+1)}"
        file_view = Button(master=self.loaded_frame, text="View", command=lambda: self.view_image(indx, False))
        file_erase = Button(master=self.loaded_frame, text="Remove", command=lambda: self.delete_lines(indx, True))
        file_line.grid(column=0, row=int(indx))
        file_view.grid(column=1, row=int(indx))
        file_erase.grid(column=2, row=int(indx))
        self.file_lines.append((file_line, file_view, file_erase))
        
FileGUI()