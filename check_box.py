import tkinter as tk
from tkinter import ttk
import win32api
from win32api import GetSystemMetrics
from tkinter import font


root = tk.Tk()
text = tk.Text(root)
screen_width = GetSystemMetrics(0)  #/screen_width = root.winfo_screenwidth()
screen_height = GetSystemMetrics(1) #screen_height = root.winfo_screenwidth()
window_width = 400
window_height = 200
x_position = (screen_width/2 ) - (window_width/2)
y_position = (screen_height/2) - (window_height/2)

#print(screen_height)
#print(screen_width)
root.geometry(f'{window_width}x{window_height}+{int(x_position)}+{int(y_position)}')
root.iconbitmap("app.ico")
root.title("Application Form")
root.resizable(False,False)

#font object
label_font = font.Font(weight="bold")
 

#variables
check_1v = tk.StringVar()
check_2v = tk.StringVar() 
#function

def submit():
    #print(check_1v.get())
    #print(check_2v.get())
    check_1_val = check_1v.get()
    check_2_val = check_2v.get()
    #print("my"+check_1_val)
    #if check_1_val=="1":
    #    print("success")
    name = entry_1.get()
    if name == "":
        label_4.pack()
        label_4.configure(text="Please enter your name")

    else:
        label_4.pack_forget()
        name = entry_1.get()
        if check_1_val =="1" and check_2_val == "1" or check_1_val == "0" and check_2_val == "1" or check_1_val == "" and check_2_val == "1" or check_1_val == "0" and check_2_val == "0" or check_1_val == "" and check_2_val == ""  :
           root_fail = tk.Toplevel(root)  
           window_1_width = 300
           window_1_height = 100
           x_1_position = (screen_width/2 ) - (window_1_width/2)
           y_1_position = (screen_height/2) - (window_1_height/2)
           root_fail.geometry(f'{window_1_width}x{window_1_height}+{int(x_1_position)}+{int(y_1_position)}')
           root_fail.iconbitmap("wrong.ico")
           root_fail.title("submission faild ")
           root_fail.resizable(False,False)
           label_3 = ttk.Label(root_fail, text="Dear "+str(name)+" Faild !",background="red" , font=label_font, foreground="white")
           label_3.pack()
        


        elif check_1_val == "1" and check_2_val == "" or check_1_val == "1" and check_2_val == "0":       
           root_pass = tk.Toplevel(root)  
           window_1_width = 300
           window_1_height = 100
           x_1_position = (screen_width/2 ) - (window_1_width/2)
           y_1_position = (screen_height/2) - (window_1_height/2)
           root_pass.geometry(f'{window_1_width}x{window_1_height}+{int(x_1_position)}+{int(y_1_position)}')
           root_pass.iconbitmap("correct.ico")
           root_pass.title("submission success ")
           root_pass.resizable(False,False)
           label_2 = ttk.Label(root_pass, text="Dear "+str(name)+" successful !",background="green", font=label_font, foreground="white")
           label_2.pack() 
        
 
    
#weigets
label_1 = ttk.Label(root)
label_1.pack()
label_1.configure(text="Enter Your name :-")

entry_1 = ttk.Entry(root, width=40,)
entry_1.pack()

label_4 = ttk.Label(root, foreground="red",padding=10)
 
 

agree = ttk.Label(root)
agree.pack(anchor = "w",pady=5,padx=75)
agree.configure(text=" This Agreement shall apply to all investments made by investors of either Contracting Party in the territory of the other Contracting Party, accepted as such in accordance with its laws and regulations, whether made before or after the coming into force of this Agreement.") 

check_1 = ttk.Checkbutton(root, text="Yes. I'm agree", width=200,variable=check_1v)
check_1.pack(anchor = "w",pady=5,padx=75)

check_2 = ttk.Checkbutton(root, text="No. I'm not agree",width=200, variable=check_2v)
check_2.pack(anchor = "w", padx=75)

btn = ttk.Button(root, text="submit", command=submit)
btn.pack(pady=10)

#weiget 2

tk.mainloop()