from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from label_maker import LabelMaker

def select_file():
    filepath.set(filedialog.askopenfilename(
        title='Select a file'))

def select_save_file():
    save_filepath.set(filedialog.asksaveasfilename(
        title='Select a file'))
    
def select_directory():
    directory_path.set(filedialog.askdirectory(
        title='Choose a folder'
    ))

def select_save_directory():
    save_directory_path.set(filedialog.askdirectory(
        title='Choose a folder'
    ))
    
def label_single():
    lm.label_single(filepath.get(), save_filepath.get())

def label_multiple():
    lm.label_multiple(directory_path.get(), save_directory_path.get())
    
lm = LabelMaker()
# before initiating labeling check that files are .lsx

root = Tk()
root.title = 'BG3 Dialogue XML Label Maker'

mainframe = ttk.Frame(root, padding=(3, 3, 12, 12))
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))


# Label single file
filepath = StringVar()

button_select_single = Button(mainframe, text="Select a File to Label...", command = select_file, width=20)
entry_select_single = Entry(mainframe, textvariable=filepath, width=150)

save_filepath = StringVar()
button_save_single = Button(mainframe, text="Save Labeled File As...", command = select_save_file, width=20)
entry_save_single = Entry(mainframe, textvariable=save_filepath, width=150)

# label button
button_label_file = Button(mainframe, text="Label File", command=label_single, width=15)

# label single positioning
Label(mainframe, text="Label a Single File").grid(column=1, row=1, columnspan=2, sticky=(W,E))

button_select_single.grid(column=1,row=2)
entry_select_single.grid(column=2, row=2)
button_save_single.grid(column=1,row=3)
entry_save_single.grid(column=2, row=3)

button_label_file.grid(column=2,row=4, sticky=E)

# label folder/multiple
directory_path = StringVar()
button_select_directory = Button(mainframe, text="Select a Folder to Label...", command=select_directory, width=20)
entry_select_directory = Entry(mainframe, textvariable=directory_path, width=150)


save_directory_path = StringVar()
button_save_directory = Button(mainframe, text="Select a Save Folder...", command=select_save_directory, width=20)
entry_save_directory = Entry(mainframe, textvariable=save_directory_path, width=150)

button_label_directory = Button(mainframe, text="Label Folder", command=label_multiple, width=15)

# label multiple positioning
Label(mainframe, text='Label Many Files at Once').grid(column=1, row=5, columnspan=2, sticky=(W,E))

button_select_directory.grid(column=1,row=6)
entry_select_directory.grid(column=2, row=6)
button_save_directory.grid(column=1,row=7)
entry_save_directory.grid(column=2, row=7)

button_label_directory.grid(column=2,row=8, sticky=E)


# exit button
# button_exit = Button(mainframe, 
#                      text = "Exit",
#                      command = exit,
#                      width=10)


# button_exit.grid(column=1, row=9)

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
mainframe.columnconfigure(2, weight=1)
for child in mainframe.winfo_children(): 
    child.grid_configure(padx=5, pady=5)



root.mainloop()