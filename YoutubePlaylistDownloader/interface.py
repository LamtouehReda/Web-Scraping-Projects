import tkinter as tk

class Window:
	def __init__(self,root,title,geometry,download):
		self.root=root
		self.root.title(title)
		self.root.geometry(geometry)
		self.download=download

		self.header=tk.Label(self.root,text='Youtube Playlist Downloader')
		self.header.grid(row=0,column=0)

		self.frame1=tk.Frame(self.root)

		self.urlInpt=tk.Entry(self.frame1)
		self.urlInpt.grid(row=0,column=0)
		self.downloadBtn=tk.Button(self.frame1,text='Download',command=lambda:self.download(self.urlInpt.get()))
		self.downloadBtn.grid(row=0,column=1)

		self.frame1.grid(row=1,column=0)

		self.root.mainloop()

