# coding: utf-8
# %load goto_class.py
#!/usr/bin/env python

import wx

class myFrame(wx.Frame):

    def __init__(self, parent, title):
        super(myFrame, self).__init__(parent, title=title)
        
        self.Center()
        
        panel = wx.Panel(self)
        
        font = wx.SystemSettings.GetFont(wx.SYS_SYSTEM_FONT)
        font.SetPointSize(9)
        
        vbox = wx.BoxSizer(wx.VERTICAL)
        
        hbox1 = wx.BoxSizer(wx.HORIZONTAL)
        st1 = wx.StaticText(panel, label='Class Name')
        st1.SetFont(font)
        hbox1.Add(st1, flag=wx.RIGHT, border=8)
        tc =wx.TextCtrl(panel)
        hbox1.Add(tc, proportion=1)
        vbox.Add(hbox1, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=8)
            
        vbox.Add((-1,10))
        
        panel.SetSizer(vbox)
       
        hbox2 = wx.BoxSizer(wx.HORIZONTAL)
        st2 = wx.StaticText(panel, label='Matching Classes')
        st2.SetFont(font)
        hbox2.Add(st2)
        tc = wx.TextCtrl(panel)
        hbox2.Add(tc, proportion=1)
        vbox.Add(hbox2, flag=wx.LEFT|wx.TOP, border=10)
        
        vbox.Add((-1, 10))
        
        hbox3 = wx.BoxSizer(wx.HORIZONTAL)
        tc = wx.TextCtrl(panel, style=wx.TE_MULTILINE)
        hbox3.Add(tc, proportion=1, flag=wx.EXPAND)
        vbox.Add(hbox3, flag=wx.LEFT|wx.RIGHT|wx.EXPAND, border=10)
        
        vbox.Add((-1, 25))
        

def main():
   
    app = wx.App()
    ex = myFrame(None, title='Go to Class')
    ex.Show()
    app.MainLoop()

if __name__ == '__main__':
    main()
