from UI.noname import MyFrame1

from Example.wenzi import run


class Face(MyFrame1):
    def OnButtonClick(self, event):
        event.Skip()
        s = run(self.img.Path)
        self.t1.Value = s
