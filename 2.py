from Tkinter import *
from PIL import Image

class App:

    def __init__(self, master):

        frame = Frame(master)
        frame.pack()

	photo = """
R0lGODlhDwASAKUAAAAAAEY6J1FELltILFVLM19UOmNWM2NXQGlcO4BdJm5hRnFjOnVoRXluWZpw
G31yXoiAbpiDQ4qEc8J/EsCBEpKMeJWQfNeMEbWWI5uYjdmYEuubD/6kDO6qEP6oDe2wEf6sDf6x
Drq4sv61Du+9Ev65Dui/Fv69D9bGMP7FEP7KEObUOe3VHf7SE/7ZFf7cFtfW0/zgGPzhGP/jGP/k
GP/pGfnuIv/tG//yHOrp6O/v7vb29v///wAAAAAAAAAAACH/C05FVFNDQVBFMi4wAwEAAAAh+QQJ
CgA/ACwAAAEADwARAAAGsMCfcGdhIBYIRWUnbMIWKxvuVmNhDrBmJiLF4Wq1mMtkyPx0hK63NhOr
SAFdBXXDAQBU2V2VckgKMjV4NwA0AC0pACcfAgYyNDQ3NzQvLYgnJSUCCy53np93IQMELQA8PKan
qQAhAQQkq6eoqhsEEBixqqoOEDAGJaapswAcA1kPDsDCdxwOD0I6AR0joBwbcU05ARogHh4cHBcB
OU1COQcJFBcTCQXk5U0iDwoNIvBBACH5BAkKAD8ALAAAAAAPABEAAAawwJ9wZ2EgFghFZSdswhYr
G+5WY2EOsGYmIsXharWYy2TI/HSErrc2E6tIAV0FdcMBAFTZXZVySAoyNXg3ADQALSkAJx8CBjI0
NDc3NC8tiCclJQILLneen3chAwQtADw8pqepACEBBCSrp6iqGwQQGLGqqg4QMAYlpqmzABwDWQ8O
wMJ3HA4PQjoBHSOgHBtxTTkBGiAeHhwcFwE5TUI5BwkUFxMJBeTlTSIPCg0i8EEAOw==
	"""

	img1 = PhotoImage(data=photo)
	img = PhotoImage(file="b.gif")

        self.button = Button(frame, text="QUIT", fg="red", command=frame.quit)
        self.button.pack(side=LEFT)
	self.button.config(relief=SUNKEN)

        self.hi_there = Button(frame, image=img1, text="Hello", compound=LEFT, command=self.say_hi, pady=50)
	self.hi_there.img = img1
        self.hi_there.pack(fill=BOTH, expand=1)


	Button(frame, text="Hello", command=self.say_hi).pack(side=LEFT)
	
	self.v = IntVar()
	self.v.set(1)

	c1 = Checkbutton(master, text="Don't show this again", variable=self.v)
	c1.var33 = self.v
	c1.pack(side=LEFT)

    def say_hi(self):
        print "hi there, everyone!", self.v.get()

root = Tk()

app = App(root)

root.mainloop()
