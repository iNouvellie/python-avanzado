import wx

class Ventana_Ejemplo(wx.Frame):
	def __init__(self, parent, title):
		super(Ventana_Ejemplo, self).__init__(parent, title = "Segunda ventana", size = (200,200))
		#Dejar la ventana al medio
		#self.Centre()
		#Elegir posicion mediante X y Y coordenadas
		self.SetPosition((10, 10))
		self.Show(True)

if __name__ == '__main__':
	app = wx.App()
	Ventana_Ejemplo(None, title = 'Nueva ventana')
	app.MainLoop()