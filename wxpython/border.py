# coding: utf-8
import wx

class myFrame(wx.Frame):
    
    def __init__(self, parent, title):
        super(myFrame, self).__init__(parent, title=title)
        
        panel = wx.Panel(self)
        panel.SetBackgroundColour('gray')
        
        vbox = wx.BoxSizer(wx.VERTICAL)
        
        Pan1 = wx.Panel(panel)
        Pan1.SetBackgroundColour('white')

        Pan2 = wx.Panel(panel)
        Pan2.SetBackgroundColour('red')
        
        Pan3 = wx.Panel(panel)
        Pan3.SetBackgroundColour('blue')
        
        img1 = wx.StaticBitmap(Pan1, wx.ID_ANY, wx.Bitmap('./img/1.jpg', wx.BITMAP_TYPE_ANY)) 
        img2 = wx.StaticBitmap(Pan2, wx.ID_ANY, wx.Bitmap('./img/2.jpg', wx.BITMAP_TYPE_ANY)) 
        img3 = wx.StaticBitmap(Pan3, wx.ID_ANY, wx.Bitmap('./img/3.jpg', wx.BITMAP_TYPE_ANY)) 
        
        vbox.Add(Pan1, wx.ID_ANY, wx.EXPAND | wx.ALL, 10)
        vbox.Add(Pan2, wx.ID_ANY, wx.EXPAND | wx.ALL, 10)
        vbox.Add(Pan3, wx.ID_ANY, wx.EXPAND | wx.ALL, 10)
        
        panel.SetSizer(vbox)
        

def main():
    
    app = wx.App()
    frame = myFrame(None, title='Border')
    frame.Show()
    app.MainLoop()
    
if __name__ == '__main__':
    main()