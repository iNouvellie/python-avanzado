import wx

#Creacion de un objeto
app = wx.App()
#None, elemento padre, -1 asigna un ID al elemento automaticamente, texto es un titulo
frame = wx.Frame(None, -1, 'Primer Ventana')
frame.Show()

app.MainLoop()