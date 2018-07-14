import wx

#Creacion de un objeto
app = wx.App()
#None, elemento padre, -1 asigna un ID al elemento automaticamente, texto es un titulo
frame = wx.Frame(None, -1, 'Primer Ventana', style = wx.MINIMIZE_BOX | wx.MAXIMIZE_BOX | wx.RESIZE_BORDER | wx.SYSTEM_MENU | wx.CAPTION | wx.CLOSE_BOX)
frame.Show()

app.MainLoop()