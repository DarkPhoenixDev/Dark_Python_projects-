import tkinter
window = tkinter.Tk(className="miles to km converter")
window.minsize(width=500,height=500)
milesinput = tkinter.Entry()
milesinput.grid(column=1,row=0)
def ans():
     result = float(milesinput.get())*1.609 
     kmresult["text"] = f"{round(result)} km "
miles = tkinter.Label(text="miles")
miles.grid(column=2,row=0)
isequalto= tkinter.Label(text="isequalto")
isequalto.grid(column=0,row=1)
km = tkinter.Label(text="km")
km.grid(column=1,row=1)
kmresult = tkinter.Label(text="0")
kmresult.grid(column=2,row=1)
button = tkinter.Button(text="Calculte",command=ans)
button.grid(column=1,row=2)
window.mainloop()



