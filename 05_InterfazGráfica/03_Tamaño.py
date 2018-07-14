import wx

class Ventana_Ejemplo(wx.Frame):
	def __init__(self, parent, title):
		super(Ventana_Ejemplo, self).__init__(parent, title = "Segunda ventana", size = (20,20))
		self.Show(True)

#Creacion de un objeto
app = wx.App()
#None, elemento padre, -1 asigna un ID al elemento automaticamente, texto es un titulo
#frame = wx.Frame(None, -1, 'Primer Ventana', size = (400,400), style = wx.MINIMIZE_BOX | wx.MAXIMIZE_BOX | wx.RESIZE_BORDER | wx.SYSTEM_MENU | wx.CAPTION | wx.CLOSE_BOX)
#frame.Show()

#app.MainLoop()

ventana = Ventana_Ejemplo(None, 'Hola')

#Mantiene la ventana ejemplo abierta
app.MainLoop()