from tkinter import *

def button_click():
    a_form = Toplevel()
    #a_form = Tk()
    a_label = Label(a_form, text='this is another label')
    a_label.bind('<Control-Button-1>', bind_close)
    a_button = Button(a_form, text='close form', command=lambda: close_form(a_button))
    a_label.pack()
    a_button.pack(fill=X)
    

def close_form(self):
    self.master.destroy()
    return
    '''
    if isinstance(self.master, Tk):
        self.master.quit() # close application
    else:
        self.master.destroy() # close form
    '''

def bind_close(ev=None):
    ev.widget.master.destroy()


def main():
    root = Tk()
    label = Label(root, text='this is a label packed left')
    button = Button(root, text='this is a command exit button', command=root.destroy)
    frame = LabelFrame(root, text='label frame')
    frame_button = Button(frame, text='open another form', command=button_click)
    exit_button = Button(root, text='Exit (lambda)', command=lambda: close_form(exit_button))


    label.pack(side='left')
    button.pack(side='left')
    frame.pack()
    frame_button.pack()
    exit_button.pack(fill=X)

    root.mainloop()
    
if __name__=='__main__':
    main()
    
