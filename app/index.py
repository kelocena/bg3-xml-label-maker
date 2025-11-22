from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from label_maker import LabelMaker

def select_file():
    # try:
    filepath.set(filedialog.askopenfilename(
        title='Select a file'))
    
    # if same path as save_filepath, display warning??
    
    # except:
    #     print('we broken')
    #     exit

def select_save_file():
    save_filepath.set(filedialog.asksaveasfilename(
        title='Select a file'))
    
def label_single():
    lm.label_single(filepath.get(), save_filepath.get())
    
lm = LabelMaker()
# before initiating labeling check that files are .lsx

root = Tk()
root.title = 'BG3 Dialogue XML Label Maker'

# init label maker with dictionaries?
mainframe = ttk.Frame(root, padding=(3, 3, 12, 12))
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))

filepath = StringVar()
button_select_single = Button(mainframe, text="Select a File to Label...", command = select_file)
entry_select_single = Entry(mainframe, textvariable=filepath, width=150)

save_filepath = StringVar()
button_save_single = Button(mainframe, text="Save Labeled File As...", command = select_save_file)
entry_save_single = Entry(mainframe, textvariable=save_filepath, width=150)

# label button
button_label_file = Button(mainframe, text="Label", command=label_single, width=15)


button_exit = Button(mainframe, 
                     text = "Exit",
                     command = exit,
                     width=10)

button_select_single.grid(column=1,row=1)
entry_select_single.grid(column=2, row=1)
button_save_single.grid(column=1,row=2)
entry_save_single.grid(column=2, row=2)

button_label_file.grid(column=2,row=3, sticky=W)

button_exit.grid(column=2, row=5, pady=10, sticky=E)

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
mainframe.columnconfigure(2, weight=1)
for child in mainframe.winfo_children(): 
    child.grid_configure(padx=5, pady=5)



root.mainloop()