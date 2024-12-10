from tkinter.messagebox import askyesno

def closeWindow(window):
		response = askyesno(
            'Exit',
            'Are you sure you want to exit?'
        )
		if response:
			window.destroy()