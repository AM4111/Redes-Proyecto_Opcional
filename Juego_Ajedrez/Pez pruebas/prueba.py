from tkinter import *
  
root = Tk() 
  
root.geometry("400x400") 
  
bg = PhotoImage(file = "Imagenes/AD.png") 
  
label1 = Label( root, image = bg) 
label1.place(x = 0, y = 0) 
  
label2 = Label( root, text = "Welcome") 
label2.pack(pady = 50) 
  
frame1 = Frame(root) 
frame1.pack(pady = 20 ) 
  
button1 = Button(frame1,text="Exit") 
button1.pack(pady=20) 
  
button2 = Button( frame1, text = "Start") 
button2.pack(pady = 20) 
  
button3 = Button( frame1, text = "Reset") 
button3.pack(pady = 20) 
  
root.mainloop()
