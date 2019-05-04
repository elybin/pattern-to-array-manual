try:
    # for Python2
    from Tkinter import *   ## notice capitalized T in Tkinter 
except ImportError:
    # for Python3
    from tkinter import *   ## notice lowercase 't' in tkinter here
import numpy as np
import array



master = Tk()

# set windows size & pos
x = (master.winfo_screenwidth() - master.winfo_reqwidth()) / 2
y = (master.winfo_screenheight() - master.winfo_reqheight()) / 2
master.geometry("500x500")
master.geometry("+%d+%d" % (x-150, y-200))
master.title("pattern to array maker, by khakim")


array_width = 32
array_height = 32

root = Tk()
root.title("result array")
text = Text(root)

def printresult(myr, myc):
    def wrapper(r=myr, c=myc):
        pass
        pass
        pass
        if(weights[r][c] == 1):
       		weights[r][c] = 0
       	else:
       		weights[r][c] = 1
        print weights
        text.delete(1.0, END)

		# loop 
        mystr = ""
        for r in range(array_height):
       	    for c in range(array_width):
                mystr = mystr + str(weights[r][c]) + ","
                pass
            mystr = mystr + str("\n")
            pass

        text.insert(INSERT, mystr)
        text.pack()
        return True
    return wrapper

weights = np.full((array_width, array_height), 0)

for r in range(array_height):
	for c in range(array_width):
		var1 = Variable()
		Checkbutton(master, borderwidth=0, variable=var1, onvalue="1", offvalue="-1", command= printresult(r,c) ).grid(row=r, column=c, pady=0,padx=0)
		pass
	pass




# text.tag_add("here", "1.0", "1.4")
# text.tag_add("start", "1.8", "1.13")
# text.tag_config("here", background="yellow", foreground="blue")
# text.tag_config("start", background="black", foreground="green")

mainloop()