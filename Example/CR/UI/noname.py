# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc


###########################################################################
## Class MyFrame1
###########################################################################

class MyFrame1(wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=wx.EmptyString, pos=wx.DefaultPosition,
                          size=wx.Size(800, 600), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)

        gSizer1 = wx.GridSizer(0, 2, 0, 0)

        self.img = wx.FilePickerCtrl(self, wx.ID_ANY, wx.EmptyString, u"Select a file", u"*.png*", wx.DefaultPosition,
                                     wx.DefaultSize, wx.FLP_DEFAULT_STYLE)
        gSizer1.Add(self.img, 0, wx.ALL, 5)

        self.start = wx.Button(self, wx.ID_ANY, u"start", wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer1.Add(self.start, 0, wx.ALL, 5)

        self.t1 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer1.Add(self.t1, 0, wx.ALL | wx.EXPAND, 5)

        self.t2 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer1.Add(self.t2, 0, wx.ALL | wx.EXPAND, 5)

        self.SetSizer(gSizer1)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.start.Bind(wx.EVT_BUTTON, self.OnButtonClick)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def OnButtonClick(self, event):
        event.Skip()
