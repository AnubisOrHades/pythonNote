import wx

from fun import Face
app = wx.App()

main_win = Face(None)
# print(main_win.m_filePicker1.value)
main_win.Show()

app.MainLoop()